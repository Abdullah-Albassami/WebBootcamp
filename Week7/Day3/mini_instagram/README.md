# Mini Instagram Lab Challenge

A Django lab challenge that demonstrates image uploads, form validation, post feeds, likes, media files, and static files.

## Setup

Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Run migrations:

```bash
python manage.py migrate
```

Start the development server:

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

## Features

- Upload JPG, JPEG, and PNG images
- Reject invalid or unsupported files
- Add a username and description
- Display all posts in one feed
- Like posts
- Show a message when a post has no likes
- Custom Instagram-inspired styling

## Static Files

Collect static files with:

```bash
python manage.py collectstatic
```

Main stylesheet:

```text
static/css/feed.css
```

## Media

Uploaded images are stored in:

```text
media/posts/
```
