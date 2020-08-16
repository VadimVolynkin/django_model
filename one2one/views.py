from django.shortcuts import render

from .models import Restaurant, Place


# def restaurant_list(request):
#     restaurant_list = Restaurant.objects.all()
#     return render(request, 'restaurant_list.html', {'restaurant_list': restaurant_list})

def restaurant_list(request):
    # restaurant_list = Restaurant.objects.get(place__name='Mirazh') # get method return string
    # restaurant_list = Restaurant.objects.filter(place__name='Mirazh')# filter method return list

    # сортирует по полю другой таблицы
    restaurant_list = Restaurant.objects.exclude(place__name='Mirazh').order_by('place__name')



    return render(request, 'restaurant_list.html', {'restaurant_list': restaurant_list})


def place_list(request):
    place_list = Place.objects.all()
    return render(request, 'place_list.html', {'place_list': place_list})