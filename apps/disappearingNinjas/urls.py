from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^ninjas$', views.all_ninjas, name='ninjas'),
    url(r'^ninja/(?P<color>[a-zA-Z]+)$', views.ninja, name='ninja'),

]
