from django.db import models

import datetime
from django.utils import timezone

class signin(models.Model):
    name = models.CharField(max_length=70)
    date = models.DateTimeField('signup date')
    age =models.IntegerField(max_length=3)
    email=models.EmailField(default="aaa@bb.c")
    # timep=models.TimeField(name='time of signin',default=datetime.datetime.now().time())
    password=models.CharField(max_length=20)
    # remember_later=models.BooleanField(default=True)
    gender=models.CharField(max_length=50,default="male")
    def __str__(self):
    	return self.name

    # def was_published_recently(self):
    #     now=timezone.now()
    #     return now-datetime.timedelta(days=1)<=self.pub_date<=now

class login(models.Model):
    name = models.CharField(max_length=70)
    date = models.DateTimeField('signup date')
    # age =models.DecimalField(max_digits=3)
    time=models.TimeField(name='time of signin')
    # password=models.CharField()
    remember_later=models.BooleanField()
    def __str__(self):
    	return self.name

class contacts(models.Model):
    name = models.CharField(max_length=70)
    email=models.EmailField(default="aaa@bb.c")
    suggestion=models.CharField(max_length=300)
    date = models.DateTimeField('date')
    time=models.TimeField(name='time')

    

    def __str__(self):
    	return self.name