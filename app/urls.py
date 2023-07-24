from django.urls import path
from .views import *
from . import views

app_name = 'app'
urlpatterns = [
    path('', views.post_create_read),
]