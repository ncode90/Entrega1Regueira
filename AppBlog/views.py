from django.shortcuts import render

def home(request):
      return render(request, "home.html")

def users(request):
      return render(request, "users.html")
      
def profiles(request):
      return render(request, "profiles.html")

def posts(request):
      return render(request, "posts.html")