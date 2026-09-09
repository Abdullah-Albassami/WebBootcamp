from django.shortcuts import render

movies = [
    {"id": 1, "title": "Inception", "year": 2010, "rating": 8.8},
    {"id": 2, "title": "Interstellar", "year": 2014, "rating": 8.7},
    {"id": 3, "title": "The Dark Knight", "year": 2008, "rating": 9.0},
]


def movie_list(request):
    return render(request, "movies/movie_list.html", {"movies": movies})


def movie_detail(request, id):
    movie = movies[id - 1]

    return render(request, "movies/movie_detail.html", {"movie": movie})