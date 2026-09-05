from django.urls import path
from . import views


urlpatterns = [
    path("products/create/", views.create_view, name="create"),
    # path("products/<str:id>/", views.details_view, name="details"),
    path("products/id/<str:id>/", views.details_view, name="details"),
]