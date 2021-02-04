# [Recipe Nation](https://recipe-nation.herokuapp.com/)

## Contents
1. [Summary](#summary)
1. [UX](#ux)
    1. [Strategy](#strategy)
    1. [Scope](#scope)
    1. [Structure](#structure)
    1. [Skeleton](#skeleton)
    1. [Surface](#surface)
1. [Features](#features)
    1. [Existing Features](#existing-features)
    1. [Features left to implement](#left-to)
1. [Bugs](#bugs)
1. [Technologies used](#tech)
1. [Testing](#testing)
1. [Deployment](#deployment)
    1. [Github Pages](#github)
    1. [heroku](#heroku)
1. [Credits](#credits)
    1. [Content](#content)
    1. [Acknowledgements](#acks)

# <a name="summary"></a> Summary
This site is a virtual cookbook.

It provides a database of recipes which can be searched, viewed, added to, removed from and edited.

# <a name="ux"></a> UX
## <a name="Strategy"></a> Strategy
### **New site user's goals:**
* As a new site user, I want to be able to browse and search for recipes 
* As a new site user, I want to get inspiration for a recipe to make
* As a new site user, I want to be able to understand the intent of the page
* As a new site user, I want I want to understand easily how to navigate the page and access the facilities provided
### **Returning user's goals**
* As a returning site user, I want to be able to log in
* As a returning site user, I want to be able to view my recipes
* As a returning site user, I want to be able to edit and delete my recipes
* As a returning site user, I want to be able to add new recipes
### **Site owner'as goals:**
* As a site owner, I want recipes added via the site to be stored in the correct format in the database
* As a site owner, I want to be able to see who has added each recipe

## <a name="scope"></a> Scope
**Functional requirements:**
#### For ease of use:
* Navigation bar which is simple and easy to navigate
* A search Function
#### To ensure the database is up to date and editable:
* Function to add a recipe
* Function to edit a recipe
* Function to delete a recipe
* For the recipes to be only editable by the creator

**Content requirements:**
#### To ensure the site is visually appealing and to draw the user's eye:
* Images of recipes
* Clear, crisp colours which do not detract from or make the text unreadable

### For usability
* For the time commitment to be clear as this is often a factor in a recipe choice

## <a name="structure"></a> Structure
**Interaction design:**
* User friendly interface to ensure usability and to encourage the user to return
* Responsive and visible links which change on hover to provide user feedback as they navigate the site
* Ability to exit pop ups so a user is not forced to use the browser navigation tools

**Information Architecture:**
* Navigation bar at the top of the page
* Footer at the bottom of the page - sticky to the bottom so it is only visible when the bottom of the page is reached
* Responsive navigation bar - adjusting for mobile for ease of use
* Responsive images to ensure they fit within the designated spaces, no matter what device is being used or the size of the screen
* All features appropriate size and responsive for mobile and desktop viewing
* All information is appropriate and relative to the subject and not misleading or hard to find

## <a name="skeleton"></a> Skeleton
Please click the below link to view the wireframe mock up of the website in mobile, tablet and desktop sizing

[Wireframe](/workspace/recipe-nation/wireframes/recipe-website.pdf)

## <a name="surface"></a> Surface
The intention of the website is to be clean, crisp and clear

* The font family chosen is 'Lato' as this is a clear and easy to read font
* The colour scheme selected is shades of teal and white. The only variant to this is the borders for the recipes which (although the colour is actually lime) provides the feel of an invitation card with a gold border
* The colour scheme was selected as it is clean and crisp. It is reminicent of a kitchen and the background chosen includes images of tools used in a kitchen

# <a name="features"></a> Features
## <a name="existing-features"></a> Existing Features
Feature | Details
--------|--------
Log in | The user can register and log into their own account with personalised features
Log out | There is a log out functionality on the page - this is especially important for users of a shared device
Add recipe | Users can contribute to the site via the add recipe form
Edit recipe form | Users are able to edit their own recipes. An important note here is that users can only edit their own recipes
Delete a recipe | Users are abel to delete their own recipes. As above, this can only be done with the user's own recipes
Search function | The users are able to search the recipe database by ingredient and recipe name. This function is available whether a user is logged in/registered or not

## <a name="left-to"></a> Features left to implement
Feature | Details
--------|--------
Browse by recipe type | The initial design included a drop down selection in the navigation bar which directed the user to pages of recipes which are within this recipe type. Unfortunately, I ran out of time to implement this feature
Menu description and serving size | Whilst creating the site, I realised it would be useful to add these fields 
# <a name="bugs"></a> Bugs
Bug | Fix
--------|--------
Navigation drop down option | Whilst this was still part of the page which was being implemented, only the drop down within the collapsed mobile view of the navbar would work. I found that this needed to be seperated into two sections to add the contents - one for the mobile view and one for the browser view
Types in add recipe form | Although the form showed the options available from the 'types' section on the database, when a recipe was added, it gave a value of '1' for the types entry. This was resolved by adding value="{{ type.type }} to the option 
It was possible to upload any file type on the add recipe form | This would cause issues as the form would not submit. I added accept=".png, .jpg, .jpeg, .gif" to the input field

# <a name="tech"></a> Technologies Used
* Materialize - https://materializecss.com/
* JavaScript
* Google fonts - https://fonts.google.com/
* www.validator.w3.org
* http://www.css-validator.org/
* Git
* Gitpod
* GitHub
* Google Chrome
* http://www.responsinator.com/
* Chrome Dev Tools
* Python
* Flask
* Amazon AWS S3
* MongoDb
* Heroku
* Jinja
* Favicon.io
* Balsamiq

# <a name="testing"></a> Testing
### **New site user testing:**
* As a new site user, I want to be able to browse and search for recipes 
    1. Upon entering the site, users are automatically greeted with the page title and sub heading
    1. There is a clear call to action to browse the recipes
* As a new site user, I want to get inspiration for a recipe to make
    1. The images and cook/prep times within the page provide inspiration to the site user
* As a new site user, I want to be able to understand the intent of the page
    1. Upon entering the page, it is clear the site is designed around food and cooking. The carousel content and background image point the user to this
* As a new site user, I want I want to understand easily how to navigate the page and access the facilities provided
    1. The navigation bar has clear and easy to understand links. These links are also dynamic to whether the user is signed in or not so they are only seeing the relevant options
### **Returning user testing**
* As a returning site user, I want to be able to log in
    1. Upon entering the site, there is the option in the nav bar to register and log in
* As a returning site user, I want to be able to view my recipes
    1. the user's profile page provides all of the recipes the user has submitted
* As a returning site user, I want to be able to edit and delete my recipes
    1. The recipes the user has submitted all show buttons to edit and delete the recipes. This is not visible to other users
* As a returning site user, I want to be able to add new recipes
    1. The form to enter a new recipe allows the user to instantly add a recipe to the site in the required format
### **Site owner testing:**
* As a site owner, I want recipes added via the site to be stored in the correct format in the database
    1. The form to add or edit a recipe validates the content to ensure all fields are complete and are in the correct format
* As a site owner, I want to be able to see who has added each recipe
    1. When a recipe is submitted, the user's _Id is stored in the database. This shows on the site as the user's username on each recipe

### **Performance testing:**
1. Tested website responsiveness using http://www.responsinator.com/
    1. Results: The website is responsive to all device sizes without any unnecessary x-scroll. 
1. Tested the image size to ensure no image is to large and impacting the website loading times. I used the Google Dev Tools - Network
    1. Results: The site loading time is sub optimal. The total website loading time is 1.30s which can be improved
1. Tested the images on the all recipes page using Google Dev Tools - Lighthouse
    1. Results: An issue highlighted using this tool is the image formats used. Image formats like JPEG 2000, JPEG XR, and WebP often provide better compression than PNG or JPEG, which means faster downloads and less data consumption.
1. All HTML pages were tested using https://jigsaw.w3.org/css-validator/validator
    1. All but the 'base' template resulted in errors that the Lang Doctype and Title were missing. This was to be expected as the details were being extended from the base template to did not need to be added
    1. All HTML pages resulted in errors where the Jinja template language was used
    1. None of these are actual errors within the code
1. Tested the CSS using http://www.css-validator.org/
    1. No errors were found
1. Tested the website on the Google Chrome browser Version 87.0.4280.88 (Official Build) (64-bit)
    1. Results: The website was responsive and the elements performed in the way they were intended to
1. Tested the website on the Microsoft Edge browser Version Version 87.0.664.66 (Official build) (64-bit)
    1. Results: The website was responsive and the elements performed in the way they were intended to
1. Tested the website on the Firefox browser Version 82.0.3 (64-bit)
    1. Results: The website was responsive and the elements performed in the way they were intended to
1. Tested the form validation worked correctly on each of the above browsers
    1. Results: The form correctly sent when the fields were completed as they should have been and did not when the fields had not been completed

# <a name="deployment"></a> Deployment
## <a name="github"></a> Github Pages
1. Create a new repository or access an existing repository
1. Click the green Gitpod button to launch the project in Gitpod
1. Create an index.html file
1. Add the file to the staging area using the git add Functional
1. Commit the file using the git commit function, adding an appropriate commentary
1. Push the file to GitHub using the git commit and git push functions
1. Refresh your GitHub repository and click the 'Settings' tab
1. Scroll to the GitHub Pages section and select a publishing source
1. Click 'Save'
1. Click the URL created within the Settings - GitHub Pages section

**To clone the repository for local deployment:** 
1. On the main page of the repository, click the down arrow Code button
1. Click the download icon under the relevant section to clone with either HTTPS, SSH or GitHub CLI 
1. In Git Bash, change the current directory to the location you want the directory to be stored
1. Type git clone and then paste the URL you copied in step 2
    1. An example for HTTPS: `git clone https://github.com/hollyford/recipe-nation`
1. Press enter - that's it, your clone has been completed! 

**To fork the repository:**
1. Navigate to the main page of the repository you wish to fork
1. Click the Fork button on the top right hand side of the page
## <a name="heroku"></a> Heroku
### How to deploy to Heroku

To deploy the app to Heroku from its [GitHub repository](https://github.com/hollyford/recipe-nation), the following steps were taken:

1. From the GitPod terminal, create **requirements.txt** and **Procfile** using these commands:

```console
pip3 freeze --local > requirements.txt
echo web: python app.py > Procfile
```

2. **Push** these files to GitHub
3. **Log In** to [Heroku](https://id.heroku.com/login)
4. Select **Create new app** from the dropdown in the Heroku dashboard
5. Choose a unique name ('recipe-nation') for the app and the location nearest to you
6. Go to the **Deploy** tab and under **Deployment method** choose GitHub
7. In **Connect to GitHub** enter your GitHub repository details and once found, click **Connect**
8. Go to the **Settings** tab and under **Config Vars** choose **Reveal Config Vars**
9. Enter the following keys and values, which must match those in the env.py file created earlier:

|**Key**|**Value**|
|:-----|:-----|
|IP|`0.0.0.0`|
|PORT|`5000`|
|SECRET_KEY|`<app secret key>`|
|MONGO_URI|mongodb+srv://root:r00tUser@cluster0.4zi37.mongodb.net/recipe_nation?retryWrites=true&w=majority
|MONGO_DBNAME|`recipe_nation`|
|S3_BUCKET|`recipe-image-repo`|
|S3_ACCESS_KEY|`<S3 key>`|
|S3_SECRET_ACCESS_KEY|`<S3 secret key>`|

10. Go back to the **Deploy** tab and under **Automatic deploys** choose **Enable Automatic Deploys**
11. Under **Manual deploy**, select **master** and click **Deploy Branch**
12. Once the app has finished building, click **Open app** from the header row of the dashboard

# <a name="credits"></a> Credits
## <a name="content"></a> Content
All of the recipes and images added under the usernames 'holly' and 'green' were sourced from https://www.bbcgoodfood.com
https://www.bbcgoodfood.com/recipes/healthy-banana-bread
https://www.bbcgoodfood.com/recipes/slow-cooker-chicken-casserole
https://www.bbcgoodfood.com/recipes/chicken-pasta-bake
https://www.bbcgoodfood.com/recipes/satay-sweet-potato-curry
https://www.bbcgoodfood.com/recipes/cupcakes

## <a name="acks"></a> Acknowledgements
* The following site was used to enable me to successfully link my application to the AWS S3 bucket to upload the images
    * https://www.zabana.me/notes/flask-tutorial-upload-files-amazon-s3

* Ed Bradley - Ed also helped me connect to AWS S3 by allowing me to view his code on github and compare this with my own. This allowed me to locate the issues in my code and get this to work. I also used his readme as an example of how to deploy Heroku
    * https://github.com/Edb83/self-isolution

* My mentor Antonio Rodriguez who has provided me with guidance and support through the project

* My friends and family who helped to test the site and to add recipes
    * Scott Ford
    * Alison Stewart
    * Michael Cole