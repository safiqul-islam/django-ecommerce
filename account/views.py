from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'frontend/home/home.html')


def logfunction(request):
    return render(request, 'frontend/auth/login.html')
