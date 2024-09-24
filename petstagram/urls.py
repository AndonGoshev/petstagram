
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('petstagram.common')),
    path('photos/', include('petstagram.photos')),
    path('pets/', include('petstagram.pets')),
    path('acoounts/', include('petstagram.accounts')),
]
