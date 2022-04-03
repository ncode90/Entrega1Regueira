from django.db import models

# Clase 1
class User(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    email = models.EmailField()

# Clase 2
class Profile(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=150)
    image = models.ImageField()
    website = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=30)

# Clase 3
class Post(models.Model):
    title = models.CharField(max_length=30)
    subtitle = models.CharField(max_length=30)
    body = models.CharField(max_length=150)
    author = models.CharField(max_length=30)
    date = models.DateField()
    image = models.ImageField()