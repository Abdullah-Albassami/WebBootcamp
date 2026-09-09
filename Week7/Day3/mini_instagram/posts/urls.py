from django.urls import path
from . import views


urlpatterns = [
    path("", views.feed, name="feed"),
    path("like/<int:post_id>/", views.like_post, name="like_post"),
]