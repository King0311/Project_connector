from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path("",views.homepage,name="homepage"),
    path("homepage",views.homepage,name="homepage"),
    path("registor",views.registor,name="registor"),
    path("login",views.login,name="login"),
    path("logout",views.logout,name="logout"),
    path("guide_form",views.guide_form,name="guide_form"),
    path("guide/<str:pr>",views.guide,name="guide"),
    path("guide_chat/<str:pr>/<str:ag>",views.guide_chat,name="guide_chat"),
    path("guide_assign/<str:pr>/<str:ag>",views.guide_assign,name="guide_assign"),
    path("guide_updates/<str:pr>/<str:ag>",views.guide_updates,name="guide_updates"),
    path("team_form",views.team_form,name="team_form"),
    path("student_chat/<str:pr>",views.student_chat,name="student_chat"),
    path("student_work/<str:pr>",views.student_work,name="student_work"),
    path("student_updates/<str:pr>",views.student_updates,name="student_updates"),
]
