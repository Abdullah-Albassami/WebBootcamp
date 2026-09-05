# Django Multi-App Challenge

A Django project demonstrating multi-app URL routing, namespaces, templates, dynamic routes, and a Class-Based View.

## Apps

- `dashboard`
- `users`
- `payments`
- `courses`

## Features

- App-specific URL configurations
- URL namespaces using `app_name`
- Shared `base.html` template
- Template inheritance
- Dashboard as the root `/`
- Dynamic course route using `<slug:slug>`
- Course data passed from views to templates

## Bonus — Class-Based View

The dashboard home page uses Django's `TemplateView` instead of a Function-Based View.

```python
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = "dashboard.html"
```

The CBV is connected in `dashboard/urls.py` using `.as_view()`:

```python
path("", views.HomeView.as_view(), name="home")
```

This allows the dashboard to be accessed from the project root:

```text
/
```

## Run

```bash
source ven/bin/activate
python manage.py runserver
```

Then visit:

```text
http://127.0.0.1:8000/
```
