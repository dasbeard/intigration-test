from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'add$', views.add, name='add'),
    url(r'remove/(?P<id>\d+)$', views.remove, name='remove'),
    url(r'user_courses/(?P<id>\d+)$', views.user_courses, name='user_courses'),
    url(r'add_course$', views.add_course, name='add_course'),

]
