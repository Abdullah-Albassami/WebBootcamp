# Week 6 - Day 3
# Django Architecture & Routing

## TOPIC 1 — CONTEXT: THE BRIDGE

Context is the dictionary that carries data from Python to HTML.

```python
context = {
    "title": "Library",
    "books": books,
    "count": len(books),
}

return render(request, "books/list.html", context)
```

The template can then use the values passed through context:

```html
<h1>{{ title }}</h1>
<p>Total: {{ count }}</p>

{% for book in books %}
    <p>{{ book.title }}</p>
{% endfor %}
```

**Key idea:** When the template “knows” something, the view usually passed it in context.

---

## TOPIC 2 — MIDDLEWARE: LAYERS AROUND THE REQUEST

Middleware can inspect or modify the request before the view and the response after it.

```text
Browser
   ↓
Security      → headers
   ↓
Session       → load state
   ↓
Auth          → user info
   ↓
CSRF          → protect POST
   ↓
View
```

**Request:** top → bottom  
**Response:** bottom → top

---

## TOPIC 3 — TEMPLATE INHERITANCE

Template inheritance ties the UI together.

One base layout keeps every page consistent.

```text
                 base.html
                /    |     \
               /     |      \
       home.html  books/list.html  contact.html
```

### Base template
Contains shared elements such as:
- navigation
- footer
- CSS links
- content block

### Child templates
Contain:
- page title
- page-specific content

**Key idea:** Avoid copy-paste HTML. Extend the base template and override blocks.

---

## TOPIC 4 — COMPLETE MVT EXAMPLE

A simple books page connects the MVT concepts together.

```text
Model
Book(title, author, year)
        ↓
View
book_list gets books
and sends context
        ↓
URL
path("books/", book_list)
        ↓
Template
loops over books in HTML
```

Complete request flow:

```text
Browser requests /books/
        ↓
URLconf matches book_list
        ↓
View prepares { books }
        ↓
Template renders list
        ↓
Browser displays HTML
```

This is the MVT pattern repeated throughout Django applications.

---

## TOPIC 5 — COMMON ARCHITECTURE MISTAKES

| Mistake | Better approach |
| --- | --- |
| Huge views | Move heavy decisions to helper functions or models later |
| HTML in Python | Use `render()` and templates instead of long `HttpResponse` strings |
| Unnamed URLs | Give every route a name and use `{% url %}` |
| Copy-paste templates | Use `base.html`, blocks, and includes |
| Wrong folder paths | Respect `app/templates/app/page.html` structure |
| Circular imports | Keep apps clean and import only what you need |

**Key idea:** The fix is usually separation: each layer does its own job.

---

## TOPIC 6 — DEBUGGING ARCHITECTURE ISSUES

Read the error, then locate the broken layer.

| Error | Check |
| --- | --- |
| `404` | URL pattern not matching, wrong include, or wrong parameter type |
| `TemplateDoesNotExist` | Template folder/name is wrong or app is not installed |
| `ImportError` | Wrong import path, circular import, or typo in module name |
| `NoReverseMatch` | URL name or required parameter is missing |
| Context missing | View did not pass the variable the template expects |
| Middleware/session issue | Check settings and installed apps |

Debugging flow:

```text
URL → View → Context → Template → Response
```

---

# GUIDED LAB — BUILD A COMPLETE MVT WORKFLOW

**Objective:** Connect URL, view, context, and template in one working feature.

1. Create `library` app.
2. Add app-level `urls.py`.
3. Create an in-memory books list.
4. Create list view.
5. Create detail view with `<int:id>`.
6. Create base + child templates.
7. Add navigation menu.
8. Draw the MVT flow in `README`.

Example in-memory data shown in the lab:

```python
books = [
    {
        "id": 1,
        "title": "Welcome to Django",
        "author": "Abdullah Albassami",
        "year": 2026,
    },
    {
        "id": 2,
        "title": "FastAPI demystified",
        "author": "Taif Alosaimi",
        "year": 2026,
    },
]
```

### Deliverable

Working pages + screenshots showing:

```text
Browser → URL → View → Template
```

---

# CHALLENGE — MOVIE CATALOG MVT SYSTEM

Move from “follow me” to independent architecture decisions.

### App
`movies` app with its own `urls.py`.

### Data
Movie:
- title
- year
- rating

Store the data as an in-memory list.

### Pages
- list page
- detail page

### Routing
Use:
- URL names
- dynamic parameter

### Templates
Inherit from `base.html`.

### README
Explain the MVT flow.

Expected routes:

```text
/movies/    → list all movies
/movies/3/  → show one movie
```

---

## TOPIC 7 — DJANGO ARCHITECTURE SUMMARY

At this point:

### MVT
Model, View, and Template each have a clear responsibility.

### Request flow
The browser request moves through middleware, URLconf, view, and template.

### URL resolver
Routes are checked top to bottom. The first match wins. Named routes prevent broken links.

### Context
Context is the data bridge between Python and HTML.

### Clean structure
Use:
- thin views
- clean templates
- app-level `urls.py`

**Foundation:** architecture first, implementation second.

---

## TOPIC 8 — TODAY'S ROUTING MENTAL MODEL

URLs are not just text; they are the road system of the application.

```text
Browser → URLconf → Pattern match → View → Response
```

**Key idea:** Routing is the map between a requested path and the Python function/class that responds.

---

## TOPIC 9 — URL DISPATCH FLOW

The request enters Django, then `urlpatterns` decides which view runs.

```text
Request
   ↓
ROOT_URLCONF
   ↓
urlpatterns[]
   ↓
first match
   ↓
View → Response
```

### `ROOT_URLCONF`
Setting that points Django to the root URL file.

### `urlpatterns`
The ordered list of route patterns.

### Resolver
The Django engine that checks patterns from top to bottom.

### View
The Python logic triggered by the matching route.

**Key idea:** Django does not search randomly. It follows one ordered routing table.

---

## TOPIC 10 — ROUTING VOCABULARY

### URLconf
Django URL configuration module.

### Path
A route definition inside `urlpatterns`.

### Converter
Validates and converts dynamic parts.

### `include()`
Loads another app's routes.

### Namespace
Prevents name conflicts between apps.

### Reverse
Builds a URL from its route name.

**Route means:**

```text
URL pattern + connected view + optional name
```

---

## TOPIC 11 — PROJECT-LEVEL VS APP-LEVEL URL FILES

Large Django projects stay clean by splitting routing responsibility.

### `project/urls.py`

The global router contains:
- admin route
- routes to apps using `include()`
- global error handlers
- static/media during DEBUG

### `core/urls.py`

Contains app-specific routing:
- feature-specific pages
- names for templates
- dynamic parameters
- app namespace
- local routing rules

### Rule

The root URL file should be a **traffic distributor**, not a storage room for every route.

**Key idea:** Do not let `project/urls.py` become a giant file. Send traffic to the correct app.

---

## TOPIC 12 — BASIC APP-LEVEL ROUTING

Start with three pages and route names.

```python
# core/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
]
```

### Empty path

```python
""
```

Means the app landing page.

### Trailing slash

Use `/` consistently.

### `name=`

Provides a stable reference for links.

### `views.home`

The function/class that runs.

**Key idea:** A URL pattern is useless unless it points to a view.

---

## TOPIC 13 — `include()`: MODULAR ROUTING

The project router delegates to app routers.

```text
                     core.urls → home/about
                    /
project/urls.py → blog.urls → posts/detail
                    \
                     shop.urls → products/cart
```

Example:

```python
urlpatterns = [
    path("", include("core.urls")),
    path("blog/", include("blog.urls")),
    path("shop/", include("shop.urls")),
]
```

**Key idea:** `include()` keeps each app responsible for its own roads.

---

## TOPIC 14 — HOW MATCHING WORKS: ORDER MATTERS

Django checks patterns from top to bottom.

**First match wins.**

```python
urlpatterns = [
    path("product/create/", create_view),
    path("product/<str:id>/", detail_view),
]
```

Request:

```text
/product/create/ → create_view
```

### Specific first
Put fixed paths before generic dynamic paths.

### Generic later
`<str:id>` can capture more than you expect.

### No longest wins
Django does **not** choose the longest route.

### No match
If no pattern matches, Django returns **404**.

**Key idea:** Route ordering is one of the most common sources of beginner routing bugs.
