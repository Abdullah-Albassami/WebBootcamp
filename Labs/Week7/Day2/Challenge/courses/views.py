from django.shortcuts import render


courses = [
    {
        "id": 1,
        "name": "python programming",
        "level": "beginner",
        "student_count": 15,
        "description": "<script>alert('Hacked')</script>",
        "image": "python.jpg",
    },
    {
        "id": 2,
        "name": "django development",
        "level": "intermediate",
        "student_count": 0,
        "description": "Build dynamic websites using <strong>Django</strong>.",
        "image": "django.jpg",
    },
    {
        "id": 3,
        "name": "web development",
        "level": "beginner",
        "student_count": 10,
        "description": "Learn HTML, CSS, and modern web development concepts.",
        "image": "web.jpg",
    },
]


def home(request):
    context = {
        "username": "Abdullah",
    }

    return render(request, "courses/home.html", context)


def course_list(request):
    context = {
        "courses": courses,
    }

    return render(request, "courses/courses.html", context)


def course_detail(request, course_id):
    selected_course = None

    for course in courses:
        if course["id"] == course_id:
            selected_course = course
            break

    context = {
        "course": selected_course,
    }

    return render(request, "courses/course_detail.html", context)