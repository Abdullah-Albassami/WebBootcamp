from django.urls import path

from . import views


app_name = "feedback"


urlpatterns = [

    path("", views.contact, name="contact"),

    path("thank-you/", views.thank_you, name="thank_you"),
]