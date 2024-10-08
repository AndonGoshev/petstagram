
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('petstagram.common.urls')),
    path('photos/', include('petstagram.photos.urls')),
    path('pets/', include('petstagram.pets.urls')),
    path('accounts/', include('petstagram.accounts.urls')),
]
