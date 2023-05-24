from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import *
from .forms import *

# Create your views here.


def homepage(request):
    return render(request, "index.html")


def registor(request):
    if(request.method == 'POST'):
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        type = request.POST['type']
        if(password1 == password2):
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username Is Already Taken Please Try Different")
                return redirect('registor')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "This Email Is Already In Use")
                return redirect('registor')
            else:
                user = User.objects.create_user(
                    username=username,
                    email=email,
                    password=password1,
                )
                user.save()
                return redirect('login')
        else:
            messages.info(request, "Password doesn't match")
            return redirect("registor")
    else:
        return render(request, "Registor.html")


def login(request):
    if(request.method=='POST'):
        username=request.POST['username']
        password=request.POST['password']
        type=request.POST['type']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user)
            if type=="guide":
                return redirect("guide_form")
            else:
                return redirect("team_form")
        else:
            messages.info(request,"Your are not our user or something may be wrong. Please try again later.")
            return redirect("login")
    else:
        return render(request, "login.html")
    
def logout(request):
    auth.logout(request)
    return redirect("homepage")


def guide(request,pr):
    return render(request, "guide.html", {'pr':pr})

def guide_form(request):
    user=request.user
    form=guide_profile_form()
    if request.method=='POST':
        form=guide_profile_form(request.POST)
        if form.is_valid:
            data=form.save
            return data
        else:
            pass
    else:
        pass
    return render(request, "guide_form.html",{'form':form,'user':user})


def guide_assign(request):
    return render(request, "guide_assign.html")


def guide_updates(request):
    return render(request, "guide_updates.html")

def team_form(request):
    user=request.user
    form=team_profile_form()
    if request.method=='POST':
        form=team_profile_form(request.POST)
        if form.is_valid:
            data=form.save
            return data
        else:
            pass
    else:
        pass
    return render(request, "team_form.html",{'form':form,'user':user})

def student_chat(request,pr):
    return render(request, "student_chat.html",{'pr':pr})


def student_work(request):
    return render(request, "student_work.html")


def student_updates(request):
    return render(request, "student_updates.html")