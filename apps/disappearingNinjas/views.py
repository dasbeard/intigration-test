from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'disappearingNinjas/index.html')

def all_ninjas(request):
    return render(request, 'disappearingNinjas/ninjas.html')

def ninja(request, color):
    context={
    "color": color
    }
    return render(request, 'disappearingNinjas/ninja.html', context)
