"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView # new
from app.views import create_food_instance, create_exercise_instance
from accounts.views import send_friend_request, accept_friend_request
from app.views import food_instance_list, exercise_instance_list
from app.views import bmrview
app_name = "app"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include("accounts.urls")),  # new
    path('accounts/', include('django.contrib.auth.urls')),
    path("", TemplateView.as_view(template_name="home.html"), name="home"),
    path("friends", TemplateView.as_view(template_name="friends.html"), name="Friends"),  # new
    path('exercise/add', create_exercise_instance, name='exercise'),  
    path('exercise/', exercise_instance_list, name = "Track Exercise"),
    path("food/add", create_food_instance, name="Add Food"),
    path("food/",  food_instance_list, name = "Track Food"),
    path('send_friend_request/<int:userID>/', 
         send_friend_request, name='send friend request'),
    path('accept_friend_request/<int:requestID>/',
         accept_friend_request, name='accept friend request'),
    path('send_friend_request', TemplateView.as_view(template_name="send_friend_request.html"), name="send"),
    path('bmr/', bmrview, name='bmr_calculation'),


]
