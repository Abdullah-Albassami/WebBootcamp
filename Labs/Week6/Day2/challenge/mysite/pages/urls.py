from django.urls import path
from .views import index, faq, team

urlpatterns = [
    path('', index, name='index'),
    path('faq/', faq, name='faq'),
    path('team/', team, name='team'),
]