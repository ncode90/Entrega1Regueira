from django.urls import path
from AppBlog import views

urlpatterns = [
    path('', views.home, name="Home"),
    path('users', views.users, name="Users"),
    path('profiles', views.profiles, name="Profiles"),
    path('posts', views.posts, name="Posts"),
]