# 📁 Static & Media-Aware Django Site

## 📝 Overview

This lab demonstrates how Django handles:

- Static files
- Media files
- Image uploads
- Default fallback images
- Pillow image validation
- `collectstatic`

---

## ✨ Features

- Shows a default profile image when no uploaded image exists
- Uploads image files using `request.FILES`
- Validates uploaded images using Pillow
- Saves uploaded files inside the `media/` folder
- Displays an uploaded image when available
- Uses CSS from the `static/` folder
- Collects static files into `staticfiles/`

---

## 📂 Project Structure

```text
mylab/
├── config/
├── core/
│   ├── templates/
│   │   └── core/
│   │       └── upload.html
│   ├── urls.py
│   └── views.py
├── media/
├── static/
│   ├── css/
│   │   └── main.css
│   └── images/
│       └── default-avatar.png
├── staticfiles/
├── db.sqlite3
└── manage.py