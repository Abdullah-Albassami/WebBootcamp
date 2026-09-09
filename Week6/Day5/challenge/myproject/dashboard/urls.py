from django.urls import path
from . import views

app_name = "dashboard"

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("reports/", views.reports, name="reports"),
]