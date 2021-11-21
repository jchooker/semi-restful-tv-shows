from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_shows),
    path('shows/new', views.show_form),
    path('shows/create', views.add_info),
    path('shows/<int:id>', views.show_info),
    path('shows/<int:id>/edit', views.edit_show),
    path('shows/<int:id>/update', views.update_show),
    path('shows/<int:id>/destroy', views.delete_show)
]