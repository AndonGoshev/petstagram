from petstagram.pets import views
from django.urls import path, include


urlpatterns = (
    path('add/', views.pet_add_page, name="pet-add-page"),
    path('<str:username>/pet/<slug:pet_slug>', include([
        path('', views.pet_details_page, name="pet-datails-page"),
        path('edit/', views.pet_edit_page, name="pet-edit-page"),
        path('delete/', views.pet_delete_page, name="pet-delete-page")
    ]))
)