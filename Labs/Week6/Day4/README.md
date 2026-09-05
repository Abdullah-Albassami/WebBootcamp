# Django URL Collision Homework

## Overview

This homework demonstrates how Django handles URL patterns when more than one route can match the same URL.

Django checks URL patterns from top to bottom and uses the first matching pattern.

---

## Original URL Patterns

```python
from django.urls import path
from . import views

urlpatterns = [
    path("products/create/", views.create_view, name="create"),
    path("products/<str:id>/", views.details_view, name="details"),
]
```

The views used for testing are:

```python
from django.http import HttpResponse


def create_view(request):
    return HttpResponse("CREATE VIEW")


def details_view(request, id):
    return HttpResponse(f"DETAIL VIEW - Product ID: {id}")
```

---

## Question 1

### What happens when I try to access a product whose ID is `"create"`?

If I visit:

```text
/products/create/
```

both patterns could match the URL:

```python
path("products/create/", views.create_view, name="create")
```

and:

```python
path("products/<str:id>/", views.details_view, name="details")
```

This is because `"create"` is also a valid string for `<str:id>`.

However, Django checks URL patterns from top to bottom and stops at the first match.

Therefore:

```text
/products/create/
```

runs:

```python
create_view
```

and displays:

```text
CREATE VIEW
```

The `details_view` is not reached.

---

## Question 2

### How do I view a product whose ID is `"create"`?

The URL structure can be changed so the create page and product detail page have different patterns.

```python
from django.urls import path
from . import views

urlpatterns = [
    path("products/create/", views.create_view, name="create"),
    path("products/id/<str:id>/", views.details_view, name="details"),
]
```

Now the create page can be accessed with:

```text
/products/create/
```

which displays:

```text
CREATE VIEW
```

A product whose ID is `"create"` can be accessed with:

```text
/products/id/create/
```

which displays:

```text
DETAIL VIEW - Product ID: create
```

---

## Before and After

### Before

```text
/products/create/
```

could match both the fixed `"create/"` route and the dynamic `<str:id>/` route.

Django selects the first matching route, so `create_view` runs.

### After

The two URLs now have different structures:

```text
/products/create/      → create_view
/products/id/create/   → details_view with id = "create"
```

This removes the URL collision.

---

## Key Takeaway

Django checks URL patterns from top to bottom.

**The first matching URL pattern wins.**

Specific routes should generally be placed before more generic dynamic routes, and URL structures should be designed to avoid ambiguity.