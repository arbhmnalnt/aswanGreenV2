from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.shortcuts import redirect


# Create your views here.
def mainPage(request):
    return render(request, 'index.html')
    # return HttpResponse("Hello, world. You're at the website main page.")

def our_services(request):
    return render(request, 'our-services.html')

def contact_us(request):
    return render(request, 'contact-us.html')

def about_us(request):
    return render(request, 'about-us.html')

def register(request):
    return render(request, 'register.html')

def login(request):
    # https://play.google.com/store/apps/details?id=com.veestudios.aswangreen
     return redirect('https://play.google.com/store/apps/details?id=com.veestudios.aswangreen')