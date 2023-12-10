from django.urls import path
from . import views

app_name = 'courses'
urlpatterns = [
    path('', views.course_list, name="courses"),
    path('search-course/', views.search_course, name='search-course'),
    path('course-by-subject/<int:pk>/', views.course_by_subject, name='course-by-subject')
]