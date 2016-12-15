from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string
from django.core.urlresolvers import reverse

# Create your views here.
def index(request):
    return render(request, "randomWord/index.html")

def create(request):
    if 'counter' not in request.session:
        request.session['counter']=1
    else:
        request.session['counter'] +=1
    random = get_random_string(length=13)

    if request.method=="POST":
        request.session['randomWord'] = random
        return redirect(reverse('randomWord:index'))
    else:
        return redirect(reverse('randomWord:index'))
