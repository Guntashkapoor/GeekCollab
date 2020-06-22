from django import forms
from django.contrib.auth.models import User
from BaseApp.models import userformmodel
stream_choice=(('Select Stream','Select Stream'),('Computer Science and Engineering','Computer Science and Engineering'),
                ('Electronics and Communication','Electronics and Communication'),
                ('Mechanical Engineering','Mechanical Engineering'))
class userform(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password'}))
    username=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Username'}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'Email'}))

    class Meta():
        model=User
        fields=('username','email','password',)

class userprofileform(forms.ModelForm):
    stream=forms.CharField(widget=forms.Select(choices=stream_choice))
    year=forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder':'Degree Year'}))
    university=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'University/College'}))


    portfolio=forms.URLField(widget=forms.URLInput(attrs={'placeholder':'Portfolio/GitHub'}))
    profile_pic=forms.ImageField(required=False,widget=forms.FileInput())
    skills=forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Skills Like Programming, Django, HTML, CSS etc..'}))
    class Meta():

        model=userformmodel
        fields=('portfolio','profile_pic',)
class edituserform(forms.ModelForm):

    class Meta():
        model=User
        fields=('username','email',)
