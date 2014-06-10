Base Template Sample App
===
This application is inteaded to be a base template for creating a new django
application at Mercy Corps

Install
===
After checking out the base template from git, rename the folders and configs
to match the name of your app (replace everything with djangotemplate with your
apps name) Rename the djangotemplate/settings/example-local.py to local.py and
update with your db and app configuration settings.

Ensure the server you are running on has all the required pip packages.
server_requirements.txt

Virtual Environemnt
===
Create a virtual environment on each server your app will run on and install
app specific libraries in the venv

Instructions
====
Create Virtualenv
virtualenv venv  (USES SERVER INSTALLED PACKAGES)

virtualenv —no-site-packages venv
*use no site packages to prevent virtualenv from seeing your global packages

. venv/bin/activate
*allows us to just use pip from command line by adding to the path rather then full path


Activate Virtualenv
source venv/bin/activate
workon venv
OR (if using wrapper)
mkvirtualenv venv1
workon venv

Create App Specifc Library List
===
pip freeze > app_requirements.txt
* creates a app_requirements.txt file for future installs

Updating or installing on a new server
pip install -r requirements.txt
