from django.shortcuts import render, redirect, HttpResponse
from . import models
from .models import Courses
from django.core.urlresolvers import reverse
from django.db.models import Count


# Create your views here.
def index(request):
    if 'logged_user' not in request.session:
        return redirect(reverse('users:index'))
    else:
        users_id = request.session['logged_user']
        user = models.Users.objects.filter(pk=users_id)

    classes = models.Courses.objects.all().order_by('created_at')

    context = {
    'classes':classes,
    'user': user[0],
    }
    return render(request, 'courses/index.html', context)

def add(request):
    add_class = models.Courses(name=request.POST['name'], description=request.POST['description'])
    add_class.save()

    return redirect(reverse('courses:index'))

def remove(request, id):
    course = models.Courses.objects.get(id=id)
    context = {'course':course}

    if request.POST:
        course.delete()
        return redirect(reverse('courses:index'))

    return render(request, 'courses/destroy.html', context)

def user_courses(request, id):
    if request.method == 'POST':
        form = request.POST

    if 'logged_user' not in request.session:
        return redirect(reverse('users:index'))
    else:
        users_id = request.session['logged_user']
        user = models.Users.objects.filter(pk=users_id)

    courses = models.Courses.objects.all()
    students = models.Courses.objects.all().annotate(count=Count('user'))
    all_users = models.Users.objects.all()
    context = {
        'students':students,
        'user': user[0],
        'all_users':all_users,
        'courses':courses,
        }

    return render(request, 'courses/user_courses.html', context)


def add_course(request):
    if request.method == 'POST':
        form = request.POST
        if 'logged_user' not in request.session:
            return redirect(reverse('users:index'))

        addClass = form['course']
        addUser = form['users']
        # print addUser, addClass
        course = models.Courses.objects.get(id=addClass)
        user = models.Users.objects.get(id=addUser)
        course.user.add(user)

    return redirect('/courses/user_courses/'+str(request.session['logged_user']) )
