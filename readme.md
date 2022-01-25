# Moringa Interview

#### Author: [Kiptoo Rotich](https://github.com/kiptoo-rotich)

## Screenshot

### Landing page

![test](https://user-images.githubusercontent.com/48821300/150989675-9a3d8cb5-e4cf-400b-ae62-928bff821261.png)

## Description

This is an example of MVC using django framework.

## Setup and installations

- Clone Project to your machine
- Activate a virtual environment on terminal: `source virtual/bin/activate`
- Install all the requirements found in requirements file.
- On your terminal run `python3.9 manage.py runserver`
- Access the live site using the local host provided
- Create your superuser account `python manage.py createsuperuser` inside virtual environment.

## Getting started

### Prerequisites

- python3.9
- virtual environment
- pip
- postgresql

#### Clone the Repo and rename it to suit your needs.

```bash
git clone `https://github.com/kiptoo-rotich/test`
```

#### Initialize git and add the remote repository

```bash
git init
```

```bash
git remote add origin <your-repository-url>
```

#### Create and activate the virtual environment

```bash
python3.9 -m virtualenv virtual
```

```bash
source virtual/bin/activate
```

#### Setting up environment variables

Create a `.env` file and paste paste the following filling where appropriate:

```
SECRET_KEY = 'your secret key'
DEBUG=True
DB_NAME='<your database name>>'
DB_USER='<your username>'
DB_PASSWORD='<password to your database>'
DB_HOST='127.0.0.1'
MODE='dev'
ALLOWED_HOSTS='*'
DISABLE_COLLECTSTATIC=1
```

#### Install dependancies

Install dependancies that will create an environment for the app to run
`pip install -r requirements.txt`

#### Make and run migrations

```bash
python3.9 manage.py check
python3.9 manage.py makemigrations web_form
python3.9 manage.py migrate web 0001
python3.9 manage.py migrate
```

#### Run the app

```bash
python3.9 manage.py runserver
```

Open [localhost:8000](http://127.0.0.1:8000/)

## Testing the Application

`python manage.py test web_form`

## Built With

- [Python3.9](https://docs.python.org/3/)
- Django==3.2.5
- Postgresql
- Boostrap
- HTML
- CSS

### License

- LICENSED UNDER [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](license)
