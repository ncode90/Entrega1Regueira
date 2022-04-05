from django.http import HttpResponse
from django.shortcuts import render
from AppBlog.models import Post, Profile, User

def home(request):
      return render(request, "home.html")

def users(request):
      return render(request, "users.html")
      
def profiles(request):
      return render(request, "profiles.html")

def posts(request):
      return render(request, "posts.html")

def addUser(request):
      if request.method == "POST":
            user = User(username=request.POST['username'], password=request.POST['password'], email=request.POST['email'])
            user.save()
            return render(request, "home.html")
      return render(request, "addUser.html")

def addProfile(request):
      if request.method == "POST":
            user = Profile(name=request.POST['name'], description=request.POST['description'], image=request.POST['image'], website=request.POST['website'], email=request.POST['email'], password=request.POST['password'])
            user.save()
            return render(request, "home.html")
      return render(request, "addProfile.html")

def addPost(request):
      if request.method == "POST":
            user = Post(title=request.POST['title'], subtitle=request.POST['subtitle'], body=request.POST['body'], author=request.POST['author'], date=request.POST['date'], image=request.POST['image'])
            user.save()
            return render(request, "home.html")
      return render(request, "addPost.html")

def userSearch(request):
      return render(request, "userSearch.html")

def search(request):
      if request.GET['username']:
            username = request.GET['username']
            users = User.objects.filter(username__icontains=username)
            return render(request, "userResult.html", {"users": users, "username": username})
      else:
            reply = "No data"
      return HttpResponse(reply)