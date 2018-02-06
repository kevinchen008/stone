from django.db import models

# Create your models here.

class User(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    loginName = models.CharField(max_length=64,blank=False,default='')
    password = models.CharField(max_length=64,blank=False,default='')
    realName = models.CharField(max_length=64,blank=True,default='')
    isDisabled = models.BooleanField()
    creater = models.CharField(max_length=64,default='')

    class Meta:
        ordering = ('created',)

