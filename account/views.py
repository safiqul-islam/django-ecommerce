from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .forms import CreateUserForm
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def index(request):
    form = CreateUserForm()
    context = {
        'form': form,

    }
    return render(request, 'frontend/home/home.html', context)


def usrelogin(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = User.objects.get(email=email)
        username = user.username
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({'message': 'login successfully'}, status=200)
        else:
            return JsonResponse({'error': 'Email or Password is incorrect'}, status=402)


@csrf_exempt
def logfunction(request):
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration is complete")
            return redirect('home')

        else:
            messages.success(request, "Registration is not complete")
            return redirect('home')


def logout_view(request):
    logout(request)
    messages.success(request, "Successfully Logout")
    return redirect('home')

def profile_view(request):
    return render(request, 'frontend/auth/profile.html')