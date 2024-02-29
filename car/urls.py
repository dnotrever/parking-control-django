from django.urls import path

from . import api

urlpatterns = [
    # GETs
    path('car-list/', api.cars_list, name='cars_list'),
    # POSTs
    path('car-insert/', api.car_insert, name='car_insert'),
]