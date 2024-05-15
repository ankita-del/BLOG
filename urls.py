from django.urls import path
from . import views

urlpatterns = [
    path('generate-profile-image/', views.generate_profile_image_view, name='generate_profile_image'),
    path('search-users/', views.search_users, name='search_users'),
]
