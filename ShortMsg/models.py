from django.db import models
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class Message(models.Model):
    text = models.CharField(max_length=160)
    datetime = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    views_count = models.IntegerField(default=0, null=True)
