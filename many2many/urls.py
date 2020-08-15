from django.urls import path
from . views import SubscribersList, SubscriberDetail
urlpatterns = [
    path('', SubscribersList, name='subscriber_list'),
    path('<int:id>/', SubscriberDetail, name='subscriber_detail'),
]