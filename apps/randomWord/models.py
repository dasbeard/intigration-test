from __future__ import unicode_literals

from django.db import models

# Create your models here.
# class User(models.Model):
#     first_name = models.CharField(max_length=40)
#     last_name = models.CharField(max_length=40)
#     email = models.EmailField()
#     password = models.CharField(max_length=255)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
# class Message(models.Model):
#     message = models.TexField(max_length=1000)
#     users_id = model.ForeignKey(User)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
# class Comment(models.Model):
#     comment = models.TexField(max_length=1000)
#     users_id = model.ForeignKey(User)
#     message_id = model.ForeignKey(Message)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
