from django.urls import path
from .views import book_detail, book_list

urlpatterns = [
    path("", book_list, name="book_list"),
    path("<int:id>/", book_detail, name="book_detail"),
]