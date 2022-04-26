from django.urls import path
from AppBlog import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.home, name="Home"),
    path('users', views.users, name="Users"),
    path('profiles', views.profiles, name="Profiles"),
    path('posts', views.posts, name="Posts"),
    path('addUser', views.addUser, name="AddUser"),
    path('addProfile', views.addProfile, name="AddProfile"),
    path('addPost', views.addPost, name="AddPost"),
    path('userSearch', views.userSearch, name="userSearch"),
    path('search/', views.search),
    path('login', views.login, name="login"),
    path('register', views.register, name="register"),
    path('logout', LogoutView.as_view(template_name="logout.html"), name="logout"),
]