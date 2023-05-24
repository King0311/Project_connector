from .models import *
from django.forms import ModelForm
from django import forms


class guide_profile_form(ModelForm):
    class Meta:
        model=guide
        fields='__all__'
        widget={
            'guide_name':forms.TextInput(attrs={
                'class':'inputs',
            }),
            'guide_email':forms.EmailInput(attrs={
                'class':'inputs',
            }),
            'teams':forms.TextInput(attrs={
                'class':'inputs',
            }),
        }


class team_profile_form(ModelForm):
    class Meta:
        model=team
        fields='__all__'
        widget={
            'team_std_div':forms.TextInput(attrs={
                'class':'inputs',
            }),
            'team_no':forms.TextInput(attrs={
                'class':'inputs',
            }),
            'guide':forms.TextInput(attrs={
                'class':'inputs',
            }),
            'mem1':forms.TextInput(attrs={
                'class':'inputs',
            }),
            'mem2':forms.TextInput(attrs={
                'class':'inputs',
            }),
            'mem3':forms.TextInput(attrs={
                'class':'inputs',
            }),
            'mem4':forms.TextInput(attrs={
                'class':'inputs',
            }),
            'project_name':forms.TextInput(attrs={
                'class':'inputs',
            }),
        }