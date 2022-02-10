# Animal_Adoption_Dating_App

## Overview
This project is a web-based "dating" app that matches shelter animals up with prospective owners. You are able to browse, view, search and adopt the pet you like.

## Getting Started
### 1. Git: Clone the project in a local directory

```
$ git clone https://github.com/li-xiaoying/Animal_Adoption_Dating_App.git
```
You should see whatever was in the folder before and a new folder with the same name as your repo.

### 2. Python Virtual Environment(Optional but Recommended)

Fire up your terminal, navigate to the root of your project folder:
```bash
# On your machine:
pip3 install virtualenv
```

We then want to run the command
```bash
# Linux and Mac
python3 -m venv ./venv

# Windows Command Prompt
python -m venv venv
```

This will create a virtual environment in your project root. It will be in the folder `venv` located in the project root. I *strongly* recommend adding `/venv` to your `.gitignore` file. This will save a lot of headaches down the road. 

To activate the virtual environment (and we need to do this everytime we close out of the terminal or log off the computer):

```bash
# Linux and Mac
source ./venv/bin/activate

# Windows Command Prompt
/venv/Scripts/activate.bat
```

If you want to verify if your virtual environment is currently active

```bash
# Linux and Mac
which python3
# <path_to_your_repo_folder>/venv/bin/python3

# Windows Command Prompt
where python
```

If you ever want to leave the virtual environment, that is easier yet

```bash
deactivate
```

Always remember to have your virtual environment running when working on your project.

### 3. Install Flask

In your terminal, make sure your virtual environment is active if you have one, and run the following command

```bash
pip3 install Flask-MySQL
```

You'll see a bunch of text fly across the screen. Let's confirm the install went OK by typing

```bash
flask --version
```

### 4. Project Directory Structure

```
.
├── .gitignore 
├── README.md
├── app.py  
├── wsgi.py 
├── venv               <= Should be in your .gitignore
├── pets/
│    ├ cats.py
│    ├ dogs.py           <= APIs for different type of pets
│    ├ others.py             
├── templates/
│    ├ landing_page.j2
│    ├ login_page.j2
│    ├ ...             <= All the other html pages
│    ├ ...
│    └ layouts/
│       └ main.j2
│
└── static/           
     ├ css
     ├ js
     └ img
```

### 5. Starting `app.py`

Finally, we can start running our web app.

Hop on over to the terminal:

```bash
python3 app.py
```

Then enter the web address, you should be able to see the landing page at: http://localhost:1234/
