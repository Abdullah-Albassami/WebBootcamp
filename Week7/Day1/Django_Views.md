# Week 7 Day 1 — Django Views

## Today's Mental Model

URLs decide **where the request goes**.  
Views decide **what happens next**.

```text
Browser → URL → View → Template → Response
```

A view acts as:

- **Decision point** — reads the request, runs logic, prepares output.
- **Bridge** — connects backend computation to the frontend.
- **Controller-like layer** — coordinates the request/response flow.

> If routing is the map, views are where the work actually happens.

---

## 1. View in the Request-Response Cycle

A Django view receives a request and must return a response.

```text
Request received
    ↓
URL matched
    ↓
View runs
    ↓
Context prepared
    ↓
Template rendered
    ↓
Response returned
```

A view may also work with a model:

```text
Browser → URL → View → Model? → Template → Response → Browser
```

The view is the step that coordinates everything.

---

## 2. The `HttpRequest` Object

Every Django view receives a `request` object containing information about the incoming HTTP request.

### Common request attributes

```python
request.method
```

HTTP method such as `GET`, `POST`, `PUT`, etc.

```python
request.GET
```

Query parameters from the URL.

```python
request.POST
```

Submitted form data.

```python
request.headers
```

Request/browser metadata.

```python
request.COOKIES
```

Cookies sent by the browser.

```python
request.session
```

Server-side session state.

```python
request.FILES
```

Uploaded files.

```python
request.path
```

Current URL path.

When debugging a view, ask:

> What did the browser send in the request?

---

## 3. Function-Based Views (FBVs)

The simplest Django view is a Python function that accepts a request and returns a response.

```python
from django.http import HttpResponse

def homepage(request):
    return HttpResponse("Hello, Django!")
```

### Why use FBVs?

- Simple
- Explicit
- Easy to trace
- Good for small pages
- Good for quick tests
- Good when the logic is straightforward

A view must always return an `HttpResponse`-like object.

Avoid writing large HTML strings directly inside Python.

FBVs are not only for beginners. They are still useful professionally when the logic is clear.

---

## 4. Rendering Templates with Context

Most Django pages return HTML using `render()`.

```python
from django.shortcuts import render

def home(request):
    context = {
        "username": "Aly",
        "age": 25
    }

    return render(request, "home.html", context)
```

The template can use the values from the context dictionary:

```html
<h1>Hello {{ username }}</h1>
<p>You are {{ age }} years old.</p>
```

### Context

Context is a dictionary that carries Python data from the backend view into the HTML template.

```text
View → Context → Template
```

Context is the bridge between backend logic and the page the user sees.

---

## 5. Response Types in Django

A Django view does not always return a normal webpage.

### `HttpResponse`

Used for plain text or simple output.

```python
from django.http import HttpResponse

return HttpResponse("Hello")
```

### `render()`

Used to return an HTML template with optional context.

```python
return render(request, "home.html", context)
```

### `redirect()`

Sends the user to another route.

```python
return redirect("success")
```

### `JsonResponse`

Returns JSON data, commonly for APIs or status endpoints.

```python
from django.http import JsonResponse

return JsonResponse({"status": "ok"})
```

### `FileResponse`

Used for downloadable files such as PDFs or CSVs.

### `StreamingHttpResponse`

Used for large files or live/streamed responses.

---

## 6. GET vs POST Inside Views

A page can behave differently depending on the HTTP method.

```python
def contact(request):

    if request.method == "GET":
        return render(request, "contact.html")

    if request.method == "POST":
        # Process submitted data
        return redirect("success")
```

### GET

Used to retrieve or display data.

Usually safe and repeatable.

### POST

Used to submit or change data.

Commonly used for forms and actions.

### PUT / PATCH / DELETE

More common in APIs and advanced workflows.

A useful rule:

> Separate read logic from write logic.

---

## 7. Reading Data from the Request

Views often need user input before deciding what to return.

### Query string

Example URL:

```text
/search/?q=django&page=2
```

Read values with:

```python
q = request.GET.get("q", "")
page = request.GET.get("page", 1)
```

Using `.get()` allows a fallback/default value.

### POST form body

```python
name = request.POST.get("name")
email = request.POST.get("email")
```

### Headers

```python
agent = request.headers.get("User-Agent")
```

### Common mistakes

Avoid this when the key may not exist:

```python
request.GET["q"]
```

Prefer:

```python
request.GET.get("q", "")
```

Also:

- Validate user input before using it.
- Avoid mixing display logic and submission logic unnecessarily.

---

## 8. Class-Based Views (CBVs)

Class-Based Views package view behavior inside a class.

```python
from django.views import View
from django.http import HttpResponse

class HomeView(View):

    def get(self, request):
        return HttpResponse("Hello from a class view")
```

### Why use CBVs?

- Reusable structure
- Useful for larger applications
- Easy separation of HTTP methods
- Works well with mixins and generic views
- Useful for CRUD-style features

To connect a CBV in `urls.py`, use:

```python
HomeView.as_view()
```

`as_view()` converts the class into something Django can call as a view.

---

## 9. CBV Dispatching

CBVs automatically route HTTP methods to matching class methods.

```text
Request
   ↓
dispatch()
   ├── GET    → get()
   ├── POST   → post()
   └── DELETE → delete()
```

Example:

```python
class ContactView(View):

    def get(self, request):
        return render(request, "contact.html")

    def post(self, request):
        email = request.POST.get("email")
        return redirect("success")
```

The main idea:

```text
GET  → get()
POST → post()
```

This keeps HTTP method logic separated without repeatedly writing `if request.method == ...`.

---

## 10. FBV vs CBV

Both are valid. The choice depends on complexity and reuse.

### Use FBV when

- Logic is simple
- Only GET/POST is needed
- The view is short
- You want full control and direct readability

### Use CBV when

- You need reusable logic
- Multiple HTTP methods are involved
- You use mixins or generic views
- You are building CRUD-style features

---

## 11. Cookies and Sessions Inside Views

Views can personalize behavior using browser and server state.

### Cookies

Cookies are stored in the browser and are useful for preferences.

```python
theme = request.COOKIES.get("theme", "light")

response = HttpResponse("OK")
response.set_cookie("theme", "dark")

return response
```

```text
Cookie → browser-side data
```

### Sessions

Sessions store state server-side.

```python
request.session["cart_items"] = 3

count = request.session.get("cart_items", 0)

del request.session["cart_items"]
```

```text
Session → server-side state
```

Sessions are useful for things such as carts or login-related state.

---

## 12. Keeping Views Professional

Views should coordinate work, not become a dumping ground.

### Fat views

Move heavy logic into:

- models
- forms
- services
- utility/helper functions

### HTML inside `HttpResponse`

Avoid writing UI directly in Python.

Use templates instead.

### Queries inside templates

Fetch and prepare data before rendering the template.

### Repeated logic

Reuse logic through:

- helper functions
- CBVs
- mixins

### Huge JSON responses

Return only the data the client actually needs.

> A thin view does not mean an empty view. It means the view delegates responsibility clearly.

---

# Guided Lab — Multi-Method View System

## Objective

Build views that handle:

- pages
- forms
- sessions
- JSON

## Tasks

1. Create an `accounts` app.
2. Add `RegisterView` with GET/POST.
3. Add `LoginView` with GET/POST.
4. Add `ProfileView` that reads session data.
5. Create one FBV status endpoint.
6. Return `JsonResponse` for the status endpoint.
7. Connect URLs and give them names.
8. Test the pages and capture screenshots.

## Deliverables

```text
views + URLs + templates + screenshots of working pages
```

---

# Week 7 Day 1 Summary

Main topics covered:

1. Role of Django views
2. Request-response cycle
3. `HttpRequest`
4. Function-Based Views
5. `render()` and context
6. Response types
7. GET vs POST
8. Reading request data
9. Class-Based Views
10. `as_view()`
11. `dispatch()`
12. FBV vs CBV
13. Cookies
14. Sessions
15. Thin/professional views
16. Guided multi-method view lab
