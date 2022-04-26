from django.http import HttpResponse
from django.shortcuts import render
from AppBlog.models import Post, Profile, User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

@login_required
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

def login(request):
      if request.method == 'POST':
            form = AuthenticationForm(request, data = request.POST)
            if form.is_valid():
                  username = form.cleaned_data.get('username')
                  password = form.cleaned_data.get('password')
                  user = authenticate(username=username, password=password)

                  if user is not None:
                        login(request, user)
                        return render(request, "home.html", {"mensaje":f"Bienvenido {username}"})
                  else:
                        return render(request, "home.html", {"mensaje":"Datos incorrectos"})
            else:
                  return render(request, "home.html", {"mensaje":"Formulario erroneo"})
      form = AuthenticationForm()
      return render(request, "login.html", {"form": form})

def register(request):
      if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                  sername = form.cleaned_data.get('username')
                  form.save()
                  return render(request, "home.html", {"mensaje":"Usuario creado"})
      else:
            form = UserCreationForm()
      return render(request, "register.html", {"form": form})

def about(request):
      return render(request, "about.html")