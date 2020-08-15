from django.shortcuts import render

from .models import Subscribers


def SubscribersList(request):
    context = Subscribers.objects.all()
    return render(request, 'subscriber_list.html', context={'subscriberlist': context})


def SubscriberDetail(request, id):
    context = Subscribers.objects.all()
    return render(request, 'subscriber_list.html', context={'subscriberlist': context})
