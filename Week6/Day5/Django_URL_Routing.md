# Week 6 - Day 5
# Django URL Routing

## TOPIC 1 — SIMPLE PATHS VS DYNAMIC PATHS

Static pages have fixed URLs. Detail pages usually need variables.

### Simple path

```text
about/ → one fixed page
```

```python
path("about/", views.about, name="about")
```

### Dynamic path

```text
product/<int:id>/ → many product pages
```

```python
path(
    "product/<int:id>/",
    views.product_detail,
    name="product_detail"
)

# /product/4/ → id = 4
```

### Path parameter

A value extracted from the URL path.

### View argument

Django passes it into the view function.

**Dynamic URLs are how one view can serve many related pages.**

---

## TOPIC 2 — BUILT-IN PATH CONVERTERS

Converters tell Django what type of URL segment is allowed.

### `<int:x>`

```text
positive integer
/product/12/
```

### `<str:x>`

```text
text without slash
/user/aly/
```

### `<slug:x>`

```text
URL-friendly text
/blog/my-post/
```

### `<uuid:x>`

```text
UUID value
/order/550e.../
```

### `<path:x>`

```text
text with slashes
/files/a/b/
```

**Pick the narrowest converter that matches your need. Do not use `<path:x>` unless you really need it.**

---

## TOPIC 3 — PASSING PARAMETERS TO VIEWS

The converter extracts the value and Django sends it into the view.

### `urls.py`

```python
path(
    "product/<int:id>/",
    views.product_detail,
    name="product_detail"
)
```

### `views.py`

```python
def product_detail(request, id):
    # id is now a Python integer

    return render(request, "product.html")
```

Flow:

```text
/product/4/
     ↓
   id = 4
     ↓
product_detail(request, id)
```

**The parameter name in the URL must match the view argument name.**

**The URL is not just navigation. It can carry data into the backend.**

---

## TOPIC 4 — URL NAMES & REVERSE RESOLUTION

Never hardcode links when Django can build them for you.

### Hardcoded URL

```html
<a href="/products/">Products</a>
```

Breaks when paths change.

### Named URL

```python
path("products/", view, name="product_list")
```

Stable reference.

### Template link

```html
{% url 'product_list' %}
```

Django builds the real path.

### In views

```python
from django.urls import reverse

return redirect(reverse("home"))
```

### In templates

```html
<a href="{% url 'home' %}">Home</a>
```

**Names allow you to refactor route paths without hunting through every template.**

---

## TOPIC 5 — NAMESPACES AVOID ROUTE-NAME COLLISIONS

Different apps can have the same route name without confusing Django.

### `blog.urls`

```python
app_name = "blog"
name = "index"
```

### `shop.urls`

```python
app_name = "shop"
name = "index"
```

### Template

```html
{% url 'blog:index' %}
{% url 'shop:index' %}
```

```text
blog:index → blog app

shop:index → shop app
```

**Namespacing is mandatory once the project has more than one app.**

---

## TOPIC 6 — DEBUGGING ROUTING ISSUES

Start from the URL, then check the map.

### 404

```text
App not included, typo, wrong converter, or route order.
```

### NoReverseMatch

```text
Missing name=, wrong namespace, or wrong arguments.
```

### Wrong view

```text
A generic route appears before a specific route.
```

### Template url error

Use quotes:

```html
{% url 'home' %}
```

### `resolve()`

Ask Django which view a path resolves to.

```python
from django.urls import resolve

resolve("/products/15/")
```

**Troubleshooting question: did Django find the route you think it found?**

---

## TOPIC 7 — ROUTING ANTI-PATTERNS

These problems make projects painful to maintain.

### Everything in root `urls.py`

```text
Root file becomes impossible to read.
```

### Hardcoded links

```text
Refactors break templates silently.
```

### Using `<path:x>` too early

```text
It captures too much route space.
```

### Duplicate route names

```text
Reverse resolution becomes confusing.
```

### Inconsistent slashes

```text
Some URLs feel broken or unpredictable.
```

**Clean routing is about separation: root distributes, apps define, templates reverse.**

---

# GUIDED LAB — FULLY MODULAR ROUTING SYSTEM

**Objective:** students build a clean URL tree with app-level routing.

### 01 — Create pages app

### 02 — Add home/about/contact

### 03 — Create blog app

### 04 — Add list/detail/category routes

### 05 — Use namespaces

### 06 — Use dynamic parameters

### 07 — Add custom 404 page

### 08 — Use `{% url %}` in templates

### Deliverables

```text
screenshots of working routes + URL tree diagram
```

---

# CHALLENGE — STARTUP PLATFORM URL ARCHITECTURE

Students design a scalable URL system before they code it.

### users

```text
login / profile
```

### courses

```text
list / detail / category
```

### payments

```text
checkout / receipt
```

### dashboard

```text
home / reports
```

### Must include

```text
app-level urls.py + include()
everywhere
```

### Must include

```text
namespaces + at least one dynamic
route
```

### Bonus include

```text
one CBV route using .as_view()
```

Example:

```python
path("courses/<slug:slug>/", views.course_detail, name="detail")
```
