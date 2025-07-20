from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import UserProfile

def register_view(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        mobile = request.POST.get('mobile')
        work_status = request.POST.get('workStatus')
        updates = request.POST.get('updates') == 'on'

        if User.objects.filter(username=email).exists():
            return render(request, 'register.html', {'error': 'Email already registered.'})

        user = User.objects.create_user(
            username=email,
            email=email,
            password=password,
            first_name=full_name
        )

        UserProfile.objects.create(
            user=user,
            mobile_number=mobile,
            work_status=work_status,
            updates_opt_in=updates
        )

        login(request, user)
        return redirect('home')

    return render(request, 'register.html')


def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid email or password.')

    return render(request, 'login.html')


@login_required(login_url='/login/')
def profile_view(request):
    user = request.user
    profile = UserProfile.objects.filter(user=user).first()

    return render(request, 'profile.html', {
        'user': user,
        'profile': profile
    })

@login_required(login_url='/login/')
def logout_view(request):
    logout(request)
    return redirect('login') 