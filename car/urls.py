from django.urls import path

from . import api

urlpatterns = [

    path('car-list/', api.cars_list, name='cars_list'),
    
]