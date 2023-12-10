from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils import timezone

current_year = timezone.now().year

User = get_user_model()


def sign_in(request):
    if request.user.is_authenticated:
        return redirect(reverse('courses:courses'))
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            return redirect(reverse('home'))

        else:
            error_message = "L'utilisateur n'existe pas"

    else:
        error_message = ''

    return render(request, 'accounts/sign-in.html', {'error': error_message, 'current_year': current_year})


@login_required
def sign_out(request):
    logout(request)
    return redirect(reverse('home'))


def sign_up(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        error = ""
        if User.objects.filter(username=username).exists():
            error = f"Le nom d'utilisateur <strong>{username}</strong> est déja utilisé!"

        if not User.objects.filter(username=username).exists():
            user = User.objects.create_user(username=username, password=password)
            login(request, user)

            return redirect(reverse('accounts:add-user-info'))
        else:
            return render(request, 'accounts/sign-up.html', {'error': error, 'current_year': current_year})

    return render(request, 'accounts/sign-up.html', {'current_year': current_year})


@login_required
def add_user_info(request):
    if request.method == 'POST':
        last_name = request.POST['last-name']
        first_name = request.POST['first-name']
        birth_date = request.POST['birth-date']
        user = request.user

        user.last_name = last_name
        user.first_name = first_name
        user.birth_date = birth_date
        user.save()

        return redirect(reverse('accounts:add-user-email'))

    return render(request, 'accounts/information.html', {'current_year': current_year})


@login_required
def add_user_email(request):
    if request.method == 'POST':
        email = request.POST['email']

        user = request.user
        user.email = email
        user.save()

        return redirect(reverse('accounts:email-confirmation'))

    return render(request, 'accounts/email.html', {'current_year': current_year})


@login_required
def add_user_level(request):
    if request.method == 'POST':
        level = request.POST.get('level')
        user = request.user

        user.niveau = level
        user.save()

        return redirect(reverse('home'))

    return render(request, 'accounts/level.html', {'current_year': current_year})


def email_confirmation(request):
    if request.method == 'POST':
        code = request.POST['code']
        if code == "000000":
            return redirect(reverse('accounts:add-user-level'))
        else:
            user = request.user
            user.email = ""
            user.save()
            error = "Code de confirmation invalide"
            return render(request, 'accounts/email.html', {'error': error, 'current_year': current_year})

    return render(request, 'accounts/email-confirmation.html', {'current_year': current_year})
