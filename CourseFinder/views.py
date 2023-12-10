from django.shortcuts import render
from courses.models import Course
from django.utils import timezone

current_year = timezone.now().year


def home(request):
    last_course = Course.objects.last()
    return render(request, 'index.html', {'last_course': last_course, 'current_year': current_year})
