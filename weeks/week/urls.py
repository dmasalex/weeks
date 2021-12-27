from django.urls import path

from . import views
from .views import *


urlpatterns = [
    path('index/', index, name='index'),
    path('create_date/', data_weeks_create, name='data_weeks_create'),
]