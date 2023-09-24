# Tasks Manager with Rest APi
This is python based django framwork app

# This django-Rest application have the following modules

1. Useruthentication (Registraion, Login)
2. Task Module ( title,desctiption,date,priority)
3. Search option
4. Rest Frrmework APi for json formate

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Development](#development)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)


# Django Cheatsheet

## Django Commands

### Initializing Projects

#### Starting New Project

Establish Django project. [Documentation](https://docs.djangoproject.com/en/1.11/glossary/#term-project)

```console
django-admin startproject mysite
```

### Starting New Application

Projects are made of many applications. [Documentation](https://docs.djangoproject.com/en/1.11/ref/django-admin/#django-admin-migrate)

```console
python manage.py startapp [app]
```

Also need to update project ```settings.py``` file

#### Creating Admin User

```console
python manage.py createsuperuser
```

### Development

#### Running Server

```console
python manage.py runserver
```

#### Migrating Databases

When changing models, we have to update the database. Migrations help us track changes.

Might need to use db's shell to create the main database when first creating.

```console
python manage.py makemigrations [app]
python manage.py migrate
```

```console
python manage.py sqlmigrate [app] [number]
```