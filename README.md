# Shoophon

This project implements a portable shopping list app that allows the user to take note of most of the common product information and keep track of some basic calculations on the list of products like the quantity of items and balance.
Also allows the owner of a list to share it with other users already registered in the web application.
The project was implemented using Django 5.0.3

components used in this project:
    - user login
    - email
    - persistence with sqlite
    - django (templates, forms)
    - bootstraps
    - crispy forms
    - Environment Variables
    - cloudinary
    - CSS
    - JavaScript


![Default Home](./static/images/welcome.jpg?raw=true "Welcome")

## Installation

First clone the repository from Github and switch to the new directory:

    $ git clone https://github.com/Itmanco/shopplist.git
    $ cd {{ project_name }}

Activate the virtualenv for your project.

Install project dependencies:

    $ pip install -r requirements.txt

Then simply apply the migrations:

    $ python manage.py migrate

You can now run the development server:

    $ python manage.py runserver

You should set up your .env file at the project root (next to the sqlite file). It should contain values for:
_ SECRET_KEY
_ EMAIL_HOST_USER \* EMAIL_HOST_PASSWORD

## Use

![Default Use](./static/images/use.jpg?raw=true "Use")

## Activity Diagram

![Default Persistence](./static/images/activityDiagram.jpg?raw=true "Activity Diagram")

## persistence model

![Default Persistence](./static/images/persistence.jpg?raw=true "Persistence Model")
