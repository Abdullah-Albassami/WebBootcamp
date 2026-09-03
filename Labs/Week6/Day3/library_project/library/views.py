from django.shortcuts import render

# Create your views here.

books = [
    {"id": 1, "title": "Python Basics", "author": "Ahmed"},
    {"id": 2, "title": "Django Basics", "author": "Sara"},
    {"id": 3, "title": "Web Development", "author": "Omar"},
]

def book_list(request):
    return render(request, "library/book_list.html", {"books": books})


def book_detail(request, id):
    book = books[id -1]
    # next(book for book in books if book["id"] == id)

    return render(request, "library/book_detail.html", {"book": book})

