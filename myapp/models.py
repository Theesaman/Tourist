from django.db import models

# Create your models here.

class Contact(models.Model):
    first_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.first_name


class Team(models.Model):
    image = models.ImageField()
    full_name = models.CharField(max_length=20)
    Designation = models.TextField()
    instagram = models.URLField()
    github = models.URLField()
    youtube = models.URLField()


class Service(models.Model):
    images = models.ImageField(upload_to='Images/service')
    name = models.CharField(max_length=20)
    description = models.TextField()
    place = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.images} {self.name}"


class Packages(models.Model):
    image = models.ImageField(upload_to='Images/packages')
    day = models.IntegerField()
    place = models.CharField(max_length=20)
    person = models.IntegerField()
    money = models.IntegerField()
    description = models.CharField(max_length=50)