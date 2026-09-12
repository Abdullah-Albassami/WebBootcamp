# Week 7 Day 4 — Path Parameters & Query Parameters

## 1. Core Idea

Django can read values from two parts of a URL:

- **Path parameters** identify the resource or route.
- **Query parameters** control how the page is displayed.

Example:

```text
/products/42/?q=django&page=2
```

- `/products/42/` → path
- `?q=django&page=2` → query string

### Mental Model

```text
Path → URLconf → View argument → Resource detail
Query → request.GET → Filtering / search / pagination → Page state
```

### Main Rule

**Path parameters identify what page or object you want.**  
**Query parameters control how that page is displayed.**

---

# 2. Path Parameters vs Query Parameters

## Path Parameters

Path parameters are:

- Inside the URL path
- Required for the route to match
- Usually used to identify a specific resource
- Validated by Django path converters

Examples:

```text
/products/42/
/blog/django-basics/
/users/aly/
```

## Query Parameters

Query parameters are:

- Written after `?`
- Optional
- Order-independent
- Commonly used for filters, search, sorting, tabs, and pagination
- Read using `request.GET`

Examples:

```text
?q=django
?page=2
?category=backend&sort=recent
```

---

# 3. URL Pattern Map

Django matches the URL against patterns in `urls.py`.

```python
# urls.py
path(
    "products/<int:id>/",
    views.product_detail,
    name="product_detail",
)
```

Here:

- `products/` → static part of the path
- `<int:id>` → dynamic path parameter
- `int` → converter
- `id` → variable name passed to the view
- `product_detail` → URL name

The view receives the converted value:

```python
def product_detail(request, id):
    ...
```

If the route expects an integer:

```text
/products/42/   ✓
/products/abc/  ✗ 404
```

---

# 4. Path Converters

Django path converters validate the shape of a URL value before the view runs.

Common converters:

```python
<int:id>
<slug:slug>
<uuid:pk>
<str:value>
```

Examples:

```python
path("products/<int:id>/", views.product_detail)
path("blog/<slug:slug>/", views.post_detail)
path("items/<uuid:pk>/", views.item_detail)
```

Important distinction:

> A converter checks whether the URL value has the correct shape. The view must still check whether the value makes sense for the application.

---

# 5. Building Links with Parameters

Do not hardcode dynamic URLs when Django can build them safely.

## In Templates

```html
<a href="{% url 'product_detail' id=product.id %}">
    View Details
</a>
```

## In Python

```python
from django.urls import reverse

url = reverse(
    "product_detail",
    kwargs={"id": product.id},
)
```

If a required parameter is missing or incorrect, Django may raise:

```text
NoReverseMatch
```

So always pass every value required by the route.

---

# 6. Understanding Query Parameters

Example URL:

```text
/search/?q=django&page=2&sort=asc
```

Path:

```text
/search/
```

Query string:

```text
q=django&page=2&sort=asc
```

The same values can appear in a different order:

```text
?page=2&q=django&sort=asc
```

The meaning is still the same.

Query parameters are useful for UI state such as:

- Search
- Filters
- Tabs
- Sorting
- Pagination

---

# 7. `request.GET` and `QueryDict`

Django stores query parameters in:

```python
request.GET
```

It behaves like a `QueryDict`.

Example:

```python
def search(request):
    q = request.GET.get("q", "")
    page = request.GET.get("page", "1")
    categories = request.GET.getlist("category")

    return render(request, "search.html", {
        "q": q,
        "page": page,
        "categories": categories,
    })
```

## `.get()`

Use `.get()` to read one value safely.

```python
q = request.GET.get("q", "")
```

If `q` does not exist, the default value is returned.

Avoid this when the key may be missing:

```python
q = request.GET["q"]
```

It can raise:

```text
KeyError
```

## `.getlist()`

Use `.getlist()` for repeated values.

Example URL:

```text
?category=backend&category=python
```

Code:

```python
categories = request.GET.getlist("category")
```

Result:

```python
["backend", "python"]
```

### Important

Values from `request.GET` arrive as strings.

---

# 8. Search and Filter Forms

GET forms are useful for search and filtering because the values appear in the URL.

```html
<form method="get">
    <input
        name="q"
        value="{{ q }}"
        placeholder="Search"
    >

    <select name="category">
        <option value="">All categories</option>
        <option value="backend">Backend</option>
    </select>

    <button type="submit">Filter</button>
</form>
```

View:

```python
def product_list(request):
    q = request.GET.get("q", "")
    category = request.GET.get("category", "")
```

Example resulting URL:

```text
/products/?q=django&category=backend
```

Using GET makes filters:

- Visible
- Shareable
- Bookmarkable

---

# 9. Pagination Uses Query Parameters

Pagination usually stores the current page in a query parameter.

Example:

```text
?page=2
```

Django example:

```python
from django.core.paginator import Paginator


def product_list(request):
    page_number = request.GET.get("page", "1")

    paginator = Paginator(products, 10)
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        "products/list.html",
        {"page_obj": page_obj},
    )
```

If filters are active, pagination links should preserve them.

Example:

```text
?q=django&category=books&page=2
```

Do not build the next-page link using only:

```text
?page=2
```

or the current filters will be lost.

---

# 10. Path and Query Parameters Together

Both can appear in the same URL.

Example:

```text
/products/django-course/?tab=syllabus
```

- `django-course` → identifies the product
- `tab=syllabus` → controls which section is shown

URL pattern:

```python
path(
    "products/<slug:slug>/",
    views.product_detail,
    name="product_detail",
)
```

View:

```python
def product_detail(request, slug):
    product = find_product(slug)

    tab = request.GET.get("tab", "details")

    return render(request, "products/detail.html", {
        "product": product,
        "tab": tab,
    })
```

### Rule

**Path is required. Query is optional. Always provide a default for optional query state.**

---

# 11. Validation and Safety

Treat URL values as user input.

Even if Django converts a value, the application still needs validation.

## Object Existence

Use a 404 when the requested object does not exist.

Typical Django pattern:

```python
from django.shortcuts import get_object_or_404

product = get_object_or_404(Product, id=id)
```

## Validate Allowed Values

Example for sorting:

```python
def clean_sort(value):
    allowed = {"recent", "popular"}
    return value if value in allowed else "recent"
```

Useful for validating:

- Sort values
- Tabs
- Categories
- Difficulty levels

## Numeric Ranges

Check whether numeric values make sense, such as:

- Page numbers
- Years
- Months
- Prices

## Security Note

Avoid exposing sensitive internal IDs when appropriate. Slugs or UUIDs can be better choices depending on the application.

---

# 12. Parameter-Aware Page Architecture

A clean application often uses path and query parameters together.

## Catalog Page

```text
/courses/
```

Query parameters can control:

```text
?category=backend&difficulty=beginner&page=2
```

Flow:

```text
/courses/
    ↓
GET form
    ↓
request.GET
    ↓
filter safely
    ↓
results UI + pagination
```

## Detail Page

```text
/courses/42/?tab=syllabus
```

Flow:

```text
/courses/<int:id>/
    ↓
path converter
    ↓
view receives id
    ↓
query controls active tab
    ↓
template displays selected tab
```

### Key Point

**Path identifies the resource. Query controls how the resource is viewed.**

---

# 13. Troubleshooting Checklist

## Problem: 404 on `/products/abc/`

Likely cause:

```python
<int:id>
```

rejects non-numeric values.

Fix:

- Use a valid number
- Or change the converter if the route should accept another type

---

## Problem: `NoReverseMatch`

Likely cause:

The URL requires an `id` or `slug`, but the value was not supplied correctly.

Fix:

```html
{% url 'product_detail' id=product.id %}
```

or:

```python
reverse("product_detail", kwargs={"id": product.id})
```

---

## Problem: `KeyError: q`

Likely cause:

```python
request.GET["q"]
```

Fix:

```python
request.GET.get("q", "")
```

---

## Problem: Filters Reset When Clicking Next

Likely cause:

The pagination link preserves only `page` and drops other query parameters.

Fix:

Preserve the existing query string when generating pagination links.

---

## Problem: `/login/` Opens a Profile Page

Likely cause:

A generic route is placed before a more specific route.

Django checks URL patterns from top to bottom.

Fix:

Place specific routes before generic routes.

---

# 14. Guided Lab — Parameter-Aware Catalog

Main tasks:

1. Create a `courses` app and mock course list.
2. Add `/courses/` list route and `/courses/<int:id>/` detail route.
3. Read `category` and `difficulty` from `request.GET`.
4. Filter the list and handle missing values gracefully.
5. Add a search field using `method="get"`.
6. Add detail tabs using query parameters such as:

```text
?tab=details
?tab=syllabus
?tab=instructor
```

7. Use `{% url %}` with parameters for detail links.
8. Add pagination using the `page` query parameter.

Exit goal:

- One working filtered URL
- One working detail URL
- One working tab URL

---

# 15. Lab 2 — Product Explorer

Build a parameter-aware product catalog using:

- Path parameters
- Query parameters
- Filtering
- Sorting
- Tabs
- Pagination
- Validation

## Requirements

### 1. Product App

Create a `products` app with mock data containing:

```text
id
name
category
price
rating
description
```

### 2. Routes

```text
/products/
/products/<int:id>/
```

### 3. Filters

Support GET parameters for:

```text
category
min_price
q
```

### 4. Sorting

Allow only:

```text
price
rating
name
```

Any invalid value should fall back to:

```text
name
```

### 5. Pagination

Paginate the filtered results and preserve:

- Search
- Filters
- Sorting

between pages.

### 6. Detail Tabs

On the product detail page support:

```text
?tab=details
?tab=reviews
?tab=shipping
```

Default:

```text
details
```

### 7. Dynamic Links

Use:

```django
{% url %}
```

instead of hardcoding product-detail URLs.

### 8. Safe Handling

- Return a 404 for an invalid product ID.
- Handle missing query parameters safely.
- Handle invalid query values with defaults.

---

# 16. Quick Review

| Concept | Purpose |
|---|---|
| Path parameter | Identifies the resource |
| Query parameter | Controls page state |
| `<int:id>` | Accepts and converts integer path values |
| `<slug:slug>` | Accepts slug-style values |
| `request.GET` | Reads query parameters |
| `.get()` | Reads one optional value safely |
| `.getlist()` | Reads repeated values |
| `{% url %}` | Builds named URLs in templates |
| `reverse()` | Builds named URLs in Python |
| `Paginator` | Splits results across pages |
| `NoReverseMatch` | Usually means a required URL argument is missing or wrong |

## Final Mental Model

```text
PATH
→ identifies the resource
→ required for route matching
→ validated by converters
→ passed as a view argument

QUERY
→ controls view state
→ optional
→ read from request.GET
→ used for search, filters, tabs, sorting, pagination
```

