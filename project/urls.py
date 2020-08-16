from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('first.urls')),
    # path('m2m/', include('many2many.urls')),
    path('one2one/', include('one2one.urls')),
]
