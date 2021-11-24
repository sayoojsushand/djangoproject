from django.db import models

# Create your models here.
class SignUp(models.Model):
    Name = models.CharField(max_length=25)
    Email = models.EmailField()
    Age = models.IntegerField()
    Photo = models.ImageField(upload_to='media/', null=True, blank=True)
    Password = models.CharField(max_length=8)

class Gallery(models.Model):
    Name = models.CharField(max_length=10)
    Description = models.CharField(max_length=50)
    Category = models.CharField(max_length=10)
    Price = models.IntegerField()
    Photo = models.ImageField(upload_to='gallery/', null=True, blank=True)
