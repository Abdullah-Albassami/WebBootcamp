from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def post_list(request):
    posts = [
        {
            "id": 1,
            "title": "My First Post",
            "content": "This is the content of my first blog post."
        },
        {
            "id": 2,
            "title": "Learning Django",
            "content": "Today I learned about Django URLs and templates."
        },
        {
            "id": 3,
            "title": "Working with Templates",
            "content": "Django templates let us display dynamic data."
        },
    ]

    return render(request, "post_list.html", {"posts": posts})


def post_create(request):
    return render(request, "post_create.html")


def post_detail(request, id):
    posts = [
        {
            "id": 1,
            "title": "My First Post",
            "content": "This is the content of my first blog post."
        },
        {
            "id": 2,
            "title": "Learning Django",
            "content": "Today I learned about Django URLs and templates."
        },
        {
            "id": 3,
            "title": "Working with Templates",
            "content": "Django templates let us display dynamic data."
        },
    ]

    post = posts[id - 1]

    return render(request, "post_detail.html", {"post": post})