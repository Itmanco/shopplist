# Shoophon

This project implements a portable shopping list app that allows the user to take note of most of the common product information and keep track of some basic calculations on the list of products like the quantity of items and balance.
Also allows the owner of a list to share it with other users already registered in the web application.
The project was implemented using Django 5.0.3

The front end is implemented with Bootstrap to provide mobile support.

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

Create new user

1. Confirm email address to activate account
2. Login in the web App
   ⋅⋅1. Shooping lists inventory (Create, Open)
   ⋅⋅⋅1. Add items to the list (Create, Update, Remove)
   ⋅⋅⋅2. Share your list with other users
   ⋅⋅⋅3. Delete List
3. User account Management (Update, Delete)

## Activity Diagram

![Default Persistence](./static/images/activityDiagram.jpg?raw=true "Activity Diagram")

## persistence model

![Default Persistence](./static/images/persistence.jpg?raw=true "Persistence Model")
