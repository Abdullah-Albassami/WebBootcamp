# Week 6 - Day 2

# Django Architecture & MVT

> **Note:** The first section continues the previous day's Django
> setup/routing work. The main Day 2 lesson then begins with **Django
> Architecture & MVT**.

------------------------------------------------------------------------

# CONTINUATION FROM PREVIOUS DAY

## Troubleshooting Mindset

**Do not panic. Read the error, then check the correct layer.**

  -----------------------------------------------------------------------
  Problem                             What to check
  ----------------------------------- -----------------------------------
  `django-admin not found`            Activate `venv`, then install
                                      Django again

  `ModuleNotFoundError: core`         Check app name and `INSTALLED_APPS`

  `404 page not found`                Check path spelling, `include()`,
                                      and URL order

  Port already in use                 Run
                                      `python manage.py runserver 8080`

  View does not appear                Check import path, URL mapping, and
                                      server refresh
  -----------------------------------------------------------------------

------------------------------------------------------------------------

## Guided Lab --- Multi-Page Django Starter Site

**Objective:** Create and test your first multi-page Django app.

1.  Create project `mysite`
2.  Create app `core`
3.  Register `core` in `INSTALLED_APPS`
4.  Create views: `home`, `about`, `contact`
5.  Map URLs properly
6.  Test all pages in browser
7.  Freeze dependencies
8.  Push to GitHub

**Deliverable:** working browser screenshots + GitHub repository link.

------------------------------------------------------------------------

## Challenge --- Cleaner App-Level Routing

**Goal:** Move from "it works" to a structure that scales.

### Build a `pages` app

Views: `index`, `faq`, `team`

### Use app-level `urls.py`

``` python
# project/urls.py
path("", include("pages.urls"))
```

``` python
# pages/urls.py
path("", index, name="index")
```

### Name every route

Use `name="index"` and link with:

``` html
{% url 'index' %}
```

### Stretch Goal

``` text
Browser → Project URLs → App URLs → View
```

------------------------------------------------------------------------

## You Now Have the Django Foundation

  Part          Meaning
  ------------- ---------------------------------------------
  Environment   Workspace + `venv` + dependencies
  Project       `manage.py`, `settings.py`, `urls.py`
  App           Feature module registered in settings
  View          Python function that returns a response
  URLconf       Route that connects the browser to the view

Next, the project structure becomes a clearer mental model: **MVT and
request-response**.

------------------------------------------------------------------------

# DJANGO ARCHITECTURE & MVT

**How Django thinks: from browser request to clean, rendered response.**

------------------------------------------------------------------------

## Today's Mental Model

``` text
Browser → URLconf → View → Context → Template → HTML
```

**Key idea:** Django is not random files. It is a predictable chain of
responsibility.

------------------------------------------------------------------------

## MVT vs MVC

Django uses **Model-View-Template (MVT)** rather than traditional MVC
naming.

### Traditional MVC

``` text
Model ↔ Controller ↔ View
```

The Controller receives the request, calls the model, then chooses a
view to display.

### Django MVT

``` text
Model ↔ View → Template
```

The **URL dispatcher + View** handle the request. The **Template** is
the presentation layer.

------------------------------------------------------------------------

## The Three Layers

### Model

Defines data structure and business rules. It represents database tables
as Python classes.

### View

Receives the request, prepares data, and chooses what response should be
returned.

### Template

Builds the final HTML. It displays data using variables, tags, loops,
and filters.

**Rule of thumb:**

``` text
Model = data
View = decision
Template = presentation
```

------------------------------------------------------------------------

## Full Request Flow

``` text
1. Client request
       ↓
2. WSGI / ASGI
       ↓
3. Middleware in
       ↓
4. URL resolver
       ↓
5. View executes
       ↓
6. Template renders
       ↓
7. Middleware out
       ↓
8. Response
```

**The View is only one stop in a bigger pipeline.**

------------------------------------------------------------------------

## URL Resolver --- The Traffic Controller

Django reads URL patterns **from top to bottom**. **First match wins.**

``` python
urlpatterns = [
    path("admin/", admin.site.urls),
    path("books/", book_list, name="book_list"),
    path("books/<int:id>/", book_detail, name="book_detail"),
]
```

-   **Order matters:** specific routes should not be hidden behind
    generic ones.
-   **Includes matter:** move app routes into app-level `urls.py` files.
-   **Names matter:** use `name="..."` so templates do not hardcode
    URLs.
-   **404 is useful:** a missing match helps identify where routing
    broke.

**URLconf connects the browser address to the Python view.**

------------------------------------------------------------------------

## View Layer --- Coordinator, Not HTML Factory

A clean view reads the request, prepares data, and returns a response.

``` python
def book_list(request):
    books = Book.objects.all()
    context = {"books": books}

    return render(
        request,
        "books/list.html",
        context
    )
```

``` text
Request → View logic → Response
```

**Good:** small, clear, testable.

**Avoid:** HTML strings, heavy logic, low-level SQL.

**Thin views are easier to debug and easier to grow.**

------------------------------------------------------------------------

## Template Layer --- Data Becomes UI

``` html
{% extends "base.html" %}

{% block content %}
<h1>Books</h1>

{% for book in books %}
    <p>{{ book.title }}</p>
{% empty %}
    <p>No books found.</p>
{% endfor %}

{% endblock %}
```

-   **Variables:** `{{ book.title }}` displays context data.
-   **Tags:** `{% for %}` and `{% if %}` control simple presentation.
-   **Inheritance:** `base.html` avoids repeated layout.
-   **Escaping:** Django protects output by default.

**Templates should present data, not make business decisions.**

------------------------------------------------------------------------

## Model Layer --- Preview Only

``` python
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    year = models.IntegerField()
```

``` text
Model class → Database table
```

  Field      Meaning
  ---------- -------------------
  `title`    short text column
  `author`   short text column
  `year`     number column

For Unit 4, in-memory data is fine. The goal is the Django flow.

------------------------------------------------------------------------

## Context --- The Bridge

Context is the dictionary that carries data from Python to HTML.

``` python
context = {
    "title": "Library",
    "books": books,
    "count": len(books),
}

return render(request, "books/list.html", context)
```

Template:

``` html
<h1>{{ title }}</h1>
<p>Total: {{ count }}</p>

{% for book in books %}
    <p>{{ book.title }}</p>
{% endfor %}
```

``` text
Python / View → Context → Template
```

**When the template "knows" something, the view usually passed it in
context.**
