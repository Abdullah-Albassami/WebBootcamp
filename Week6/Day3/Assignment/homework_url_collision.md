# Homework — URL Collision

Given:

```python
path("products/create/", create_view),
path("products/<str:id>/", details_view),
```

## 1. What happens when I try to access a product whose ID is "create"?

Django checks the URL patterns from top to bottom.

`products/create/` matches the first path, so `create_view` runs instead of `details_view`.

## 2. How do I view product ID = "create"?

I can change the detail URL to avoid the collision:

```python
path("products/create/", create_view),
path("products/id/<str:id>/", details_view),
```

Then I can access the product with ID `"create"` using:

```text
/products/id/create/
```