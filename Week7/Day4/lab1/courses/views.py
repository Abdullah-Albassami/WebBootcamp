from django.shortcuts import render


# Mock course data
courses = [
    {
        "id": 1,
        "title": "Python Basics",
        "category": "Programming",
        "difficulty": "Beginner",
        "syllabus": "Variables, conditions, loops, functions",
        "instructor": "Ahmed",
    },
    {
        "id": 2,
        "title": "Django Web Development",
        "category": "Programming",
        "difficulty": "Intermediate",
        "syllabus": "URLs, views, templates, models",
        "instructor": "Khalid",
    },
    {
        "id": 3,
        "title": "Network Fundamentals",
        "category": "Networking",
        "difficulty": "Beginner",
        "syllabus": "IP addressing, routing, switching",
        "instructor": "Sara",
    },
    {
        "id": 4,
        "title": "Cybersecurity Basics",
        "category": "Security",
        "difficulty": "Beginner",
        "syllabus": "Threats, vulnerabilities, authentication",
        "instructor": "Mohammed",
    },
    {
        "id": 5,
        "title": "Advanced Python",
        "category": "Programming",
        "difficulty": "Advanced",
        "syllabus": "OOP, decorators, generators",
        "instructor": "Ali",
    },
    {
        "id": 6,
        "title": "Advanced Networking",
        "category": "Networking",
        "difficulty": "Advanced",
        "syllabus": "VLANs, routing protocols, VPN",
        "instructor": "Fahad",
    },
]


def course_list(request):

    # Get filter/search values from the URL.
    category = request.GET.get("category")
    difficulty = request.GET.get("difficulty")
    search = request.GET.get("search", "")

    # Start with all courses.
    filtered_courses = courses

    # Filter by category.
    if category:
        filtered_courses = [
            course
            for course in filtered_courses
            if course["category"] == category
        ]

    # Filter by difficulty.
    if difficulty:
        filtered_courses = [ 
            course 
            for course in filtered_courses 
            if course["difficulty"] == difficulty 
            ]

    # Search by course title.
    if search:
        filtered_courses = [
            course
            for course in filtered_courses
            if search.lower() in course["title"].lower()
        ]

    # Get the page number from the URL.
    # Default page is 1.
    page = request.GET.get("page", "1")

    try:
        page = int(page)
    except ValueError:
        page = 1

    # Prevent page 0 and negative pages.
    if page < 1:
        page = 1

    # Number of courses shown on each page.
    per_page = 2

    # Calculate how many pages are needed.
    total_courses = len(filtered_courses)

    total_pages = (total_courses + per_page - 1) // per_page

    # If courses exist and the user requests a page
    # beyond the last page, show page 1.
    if total_pages > 0 and page > total_pages:
        page = 1

    # Calculate which courses belong to the current page.
    start = (page - 1) * per_page
    end = start + per_page

    page_courses = filtered_courses[start:end]

    # Check whether previous and next pages exist.
    has_previous = page > 1
    has_next = page < total_pages

    context = {
        "courses": page_courses,
        "category": category,
        "difficulty": difficulty,
        "search": search,
        "page": page,
        "total_pages": total_pages,
        "has_previous": has_previous,
        "has_next": has_next,
    }

    return render(request, "courses/course_list.html", context)


def course_detail(request, id):

    # Find the course matching the ID from the URL.
    course = None

    for item in courses:
        if item["id"] == id:
            course = item
            break

    # Get selected tab.
    # Default tab is details.
    tab = request.GET.get("tab", "details")

    # Only allow valid tabs.
    if tab not in ["details", "syllabus", "instructor"]:
        tab = "details"

    context = {
        "course": course,
        "tab": tab,
    }

    return render(request, "courses/course_detail.html", context)