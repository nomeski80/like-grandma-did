
# Like Grandma 

Welcome to Like Grndama Did, a website designed to treasure thoses delicious memories and special family traditions that we have passed down through generations. The idea is we can she some new ones to pass on in the future too!

The site has been built with Django, JavaScript, HTML and CSS styling to enable to user to have full CRUD funcuanility of the site. The site is targetd towards users who have a nostalic love of food and treasure the memories and monets share with the loved ones in their family.

# add screenshot of home page here

# view the live website here...

# Table of Contents

User Experience Design (UX)
The Strategy Plane
Site Goals
Epics
User Stories
The Scope Plane
The Structure Plane
Opportunities

Wireframes
Database Schema
The Surface Plane
Features
Future Enhancements
Technologies Used
Testing
Deployment
Credits

# User Experience Design (UX)

The idea behind Like Grandma Did is to be a community site for users to share and create their family recipes with others, enabling them to keep traditions alive and to pass on the love of food and cooking together. Users will also be able to explore recipes written by other users from around the world. The graphical elements and overall design of the site provide the user with a simple and easy to navigae environment.
# The Sites Ideal User
Food lover looking to share their favourite recipes with others
Someone looking to expand their recipe knowledge
Someone looking for inspiration for new things to try
Someone looking build their cooking social media following
Site Goals
To provide users with a place to find recipes
To provide users with a place to share their own recipes
To provide users with a place to discover new meals





# The Strategy Plane
# Site Goals
# Milestones - 

11 milestones were created to plan out the project and they were devided in to the User stories with the labels must have, should have and might have. These can be viewed here on the kanban board.
- Create an app with Django and deploy on Heroku
- Plan and design site Features
- testing of the app
- write up the ReadMe file
- Create an About Grandma page
- Create a user sign in form with authentication
- Create forms for users to comment on recipes
- Create forms for users to add their own recipes
- search functionan
- add content to populate the site
- add funcuanility for user to save and download a recipe

# User Stories
# The Scope Plane
# The Structure Plane
# Opportunities
# Wireframes 
add screenshots here
# Database Schema
add screenshots of Lucid here
# The Surface Plane

Features - functional overview, nav bar, footer Menus in navbar 
Icons for times/ difficulty, Search box, Options to save/ download / print recipes, Rate / comment, Show more / show less, Reactive Defensive

Future Enhancements
Technologies Used
Testing - mannual testing, quality assurance, addressing potentual issues
# Deployment -
To deploying my Django App on Heroku I followed these steps:
I set up a Heroku account and signed in. I commited my projet in GitPod and pushed my code so far. I installed Python and Pip, the Django project was ready for deployment. Installed packages

From the main Heroku Dashboard page select 'New' and then 'Create New App'
Give the project a name - I entered like-grandma-did and select a suitable region, as I'm in the UK I selected Eurpoe, then select create app. 
This will create the app within Heroku and bring you to the deploy tab. From the submenu at the top, navigate to the resources tab.
Add the database to the app, in the add-ons section search for 'Heroku Postgres', select the package that appears and add 'Heroku Postgres' as the database
Navigate to the setting tab, within the config vars section copy the DATABASE_URL to the clipboard for use in the Django configuration.
Within the django app repository create a new file called env.py - within this file import the os library and set the environment variable for the DATABASE_URL pasting in the address copied from Heroku. The line should appear as os.environ["DATABASE_URL"]= "Paste the link in here"
Add a secret key to the app using os.environ["SECRET_KEY"] = "your secret key goes here"
Add the secret key just created to the Heroku Config Vars as SECRET_KEY for the KEY value and the secret key value you created as the VALUE
In the settings.py file within the django app, import Path from pathlib, import os and import dj_database_url
insert the line if os.path.isfile("env.py"): import env
remove the insecure secret key that django has in the settings file by default and replace it with SECRET_KEY = os.environ.get('SECRET_KEY')
replace the databases section with DATABASES = { 'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))} ensure the correct indentation for python is used.

In the terminal migrate the models over to the new database connection
Navigate in a browser to cloudinary, log in, or create an account and log in.
From the dashboard - copy the CLOUDINARY_URL to the clipboard
in the env.py file created earlier - add os.environ["CLOUDINARY_URL"] = "paste in the Url copied to the clipboard here"



In Heroku, add the CLOUDINARY_URL and value copied to the clipboard to the config vars
Also add the KEY - DISABLE_COLLECTSTATIC with the Value - 1 to the config vars
this key value pair must be removed prior to final deployment
Add the cloudinary libraries to the list of installed apps, the order they are inserted is important, 'cloudinary_storage' goes above 'django.contrib.staitcfiles' and 'cloudinary' goes below it.
in the Settings.py file - add the STATIC files settings - the url, storage path, directory path, root path, media url and default file storage path.
Link the file to the templates directory in Heroku TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')
Change the templates directory to TEMPLATES_DIR - 'DIRS': [TEMPLATES_DIR]
Add Heroku to the ALLOWED_HOSTS list the format will be the app name given in Heroku when creating the app followed by .herokuapp.com
In your code editor, create three new top level folders, media, static, templates
Create a new file on the top level directory - Procfile
Within the Procfile add the code - web: guincorn PROJECT_NAME.wsgi
In the terminal, add the changed files, commit and push to GitHub

In Heroku, navigate to the deployment tab and deploy the branch manually - watch the build logs for any errors.
Heroku will now build the app for you. Once it has completed the build process you will see a 'Your App Was Successfully Deployed' message and a link to the app to visit the live site.
speeds up the deployment process, ensures that the project is correctly set up and functipnal in a live environment
ready for actual use

# Forking





Credits - which tutorials did I use, graphics, photos, text content, any other resorces









