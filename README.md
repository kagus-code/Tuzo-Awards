#  Tuzo-Awards Web App

#### The application will allow a user to post a project he/she has created and get it reviewed by his/her peers, 28/05/2021

#### By **Eston Kagwima**

## Description
Tuzo-awards will allow a user to post a project with the following fields 
available Title, an image of the project's landing page, a detailed description of the project and a link to the live site.
A project can be rated based on 3 different criteria
Design,
Usability and
Content.
These criteria can be reviewed on a scale of 1-10 and the average score is taken.

This project was generated with [Django](https://docs.djangoproject.com/en/3.2/) version 3.2.3


### User stories Specification
- View posted projects and their details
- Post a project to be rated/reviewed
- Rate/ review other users' projects
- Search for projects 
- View projects overall score
- View my profile page
## Setup/Installation Requirements
- install Python3.9
- Clone this repository `https://github.com/kagus-code/Tuzo-Awards.git`
- Change directory to the project directory using  the `cd` command
- Open project on VSCode
- If you want to use virtualenv: `virtualenv ENV && source ENV/bin/activate`
####  Create the Database
    - psql
    - CREATE DATABASE <name>;
####  .env file
Create .env file and paste paste the following and fill  required fields:

    SECRET_KEY = '<Secret_key>'
    DBNAME = '<name>'
    USER = '<Username>'
    PASSWORD = '<password>'
    DEBUG = True
    DB_HOST='127.0.0.1'
    MODE='dev'
    ALLOWED_HOSTS='*'
    DISABLE_COLLECTSTATIC=1
#### Run initial Migration
    python3.9 manage.py makemigrations <name of the app>
    python3.9 manage.py migrate
#### Run the app
    python3.9 manage.py runserver
    Open terminal on localhost:8000


## Technologies Used

- Django version 3.2.3
- Python
- JavaScript
- HTML
- CSS
- Bootstrap
- Postgressql

## link to live site on heroku
https://tuzo-awards.herokuapp.com/



## Support and contact details

| Eston | ekagwima745@gmail.com |
| ----- | --------------------- |

### License

License
[MIT License](https://choosealicense.com/licenses/mit/)
Copyright (c) 2021 Eston Kagwima
