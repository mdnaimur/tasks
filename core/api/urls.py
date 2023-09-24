from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes),
    path('task/', views.getTasks),
    path('task/<str:pk>/', views.getTask)
]
