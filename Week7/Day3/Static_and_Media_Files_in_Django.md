# Week 7 Day 3 — Static & Media Files in Django

## Topic 1 — Static Files vs Media Files

### Static files
Static files are part of the project codebase.

They are usually:
- Versioned in Git
- The same for every user
- Updated when developers deploy

Examples:
- CSS
- JavaScript
- Logos
- Icons
- Fonts
- Background images

### Media files
Media files are created or uploaded by users at runtime.

They are usually:
- Not committed to Git
- Different between users
- Possibly private, large, or frequently changing
- Backed up and access-controlled

Examples:
- Profile photos
- PDFs
- CVs
- Product images
- Attachments

**Key idea:**  
Static = assets that ship with the code.  
Media = files created or uploaded by users.

---

## Topic 2 — Static and Media Settings

Django uses URL prefixes and filesystem locations.

```python
# settings.py

STATIC_URL = "/static/"

STATICFILES_DIRS = [
    BASE_DIR / "static",
]

STATIC_ROOT = BASE_DIR / "staticfiles"

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"
```

### STATIC_URL
Browser URL prefix for static files.

Example:

```text
/static/css/main.css
```

### STATICFILES_DIRS
Extra folders Django searches for static files during development.

### STATIC_ROOT
Single output folder used after running `collectstatic`.

### MEDIA_URL
Browser URL prefix for uploaded files.

Example:

```text
/media/avatars/user1.png
```

### MEDIA_ROOT
Physical folder where uploaded files are stored.

**Common mistake:**  
Do not point `STATIC_ROOT` to the same folder used by `STATICFILES_DIRS`.

---

## Topic 3 — Organizing Static and Media Folders

Example project structure:

```text
project_root/
│
├── static/
│   ├── css/
│   │   └── base.css
│   ├── js/
│   │   └── app.js
│   └── images/
│       └── logo.png
│
├── core/
│   └── static/
│       └── core/
│           └── core.css
│
├── blog/
│   └── static/
│       └── blog/
│           └── blog.css
│
└── media/
    ├── avatars/
    └── documents/
```

### Project-level static
Used for shared assets such as:
- Main CSS
- Shared JavaScript
- Logos
- Layout assets

### App-level static
Usually stored under the app name.

Example:

```text
core/static/core/core.css
```

This reduces filename collisions between apps.

### Media
User uploads belong under `MEDIA_ROOT`.

They are not part of source code.

Typical `.gitignore` entries:

```gitignore
media/
staticfiles/
venv/
__pycache__/
```

---

## Topic 4 — Using Static Files in Templates

Load Django's static template tag first:

```django
{% load static %}
```

Then generate asset URLs:

```html
<link rel="stylesheet" href="{% static 'css/main.css' %}">

<script src="{% static 'js/app.js' %}"></script>

<img src="{% static 'images/logo.png' %}" alt="Logo">
```

Do not hardcode `/static/...` directly.

Why?

- Django uses `STATIC_URL`
- Deployment paths may change
- A CDN or another storage backend may be used later

---

## Topic 5 — collectstatic

Development static folders are not necessarily what the production server serves.

Run:

```bash
python manage.py collectstatic
```

Django collects files from:
- App static folders
- Project static folders

and copies them into:

```text
STATIC_ROOT
```

Example flow:

```text
core/static/
blog/static/
project static/
        ↓
python manage.py collectstatic
        ↓
STATIC_ROOT
        ↓
Web server / CDN
```

### Deployment rule
Run `collectstatic` as part of deployment.

`STATIC_ROOT` output can usually be regenerated, so `staticfiles/` is commonly ignored in Git.

---

## Topic 6 — Serving Media Files in Development

Settings:

```python
# settings.py

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"
```

Project URL configuration:

```python
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # project URLs
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
```

This development helper serves uploaded media when `DEBUG=True`.

Example mapping:

```text
/media/avatars/user1.png
        ↓
MEDIA_ROOT/avatars/user1.png
```

---

## Topic 7 — FileField and ImageField

### FileField
Used for general uploaded files.

Examples:
- PDF
- ZIP
- DOCX
- CSV

```python
class Document(models.Model):
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to="documents/")
```

### ImageField
Used specifically for images.

```python
class Profile(models.Model):
    avatar = models.ImageField(
        upload_to="avatars/",
        blank=True,
        null=True
    )
```

`ImageField` requires Pillow.

### upload_to
Creates subfolders under `MEDIA_ROOT`.

For example:

```python
upload_to="documents/"
```

means uploaded files are stored under:

```text
MEDIA_ROOT/documents/
```

and accessed using:

```text
MEDIA_URL + documents/<filename>
```

---

## Topic 8 — Upload Workflow

A successful file upload requires:
- The HTML form
- The Django view
- `request.FILES`

### HTML form

```html
<form method="post" enctype="multipart/form-data">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Upload</button>
</form>
```

The important part is:

```html
enctype="multipart/form-data"
```

Without it, the uploaded file does not reach `request.FILES`.

### View

```python
if request.method == "POST":
    form = DocumentForm(request.POST, request.FILES)

    if form.is_valid():
        form.save()
        return redirect("document_list")
```

### Flow

```text
HTML form
    ↓
request.FILES
    ↓
Form validation
    ↓
form.save()
    ↓
MEDIA_ROOT
```

---

## Topic 9 — Upload Security and Validation

Treat every uploaded file as untrusted input.

### Size limits
Set upload limits at different layers:
- Django form
- Django application
- Web server

### File type validation
Allow only expected extensions or MIME types.

Example:

```python
from django.core.exceptions import ValidationError

def validate_pdf(file):
    if not file.name.lower().endswith(".pdf"):
        raise ValidationError("Only PDF files are allowed.")
```

### Storage isolation
Do not upload user files into:
- Template folders
- Python source folders
- Other executable code locations

### Production concerns
Plan for:
- Permissions
- Backups
- Retention
- Malware scanning
- Removal of old files

---

## Topic 10 — Production Architecture

Static files and media files scale differently.

### Static flow

```text
Git + app static folders
        ↓
collectstatic
        ↓
STATIC_ROOT
        ↓
CDN / web server
```

### Media flow

```text
User upload
        ↓
Django view
        ↓
request.FILES
        ↓
Storage volume / object storage
        ↓
Backup
```

**Key point:**  
Static is mainly a deployment concern.  
Media is mainly a data-management concern.

---

## Topic 11 — Troubleshooting Checklist

### CSS disappeared after deployment
Likely cause:
- `collectstatic` was not run
- Web server points to an empty `STATIC_ROOT`

Fix:
- Run `collectstatic`
- Verify the `STATIC_ROOT` configuration

### Static file gives 404 locally
Likely cause:
- Wrong file path
- Missing `{% load static %}`

Fix:
- Match the folder path
- Load the static template tag

### Uploaded file is not received
Likely cause:
- Missing `multipart/form-data`

Fix:
- Add:

```html
enctype="multipart/form-data"
```

- Use `request.FILES`

### Media file gives 404 in development
Likely cause:
- Media URL route was not added

Fix:

```python
urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)
```

### Permission denied
Likely cause:
- Application cannot write to `MEDIA_ROOT`

Fix:
- Correct operating-system permissions securely

---

# Guided Lab — Static & Media-Aware Site

## Tasks

1. Configure:

```python
STATIC_URL
STATICFILES_DIRS
STATIC_ROOT
```

2. Create:

```text
static/css/main.css
static/images/default-avatar.png
```

3. Configure:

```python
MEDIA_URL
MEDIA_ROOT
```

4. Add media serving to project `urls.py` for development.

5. Create an upload form using:

```html
enctype="multipart/form-data"
```

6. Use `request.FILES` in the upload view.

7. Display either:
- The uploaded image
- A fallback static image

8. Run:

```bash
python manage.py collectstatic
```

Then inspect the generated `staticfiles/` folder.

---

# Lab 3 — Mini Instagram Clone

## Goal

Build one feed page where users can:
- Add image posts
- Write captions
- Like posts

## Core Requirements

1. Create a `Post` model with:
   - `username`
   - `description`
   - `image`
   - `likes`

2. Store uploaded images under:

```text
media/posts/
```

3. Allow only:
- `.jpg`
- `.jpeg`
- `.png`

4. Use:

```html
multipart/form-data
```

and:

```python
request.FILES
```

## Page Behavior

5. Show all posts on one feed page.

6. Each post should display:
- Username
- Image
- Description
- Number of likes

7. Add a **Like** button that increases the like count by 1.

8. Style the page with:

```text
static/css/feed.css
```

## Challenge

If a post has `0` likes, display:

```text
Be the first to like this
```

Otherwise display the number of likes.

## Exit Check

The lab should demonstrate that:
- A valid image post appears
- Invalid image types are rejected
- The Like button updates the count
- `feed.css` appears inside `STATIC_ROOT` after `collectstatic`

---

# Quick Review

Remember the separation:

```text
Static files
→ project assets
→ CSS, JS, logos
→ usually stored in Git
→ collected with collectstatic
→ served from STATIC_ROOT / CDN
```

```text
Media files
→ user uploads
→ profile photos, documents, post images
→ not stored in Git
→ received through request.FILES
→ stored under MEDIA_ROOT
```
