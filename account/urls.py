from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('login', views.usrelogin, name='login'),
    path('registration', views.logfunction, name='registration'),
    path('logout', views.logout_view, name='logout'),
    path('profile', views.profile_view, name='profile')
]
