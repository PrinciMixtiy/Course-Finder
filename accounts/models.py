from django.db import models
from django.contrib.auth.models import AbstractUser


class Subject(models.Model):
    name = models.CharField(max_length=120, unique=True)
    abstraction = models.IntegerField(default=1)

    def __str__(self):
        return self.name


class SiteUser(AbstractUser):
    levels = [
        ('C', 'Collège'),
        ('L', 'Lycée'),
        ('U', 'Université'),
    ]
    tel = models.CharField(max_length=120, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars', blank=True, null=True)
    level = models.CharField(max_length=20, choices=levels, blank=True, null=True)
    interests = models.ManyToManyField(Subject)
