from __future__ import unicode_literals

from django.db import models

from ..loginReg.models import Users
# Create your models here.

class Courses(models.Model):
    name = models.CharField(max_length=65)
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ManyToManyField('loginReg.Users', related_name='students')
