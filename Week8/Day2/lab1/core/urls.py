from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("theme/<str:theme>/", views.set_theme, name="set_theme"),
    path("cart/add/<int:product_id>/", views.add_to_cart, name="add_to_cart"),
    path("cart/clear/", views.clear_cart, name="clear_cart"),
]