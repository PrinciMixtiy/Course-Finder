from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Course
from accounts.models import Subject
from django.utils import timezone

current_year = timezone.now().year


def course_list(request):
    subjects = Subject.objects.order_by('abstraction')
    courses = Course.objects.order_by('-created_date')
    paginator = Paginator(courses, 6)
    try:
        page_number = request.GET['page']
    except KeyError:
        page_number = 1
    page_obj = paginator.get_page(page_number)
    return render(request, 'courses/courses.html', {'courses': page_obj, 'subjects': subjects, 'current_year': current_year})


def search_course(request):
    query = request.GET.get('search-course')
    courses = Course.objects.filter(title__icontains=query).order_by('-created_date')
    if not courses.exists():
        courses = Course.objects.filter(description__icontains=query).order_by('-created_date')
    if not courses.exists():
        courses = Course.objects.filter(profs__username__icontains=query).order_by('-created_date')
    subjects = Subject.objects.order_by('abstraction')
    paginator = Paginator(courses, 6)
    try:
        page_number = request.GET['page']
    except KeyError:
        page_number = 1
    page_obj = paginator.get_page(page_number)

    return render(request, 'courses/courses.html', {'courses': page_obj, 'q': query, 'subjects': subjects, 'current_year': current_year})


def course_by_subject(request, pk):
    subject = Subject.objects.get(pk=pk)
    courses = subject.course_set.order_by('-created_date')
    subjects = Subject.objects.order_by('abstraction')
    paginator = Paginator(courses, 6)
    try:
        page_number = request.GET['page']
    except KeyError:
        page_number = 1
    page_obj = paginator.get_page(page_number)

    return render(request, 'courses/courses.html', {'courses': page_obj, 'subjects': subjects, 'current_year': current_year})
