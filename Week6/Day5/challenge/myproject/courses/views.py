from django.shortcuts import render

# Create your views here.


courses = [
    {
        "slug": "python",
        "title": "Python Programming",
        "description": "Learn the fundamentals of Python programming.",
    },
    {
        "slug": "django",
        "title": "Django Development",
        "description": "Learn how to build web applications using Django.",
    },
    {
        "slug": "web-development",
        "title": "Web Development",
        "description": "Learn HTML, CSS, and web development fundamentals.",
    },
]


def course_list(request):
    return render(request, "course_list.html", {"courses": courses})


def course_category(request):
    return render(request, "course_category.html")


def course_detail(request, slug):
    course = None

    for item in courses:
        if item["slug"] == slug:
            course = item
            break

    return render(request, "course_detail.html", {"course": course})