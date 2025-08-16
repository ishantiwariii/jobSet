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
        image = request.FILES.get('image')

        if User.objects.filter(username=email).exists():
            return render(request, 'register.html', {'error': 'Email already registered.'})

        # Create the user
        user = User.objects.create_user(
            username=email,
            email=email,
            password=password,
            first_name=full_name
        )

        # Create the profile with image
        UserProfile.objects.create(
            user=user,
            mobile_number=mobile,
            work_status=work_status,
            updates_opt_in=updates,
            image=image 
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
            next_url = request.GET.get('next')
            return redirect(next_url) if next_url else redirect('home')
        else:
            messages.error(request, 'Invalid email or password.')

    return render(request, 'login.html', {
        'next': request.GET.get('next')
    })

@login_required
def main_profile(request):
    profile = UserProfile.objects.get(user=request.user)
    return render(request, 'main_profile.html', {
        'user': request.user,
        'profile': profile
    })

@login_required(login_url='/login/')
def profile_view(request):
    user = request.user
    profile, created = UserProfile.objects.get_or_create(user=user)

    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        mobile = request.POST.get('mobile')
        work_status = request.POST.get('workStatus')
        updates = request.POST.get('updates') == 'on'
        image = request.FILES.get('image')

        user.first_name = full_name
        user.save()

        profile.mobile_number = mobile
        profile.work_status = work_status
        profile.updates_opt_in = updates
        if image:
            profile.image = image
        profile.save()

        messages.success(request, "Profile updated successfully.")
        return redirect('main-profile')

    return render(request, 'profile.html', {
        'user': user,
        'profile': profile
    })

@login_required(login_url='/login/')
def logout_view(request):
    logout(request)
    return redirect('login') 