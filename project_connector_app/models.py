from django.db import models
import uuid
from django_mysql.models import ListCharField


# Create your models here(comments).


class guide(models.Model):
    guide_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username=models.CharField(max_length=20,default="")
    guide_name = models.CharField(max_length=50)
    guide_email = models.EmailField(max_length=20)
    teams = ListCharField(base_field=models.CharField(
        max_length=100, default=""), size=10, max_length=10000, default="")

    def __str__(self):
        return self.guide_name


class team(models.Model):
    team_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username=models.CharField(max_length=20,default="hee")
    team_std_div = models.CharField(max_length=10)
    team_no = models.CharField(max_length=2, default="")
    guide = models.ForeignKey(guide, on_delete=models.CASCADE, default="")
    mem1=models.CharField(max_length=10 , default=" ")
    mem2=models.CharField(max_length=10 , default=" ")
    mem3=models.CharField(max_length=10 , default=" ")
    mem4=models.CharField(max_length=10 , default=" ")
    project_name=models.CharField(max_length=10 , default=" ")


    def __str__(self):
        return self.team_std_div + " " + self.team_no


class debugg(models.Model):
    name=models.CharField( max_length=50)
    email=models.EmailField( max_length=254)