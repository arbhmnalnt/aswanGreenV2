from django.urls import path, include
from .views import *


app_name = "the website"

urlpatterns = [
    path('', mainPage, name='mainPage'),
    path('index.html', mainPage, name='mainPage'),
    path('our-services.html', our_services, name='our_services'),
    path('contact-us.html', contact_us, name='contact_us'),
    path('about-us.html', about_us, name='about_us'),
    path('register.html', register, name='register'),
    path('login', login, name='login'),
]