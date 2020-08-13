from django.shortcuts import render

from . models import Car, Manufacturer


def CarList(request):
    cars = Car.objects.all()
    return render(request, 'car_list.html', {'carlist': cars})


def CarDetail(request, id):
    car = Car.objects.get(pk=id)
    return render(request, 'car_detail.html', {'car': car})

def ManufacturerList(request):
    manufacturers = Manufacturer.objects.all()
    return render(request, 'manufacturer_list.html', {'manufacturerlist': manufacturers})


def ManufacturerDetail(request, id):
    manufacturer = Manufacturer.objects.get(pk=id)
    return render(request, 'manufacturer_detail.html', {'manufacturer': manufacturer})
