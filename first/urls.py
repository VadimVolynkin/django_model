from django.urls import path
from . import views

urlpatterns = [
    path('', views.CarList, name='car_list'),
    path('car/<int:id>/', views.CarDetail, name='car_detail'),
    path('list/', views.ManufacturerList, name='manufacturer_list'),
    path('list/<int:id>/', views.ManufacturerDetail, name='manufacturer_detail'),
]