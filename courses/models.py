from django.db import models
from django.contrib.auth import get_user_model
from accounts.models import Subject
from django.utils import timezone

User = get_user_model()


class Course(models.Model):
    title = models.CharField(max_length=120, blank=True, null=True)
    description = models.TextField()
    profs = models.ManyToManyField(User)
    subjects = models.ManyToManyField(Subject)
    created_date = models.DateTimeField(default=timezone.now, blank=True, null=True)
    price = models.IntegerField(default=0)
    photo = models.ImageField(upload_to='courses', blank=True, null=True)

    def __str__(self):
        return self.title

