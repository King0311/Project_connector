from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import guide as guide_model, team, updates_by_team, work_assign_by_guide
from .forms import *
from django.contrib.auth.decorators import login_required

# Create your views here.


def homepage(request):
    # logedin_user=request.user
    # guide_using_username=guide_model.objects.get(username=logedin_user)
    # teams_using_guide_username=team.objects.filter(guide=guide_using_username)
    # for teamsss in teams_using_guide_username:
    #     print(teamsss)
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
                messages.info(
                    request, "Username Is Already Taken Please Try Different")
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
    if(request.method == 'POST'):
        username = request.POST['username']
        password = request.POST['password']
        type = request.POST['type']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            if type == "guide":
                return redirect("guide_form")
            else:
                return redirect("team_form")
        else:
            messages.info(
                request, "Your are not our user or something may be wrong. Please try again later.")
            return redirect("login")
    else:
        return render(request, "login.html")


def logout(request):
    auth.logout(request)
    return redirect("homepage")


@login_required(login_url="login")
def guide_form(request):
    user = request.user
    logedin_user = User.objects.get(username=user)
    form = guide_profile_form()
    if request.method == 'POST':
        form = guide_profile_form(request.POST)
        if form.is_valid():
            data1 = form.save()
            dynamic_url = reverse('guide', args=[user])
            return redirect(dynamic_url)
        else:
            pass
    else:
        form = guide_profile_form(instance=logedin_user)
    return render(request, "guide_form.html", {'form': form, 'user': user})


def guide(request, pr):
    guide_using_username = guide_model.objects.get(username=pr)
    teams_using_guide_username = team.objects.filter(
        guide=guide_using_username)
    return render(request, "guide.html", {'pr': pr, 'teams_using_guide_username': teams_using_guide_username})


def guide_chat(request, pr, ag):
    guide_using_username = guide_model.objects.get(username=pr)
    teams_using_guide_username = team.objects.filter(
        guide=guide_using_username)
    return render(request, "guide_chat.html", {'pr': pr, 'ag': ag, 'teams_using_guide_username': teams_using_guide_username})


def guide_assign(request, pr, ag):
    guide_using_username = guide_model.objects.get(username=pr)
    teams_using_guide_username = team.objects.filter(guide=guide_using_username)
    username=pr
    guide_name=guide_using_username
    std=ag
    if request.method == 'POST':
        start_date = request.POST['Sdate']
        end_date = request.POST['Edate']
        no = request.POST['no']
        work_name = request.POST['name']
        work_des = request.POST['Des']
        create = work_assign_by_guide.objects.create(
            username=username,
            guide=guide_name,
            team_std_div=std,
            start_date=start_date,
            end_date=end_date,
            team_no=no,
            work_name=work_name,
            work_des=work_des
        )
        create.save()
        return redirect(request.path)

    return render(request, "guide_assign.html", {'pr': pr, 'ag': ag, 'teams_using_guide_username': teams_using_guide_username})


def guide_updates(request, pr, ag):
    guide_using_username = guide_model.objects.get(username=pr)
    teams_using_guide_username = team.objects.filter(guide=guide_using_username)
    teams_updates = updates_by_team.objects.filter(guide=guide_using_username)
    return render(request, "guide_updates.html", {'pr': pr, 'ag': ag, 'teams_using_guide_username': teams_using_guide_username, 'teams_updates': teams_updates})


@login_required(login_url="login")
def team_form(request):
    user = request.user
    logedin_user = User.objects.get(username=user)
    form2 = team_profile_form()
    if request.method == 'POST':
        form2 = team_profile_form(request.POST)
        if form2.is_valid():
            data2 = form2.save()
            dynamic_url = reverse('student_chat', args=[user])
            return redirect(dynamic_url)
        else:
            pass
    else:
        form2 = team_profile_form(instance=logedin_user)
    return render(request, "team_form.html", {'form': form2, 'user': user})


def student_chat(request, pr):
    user = team.objects.get(username=pr)
    print(user.username)
    return render(request, "student_chat.html", {'pr': pr, 'user': user})


def student_work(request, pr):
    user = team.objects.get(username=pr)
    std=user.team_std_div
    no=user.team_no
    work_for_students=work_assign_by_guide.objects.filter(team_std_div=std , team_no=no)
    return render(request, "student_work.html", {'pr': pr, 'user': user,'work_for_students':work_for_students})


def student_updates(request, pr):
    user = team.objects.get(username=pr)
    username = pr
    guide_name=user.guide
    std=user.team_std_div
    if request.method == "POST":
        start_date = request.POST['Sdate']
        end_date = request.POST['Edate']
        work_name = request.POST['name']
        work_des = request.POST['Des']
        create = updates_by_team.objects.create(
            username=username,
            guide=guide_name,
            team_std_div=std,
            start_date=start_date,
            end_date=end_date,
            work_name=work_name,
            work_des=work_des
        )
        create.save()
        return redirect(request.path)
    else:
        pass

    return render(request, "student_updates.html", {'pr': pr, 'user': user})
