# Week 7 Day 2 — Django Templates

## 1. Template Mental Model

A Django template is not just HTML; it is HTML prepared by Django.

Flow:

```text
Browser → View → Context → Template Engine → HTML → Browser
```

- **View**: prepares data and chooses a template.
- **Context**: dictionary passed from Python to the template.
- **Template**: reusable HTML with variables and tags.
- **Response**: final HTML returned to the browser.

Main idea:

```text
View prepares → Template presents
```

---

## 2. Templates in Django MVT

Views handle backend logic and templates handle presentation.

### Example View

```python
def home(request):
    context = {
        "title": "Home",
        "courses": courses,
    }

    return render(
        request,
        "core/home.html",
        context
    )
```

### Example Template

```html
<h1>{{ title }}</h1>

{% for course in courses %}
    <p>{{ course.name }}</p>
{% empty %}
    <p>No courses yet.</p>
{% endfor %}
```

Keep the boundary clear:

```text
Python prepares data.
HTML presents data.
```

---

## 3. Where Templates Live

### App-Level Templates

Used when templates belong to one specific app.

```text
core/
└── templates/
    └── core/
        ├── home.html
        ├── about.html
        └── contact.html
```

Typical reference:

```python
return render(request, "core/home.html")
```

### Project-Level Templates

Useful for shared layouts and reusable components.

```text
project/
└── templates/
    ├── base.html
    ├── shared/
    │   ├── navbar.html
    │   └── footer.html
    └── core/
        └── home.html
```

The important part is consistency so Django knows where to find templates.

---

## 4. Rendering Templates from Views

`render()` combines:

```text
request + template + context
```

Example:

```python
from django.shortcuts import render

def dashboard(request):
    stats = {
        "students": 28,
        "labs_done": 6,
    }

    return render(
        request,
        "core/dashboard.html",
        stats
    )
```

Template:

```html
<h1>Dashboard</h1>

<p>Students: {{ students }}</p>
<p>Labs completed: {{ labs_done }}</p>
```

Flow:

1. View runs.
2. Django loads the template.
3. Context variables become available.
4. Final HTML is returned to the browser.

`render()` is the normal way to return HTML pages in Django.

---

## 5. Template Variables

Template variables are placeholders that Django replaces with real data.

### View

```python
context = {
    "username": "Aly",
    "age": 25,
    "course": "Django",
}

return render(request, "home.html", context)
```

### Template

```html
<h1>Hello {{ username }}</h1>
<p>Age: {{ age }}</p>
<p>Course: {{ course }}</p>
```

Output:

```text
Hello Aly
Age: 25
Course: Django
```

### Syntax

```django
{{ variable }}
```

Template variables are for displaying values.

Avoid putting business logic inside templates.

---

## 6. Dot Notation

Django templates use dot notation to access data.

Examples:

```django
{{ user.email }}
{{ book.author.name }}
{{ products.0.name }}
{{ course.lessons }}
```

Django can resolve dots through:

```text
Dictionary key
→ Object attribute
→ Object method
→ List index
```

Examples:

```python
product["price"]
product.price
product.get_price
products[0]
```

Inside a template, these are accessed using dots rather than normal Python syntax.

Django does not allow templates to execute arbitrary Python code.

---

## 7. Template Filters

Filters transform values for display.

Syntax:

```django
{{ variable|filter }}
```

Examples:

```django
{{ name|upper }}
{{ title|lower }}
{{ title|title }}
{{ article|truncatewords:20 }}
{{ price|floatformat:2 }}
```

Common filters:

- `upper` → converts text to uppercase.
- `lower` → converts text to lowercase.
- `title` → converts text to title case.
- `date` → formats dates and times.
- `truncatewords` → shortens long text.
- `default` → provides a fallback value.
- `floatformat` → formats decimal values.

Filters are display transformations, not validation or business rules.

---

## 8. Template Tags

Template tags control simple presentation logic.

Syntax:

```django
{% tag %}
```

### Condition

```django
{% if user.is_authenticated %}
    Welcome back
{% else %}
    Please log in
{% endif %}
```

### Loop and Empty State

```django
{% for item in items %}
    {{ item }}
{% empty %}
    No items found
{% endfor %}
```

### Comment

```django
{% comment %}
    Hidden note
{% endcomment %}
```

### With

```django
{% with total=10 %}
    {{ total }}
{% endwith %}
```

Tags allow light UI logic, not full business logic.

---

## 9. Template Inheritance

Template inheritance allows many pages to share one base layout.

### `base.html`

```html
<!DOCTYPE html>
<html>
<head>
    <title>
        {% block title %}
            Site
        {% endblock %}
    </title>
</head>

<body>

    {% block content %}
    {% endblock %}

</body>
</html>
```

### `home.html`

```django
{% extends "base.html" %}

{% block title %}
    Home
{% endblock %}

{% block content %}
    <h1>Welcome</h1>
{% endblock %}
```

Inheritance reduces duplication and keeps the site consistent.

---

## 10. Blocks and `block.super`

Blocks are named slots in a parent template that child templates can replace or extend.

Common blocks:

```text
title
styles
header
content
sidebar
scripts
```

Example:

```django
{% block page_title %}
    {{ block.super }} - Dashboard
{% endblock %}
```

Use:

```django
{{ block.super }}
```

when the child template should keep the parent block content and add to it instead of replacing it completely.

---

## 11. Reusable Components with `include`

Use `{% include %}` for small reusable UI pieces.

Examples:

```django
{% include "shared/navbar.html" %}
{% include "components/card.html" %}
{% include "shared/footer.html" %}
```

Good uses:

- Navbar
- Footer
- Cards
- Pagination
- Small repeated visual components

Avoid extremely deep or complicated nested includes.

Difference:

```text
Inheritance → controls page structure.
Includes    → reuse smaller page parts.
```

---

## 12. `url` and `static` Template Tags

Avoid hardcoding paths when Django can generate them.

### Hardcoded Link

```html
<a href="/products/">Products</a>
```

Problem: it may break if the URL changes.

### Dynamic URL

```django
{% url "products:list" %}
```

Inside an anchor:

```html
<a href="{% url 'blog:detail' post.slug %}">
    Read more
</a>
```

Using named URLs makes routing safer.

---

## 13. Static Files

Load static support first:

```django
{% load static %}
```

CSS example:

```html
<link
    rel="stylesheet"
    href="{% static 'css/main.css' %}"
>
```

Image example:

```html
<img
    src="{% static 'images/logo.png' %}"
    alt="Logo"
>
```

Use `{% static %}` for assets such as:

- CSS
- JavaScript
- Images

---

## 14. Escaping and Safe Output

Django automatically escapes unsafe HTML by default.

Example value:

```html
<script>alert('Hi')</script>
```

If displayed normally:

```django
{{ comment }}
```

Django displays it as text instead of executing it.

This helps prevent XSS attacks.

### `safe` Filter

```django
{{ html_content|safe }}
```

Use `safe` only for content you completely trust.

Never mark user-generated content as safe because it can create an XSS vulnerability.

---

## 15. Professional Template Organization

Example structure:

```text
templates/
├── base.html
│
├── shared/
│   ├── navbar.html
│   └── footer.html
│
├── components/
│   ├── card.html
│   └── pagination.html
│
├── core/
│   └── home.html
│
├── blog/
│   ├── list.html
│   └── detail.html
│
└── dashboard/
    └── index.html
```

Recommended approach:

- Keep common layout in `base.html`.
- Put repeated shared UI in `shared/` or `components/`.
- Group page templates by feature or app.
- Avoid business logic in templates.
- Avoid hardcoded URLs.
- Avoid database access from templates.

Good structure reduces confusion as a project grows.

---

# Guided Lab — Dynamic Multi-Page UI

## Objective

Build a reusable template structure for a small Django website.

### Requirements

1. Create `base.html` with:
   - Navbar
   - Footer
   - Blocks

2. Create three pages that extend the base template.

3. Pass context from views into templates.

4. Use:
   - Loops
   - `if` conditions
   - Filters
   - Empty states

5. Add static CSS and link it with:

```django
{% static %}
```

6. Create at least one reusable include component such as:
   - Card
   - Navbar

7. Use:

```django
{% url %}
```

for all navigation links.

8. Submit screenshots of all working pages.

### Deliverables

- Working routes
- Templates
- Screenshots
- Short explanation of template inheritance

---

# Lab Version Shown in Class

## 1. Base Template

Create `base.html` with:

- Navbar
- Footer
- `{% block title %}`
- `{% block content %}`
- `{% load static %}`

---

## 2. Pages

Create:

```text
home.html
courses.html
course_detail.html
```

All pages should extend `base.html`.

---

## 3. Context Data

Pass context containing:

- Username
- List of courses

Each course should contain:

- Name
- Level
- Student count
- Description
- Image filename

---

## 4. Template Features

Use:

```django
{% for %}
{% if %}
{% empty %}
```

Filters:

```django
|title
|truncatewords
|safe
```

Use `safe` only with one trusted course description.

---

## 5. Reusable Course Card

Create:

```text
course_card.html
```

Use it to display each course.

Display a different message when a course has zero students.

---

## 6. Course Detail Links

Link each course card to its detail page using:

```django
{% url %}
```

Pass the course identifier in the URL.

---

## 7. Static Files

Add static CSS and course images using:

```django
{% static %}
```

Organize them into separate folders such as:

```text
static/
├── css/
└── images/
```

---

# Key Takeaways

```text
View        → prepares data
Context     → carries data
Template    → presents data
Variable    → {{ value }}
Tag         → {% logic %}
Filter      → {{ value|filter }}
Inheritance → {% extends %}
Block       → {% block %}
Include     → {% include %}
URL         → {% url %}
Static      → {% static %}
```

The main rule:

```text
Keep Python responsible for application logic.
Keep templates responsible for presentation.
```
