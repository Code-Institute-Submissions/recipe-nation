import os
import boto3
import botocore
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
if os.path.exists("env.py"):
    import env


# flask
app = Flask(__name__)

# mondodb
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


mongo = PyMongo(app)


# Amazon S3 Bucket
S3_BUCKET_NAME = os.environ.get("S3_BUCKET_NAME")
S3_ACCESS_KEY = os.environ.get("S3_ACCESS_KEY")
S3_SECRET_ACCESS_KEY = os.environ.get("S3_SECRET_ACCESS_KEY")
S3_LOCATION = 'http://recipe-image-repo.s3.eu-west-2.amazonaws.com/'.format(
    S3_BUCKET_NAME)


s3 = boto3.client(
    "s3",
    aws_access_key_id=S3_ACCESS_KEY,
    aws_secret_access_key=S3_SECRET_ACCESS_KEY
)

# Image upload restrictions
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif"}

# Amazon S3 Bucket Functions


def allowed_file(filename):

    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def upload_file():
    # Output will be blank if user_file key not found on submission
    output = ""

    if "user_file" not in request.files:

        return output

    # If the key is in the object, save it in file variable
    file = request.files["user_file"]

    # Check the filename, if it's blank, leave it blank
    if file.filename == "":

        return output

    # Check that there is a file and that it has an allowed filetype
    if file and allowed_file(file.filename):
        file.filename = secure_filename(file.filename)
        output = upload_file_to_s3(file)

    return output


def upload_file_to_s3(file, acl="public-read"):
    try:
        # Upload image to s3
        s3.upload_fileobj(
            file,
            S3_BUCKET_NAME,
            file.filename,
            ExtraArgs={
                'ACL': acl,
                "ContentType": file.content_type
            }
        )

    except Exception as e:
        print("Something Happened: ", e)
        return e

    return "{}{}".format(S3_LOCATION, file.filename)


# Routes
@app.route("/")
@app.route("/get_recipes")
def recipes():
    recipes = list(mongo.db.recipes.find())
    for recipe in recipes:
        try:
            recipe["user_id"] = mongo.db.users.find_one(
                {"_id": recipe["user_id"]})["username"]
        except:
            pass
    return render_template("index.html", recipes=recipes)


@app.route("/search", methods=["GET", "POST"])
def search():
    if request.method == "POST":
        query = request.form.get("query")
        recipes = list(mongo.db.recipes.find({"$text": {"$search": query}}))
        all_recipes = list(mongo.db.recipes.find())
        print(recipes)
        for recipe in recipes:
            try:
                recipe["user_id"] = mongo.db.users.find_one(
                {"_id": recipe["user_id"]})["username"]
            except:
                pass
        return render_template("search.html", recipes=recipes)

    return render_template("search.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(request.form.get("username").capitalize()))
                return redirect(url_for(
                    "profile", username=session["user"]))

            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's username from db
    recipes = list(mongo.db.recipes.find())
    if session["user"]:
        for recipe in recipes:
            try:
                recipe["user_id"] = mongo.db.users.find_one(
                    {"_id": recipe["user_id"]})["username"]
            except:
                pass
        return render_template("profile.html", username=username.capitalize(), recipes=recipes)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    flash("You've been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    if request.method == "POST":
        user = mongo.db.users.find_one({"username": session["user"]})
        new_recipe = {
            "recipe_name": request.form.get("recipe_name"),
            "prep_time": request.form.get("prep_time"),
            "cook_time": request.form.get("cook_time"),
            "ingredients": request.form.getlist("ingredients"),
            "method": request.form.getlist("method"),
            "type": request.form.getlist("type"),
            "user_file": upload_file(),
            "user_id": ObjectId(user["_id"])
        }
        mongo.db.recipes.insert_one(new_recipe)
        flash("Recipe Successfully Added")
        return redirect(url_for("add_recipe"))

    types = mongo.db.types.find().sort("type", 1)
    return render_template("add_recipe.html", types=types)


@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    if request.method == "POST":
        user = mongo.db.users.find_one({"username": session["user"]})
        edit_recipe = {
            "recipe_name": request.form.get("recipe_name"),
            "prep_time": request.form.get("prep_time"),
            "cook_time": request.form.get("cook_time"),
            "ingredients": request.form.getlist("ingredients"),
            "method": request.form.getlist("method"),
            "type": request.form.getlist("type"),
            "user_file": request.form.get("user_file"),
            "user_id": ObjectId(user["_id"])
        }
        mongo.db.recipes.update({"_id": ObjectId(recipe_id)}, edit_recipe)
        flash("Recipe Successfully Edited")

    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    types = mongo.db.types.find().sort("type", 1)
    return render_template("edit_recipe.html", recipe=recipe, types=types)


@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    flash("Recipe Deleted")
    return redirect(url_for("search"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
# Remember to change debug to False before submitting project
