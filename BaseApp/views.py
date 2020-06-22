from django.shortcuts import render,redirect
from BaseApp.forms import userform,userprofileform,edituserform
# Create your views here.
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.forms import UserChangeForm
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
def index(req):

    return render(req,'BaseApp/index.html')
@login_required
def log_out(req):

    req.session.flush()

    logout(req)
    return HttpResponseRedirect(reverse('index'))
@login_required
def profile(req):
    req.session.set_expiry(req.session.get_expiry_age())
    return render(req, 'BaseApp/profile.html')
@login_required
def edit_profile(req):
    req.session.set_expiry(req.session.get_expiry_age())
    if req.method=="POST":
        user_form=edituserform(data=req.POST,instance=req.user)
        profile_form=userprofileform(data=req.POST,instance=req.user.userformmodel,files=req.FILES)
        if user_form.is_valid() and profile_form .is_valid():

            user_form.save()
            profile_form.save()
            return HttpResponseRedirect(reverse('profile'))

    else:
        user_form=edituserform(instance=req.user)
        profile_form=userprofileform(instance=req.user.userformmodel)
    return render(req,'BaseApp/editprofile.html',{'user_form':user_form,'profile_form':profile_form})
def register(req):
    req.session.set_expiry(req.session.get_expiry_age())
    registered=False

    if req.method=='POST':
        user_form=userform(data=req.POST)
        profile_form=userprofileform(data=req.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user=user_form.save()
            user.set_password(user.password)
            user.save()

            profile=profile_form.save(commit=False)
            profile.user=user

            if 'profile_pic' in req.FILES:
                profile.profile_pic=req.FILES['profile_pic']

            profile.save()

            registered=True
        else:
            print(user_form.errors,profile_form.errors)

    else:
        user_form=userform()
        profile_form=userprofileform()



    return render(req,'BaseApp/register.html',{'registered':registered,'user_form':user_form,'profile_form':profile_form})

def user_login(req):
    req.session.set_expiry(req.session.get_expiry_age())
    if(req.method=='POST'):
        username=req.POST.get('username')
        password=req.POST.get('password')

        user=authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(req,user)
                req.session['username'] = username
                if req.session.has_key('username'):
                    username = req.session['username']
                    return HttpResponseRedirect(reverse('index'))
                else:
                    return render(req, 'login.html', {})

            else:
                return HttpResponse('ACCOUNT NOT ACTIVE')
        else:
            messages.error(req, "Incorrect username or password")
            return redirect('login')

    else:
        return render(req,"BaseApp/login.html")
@login_required
def change_password(req):

    if req.method == 'POST':
        form = PasswordChangeForm(req.user, req.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(req, user)  # Important!
            messages.success(req, 'Your password was successfully updated!')
            return redirect('index')
        else:
            messages.error(req, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(req.user)
    return render(req, 'BaseApp/change_password.html', {
        'form': form
    })
