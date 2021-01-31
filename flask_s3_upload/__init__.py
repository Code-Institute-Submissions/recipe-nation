from .helpers import *
from flask import Flask, render_template, request, redirect
from werkzeug.security import secure_filename

app = Flask(__name__)
app.config.from_object("flask_s3_upload.config")


@app.route("/add_recipe", methods=["POST"])
def upload_file():
    if "user_file" not in request.files:
        return "No user_file key in request.files"
    file = request.files["user_file"]
    if file.filename == "":
        return "Please select a file"
    if file and allowed_file(file.filename):
        file.filename = secure_filename(file.filename)
        output = upload_file_to_s3(file, app.config["S3_BUCKET"])
        return str(output)

    else:
        return redirect("/")
