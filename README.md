# Shoophon

This project implements a portable shopping list app that allows the user to take note of most of the common product information and keep track of some basic calculations on the list of products like the quantity of items and balance.
Also allows the owner of a list to share it with other users already registered in the web application.
The project was implemented using Django 5.0.3

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
&nbsp;Confirm email address to activate account
&nbsp;Login in the web App
&nbsp;&nbsp;Shooping lists inventory (Create, Open)
&nbsp;&nbsp;&nbsp;Add items to the list (Create, Update, Remove)
&nbsp;&nbsp;&nbsp;Share your list with other users
&nbsp;&nbsp;&nbsp;Delete List
&nbsp;User account Management (Update, Delete)

## persistence model
