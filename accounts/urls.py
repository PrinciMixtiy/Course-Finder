from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('sign-in/', views.sign_in, name='sign-in'),
    path('sign-up/', views.sign_up, name='sign-up'),
    path('add-user-info/', views.add_user_info, name='add-user-info'),
    path('add-user-email/', views.add_user_email, name='add-user-email'),
    path('email-confirmation/', views.email_confirmation, name='email-confirmation'),
    path('add-user-level/', views.add_user_level, name='add-user-level'),
    path('sign-out/', views.sign_out, name='sign-out'),
]
