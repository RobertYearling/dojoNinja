from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('dojoPost', views.dojo),
    path('ninjaPost', views.ninja),
    path('delete', views.delete),
]
