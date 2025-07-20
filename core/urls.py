from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.home_view, name='home'),      
    path('about/', views.about_view, name='about'),
]
