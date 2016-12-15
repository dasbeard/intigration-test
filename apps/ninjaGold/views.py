from django.shortcuts import render, redirect, HttpResponse
from random import randrange
from datetime import datetime
from django.core.urlresolvers import reverse

# Create your views here.
def index(request):
    if 'gold' not in request.session:
        request.session['gold']=0
    if 'activity' not in request.session:
        request.session['activity']=[]

    return render(request, 'ninjaGold/index.html')

def process_money(request):
    time = datetime.now()
    place = request.POST['action']
    gamble = 'earned'
    gambleType = 'add'

    if place == "farm":
        gold = randrange(5,11)
        request.session['gold'] += gold


    if place == "caves":
        gold = randrange(5,11)
        request.session['gold'] += gold

    if place == "house":
        gold = randrange(2,6)
        request.session['gold'] += gold

    if place == "casino":
        gold = randrange(-50,50)
        request.session['gold'] += gold
        if gold < 0:
            gamble = 'lost'
            gambleType = 'loss'

    activityString = "You {} {} gold from the {}! ({})".format(gamble, gold, place, time)
    request.session['activity'].insert(0,[gambleType, activityString])

    return redirect(reverse('ninjaGold:index'))

def reset(request):
    request.session.pop('gold')
    request.session.pop('activity')

    return redirect(reverse('ninjaGold:index'))
