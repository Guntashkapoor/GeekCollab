from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save# Create your models here.
from django.dispatch import receiver
from django.conf import settings

stream_choice=(('Computer Science and Engineering','COMPUTER SCIENCE AND ENGINEERING'),
                ('Electronics and Communication','ELECTRONICS AND COMMUNICATION'),
                ('Mechanical Engineering','MECHANICAL ENGINEERING'))
class userformmodel(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    stream = models.CharField(max_length=200,choices=stream_choice,blank=True,null=True)

    year=models.IntegerField(blank=True,null=True)

    university=models.CharField(max_length=200,blank=True,null=True)

    portfolio=models.URLField(blank=True,null=True)

    profile_pic=models.ImageField(upload_to='profile_pics',blank=True,null=True,default="Download.png")

    skills=models.CharField(max_length=3000,blank=True,null=True)

    def __str__(self):
        return self.user.username
