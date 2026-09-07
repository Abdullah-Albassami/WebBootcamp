from django.shortcuts import render


def home(request):
    context = {
        "title": "Home",
        "username": "Abdullah",
    }

    return render(request, "pages/home.html", context)


def about(request):
    context = {
        "title": "About",
        "description": "This is a small Django multi-page website.",
    }

    return render(request, "pages/about.html", context)


def courses(request):
    context = {
        "title": "Courses",
        "courses": [
            "Python",
            "Django",
            "HTML",
            "CSS",
        ],
    }

    return render(request, "pages/courses.html", context)