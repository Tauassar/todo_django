from django.urls import path
from . import views

urlpatterns = [
    path('', views.homeView),
    path('about/', views.aboutView),
    path('personnal/', views.personnalView),
]
