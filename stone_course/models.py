from django.db import models
# -*- coding:utf-8 -*-
# Create your models here.

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class Category(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=64,blank=False,default='')
    sort = models.IntegerField(default=0)
    isDisabled = models.BooleanField()
    cid = models.CharField(max_length=64,blank=False)
    pid = models.CharField(max_length=64,blank=False)
    creater = models.CharField(max_length=64,default='')

    class Meta:
        ordering = ('created',)


class Course(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=64,blank=False,default='')
    linkSrc = models.CharField(max_length=200,blank=False,default='')
    pirce = models.FloatField(blank=False,default=0)
    sort = models.IntegerField(default=0)
    isDisabled = models.BooleanField(default=False)
    categoryId = models.CharField(max_length=64,blank=False)
    creater = models.CharField(max_length=64,default='')

    class Meta:
        ordering = ('created',)