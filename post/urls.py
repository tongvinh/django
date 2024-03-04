from django.urls import path, include
from . import views

app_name = 'post'
urlpatterns = [
    path('', views.post, name='blog'),
]