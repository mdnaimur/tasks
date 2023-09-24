from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.home, name='home'),
    path('login/', views.loginPageCustom, name='login'),
    path('register/', views.registerUser, name='register'),
    path('update-user/', views.updateUser, name='update-user'),
    path('logout/', views.logoutUser, name="logout"),

]
