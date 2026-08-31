# Week 6 Day 1 — Django Setup & Project Structure

> From a clean environment to your first working Django route.

---

## Django Setup & Project Structure

Django provides a reusable framework so developers can focus on application features instead of building common web infrastructure manually.

Without a framework, developers would need to handle areas such as:

- Routing
- Request handling
- HTML rendering
- Forms
- Security
- Database access

With Django, the project starts with a structured, production-oriented foundation.

---

## Django Build Path

The slides follow this sequence:

```text
Workspace
   ↓
Virtual Environment
   ↓
Install Django
   ↓
Project
   ↓
App
   ↓
First View
```

The goal is for the browser to reach a Django URL and receive a response from a view.

---

## Virtual Environment

A virtual environment is an isolated workbench for a Python project.

Each project keeps its own packages and versions instead of relying on global Python packages.

```text
Global Python
├── Django 4.x
├── Random tools
├── Old packages
└── Risk of conflicts

Project venv
├── Its own Python environment
├── Its own Django version
└── Its own dependencies
```

This makes development, teamwork, and deployment more predictable.

---

## Create the Workspace and Virtual Environment

First create a folder for the workspace:

```bash
mkdir myproject
cd myproject
```

Create the virtual environment:

```bash
python -m venv venv
```

Activate it on macOS/Linux:

```bash
source venv/bin/activate
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

The project folder is the **workspace**, not yet the Django project.

When `(venv)` appears in the terminal, commands are running inside the isolated environment.

---

## Install Django Inside the Virtual Environment

Install Django:

```bash
pip install django
```

Check the installed Django version:

```bash
django-admin --version
```

Record the installed libraries and versions:

```bash
pip freeze > requirements.txt
```

`requirements.txt` allows another developer or machine to recreate the environment.

Later, dependencies can be installed with:

```bash
pip install -r requirements.txt
```

---

## `django-admin` vs `manage.py`

These command tools have different jobs.

### `django-admin`

Used before the Django project exists.

It can create a new project skeleton.

Example:

```bash
django-admin startproject mysite
```

### `manage.py`

Lives inside the Django project and runs project-specific commands.

Examples include:

- Running the server
- Creating apps
- Migrations
- Opening the Django shell

Example:

```bash
python manage.py runserver
```

---

## Create the Django Project

Create the project:

```bash
django-admin startproject mysite
```

Enter the project:

```bash
cd mysite
```

Django generates:

```text
mysite/
├── manage.py
└── mysite/
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    ├── wsgi.py
    └── asgi.py
```

### `manage.py`

The project's command interface for commands such as the development server, shell, and migrations.

### `settings.py`

Contains project configuration such as:

- Installed apps
- Middleware
- Templates
- Static files
- Database configuration
- Allowed hosts

### `urls.py`

The root URL router. It maps incoming browser paths toward views.

### `wsgi.py` and `asgi.py`

Entry points used when Django communicates with production web servers.

---

## `settings.py`

`settings.py` acts as the project's control panel.

Important settings shown in the slides include:

### `INSTALLED_APPS`

Controls which Django apps are activated.

### `MIDDLEWARE`

Defines processing layers around requests and responses.

### `ROOT_URLCONF`

Specifies where URL routing begins.

### `TEMPLATES`

Controls how Django finds HTML templates.

### `STATIC_URL`

Controls how CSS, JavaScript, and images are referenced.

### `BASE_DIR`

Provides the base path used to build paths relative to the project root.

---

## Project vs App

Django separates the whole website from individual feature modules.

### Project

The main container for the website.

It holds global configuration such as:

- Settings
- Root URLs
- Server entry points

Example:

```text
mysite
```

### App

A feature module inside the project.

An app can contain:

- Views
- URLs
- Templates
- Forms
- Models
- Tests

Examples:

```text
core
blog
store
```

**One Django project can contain many apps.**

---

## Create and Register the First App

Create an app called `core`:

```bash
python manage.py startapp core
```

Django generates:

```text
core/
├── admin.py
├── apps.py
├── models.py
├── tests.py
└── views.py
```

The app must then be registered in `settings.py`.

```python
INSTALLED_APPS = [
    ...
    "core",
]
```

Creating the app folder without adding it to `INSTALLED_APPS` can prevent Django from recognizing the app correctly.

---

## Your First Django View

A Django view is Python logic that receives a request and returns a response.

In `core/views.py`:

```python
from django.http import HttpResponse

def homepage(request):
    return HttpResponse(
        "Welcome to Django!"
    )
```

The basic flow is:

```text
HttpRequest
    ↓
homepage()
    ↓
HttpResponse
```

---

## Connect the View to a URL

A view does nothing for a browser request until a URL points to it.

In `mysite/urls.py`:

```python
from django.contrib import admin
from django.urls import path
from core.views import homepage

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", homepage, name="home"),
]
```

### `""`

The empty path represents the homepage:

```text
http://127.0.0.1:8000/
```

### `"admin/"`

Maps to Django's admin interface route.

### `name="home"`

Provides a reusable name for the route, which can later be referenced by templates and redirects.

---

## Run the Development Server

Start the Django development server:

```bash
python manage.py runserver
```

The development server runs at:

```text
http://127.0.0.1:8000/
```

The request flow is:

```text
Browser
   ↓
Django Server
   ↓
URLconf
   ↓
View
   ↓
Response
```

Django checks `urlpatterns` from top to bottom.

**The first matching URL pattern wins.**

---

## Complete Setup Flow

```text
Create workspace
      ↓
Create venv
      ↓
Activate venv
      ↓
Install Django
      ↓
Create requirements.txt
      ↓
Create Django project
      ↓
Create Django app
      ↓
Register app in INSTALLED_APPS
      ↓
Create view
      ↓
Map URL to view
      ↓
Run development server
      ↓
Browser receives response
```
