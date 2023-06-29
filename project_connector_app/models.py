from django.db import models
import uuid


# Create your models here(comments).


class guide(models.Model):
    guide_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username=models.CharField(max_length=20,default="")
    guide_name = models.CharField(max_length=50)
    guide_email = models.EmailField(max_length=20)

    def __str__(self):
        return self.guide_name


class team(models.Model):
    team_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username=models.CharField(max_length=20,default="")
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


class updates_by_team(models.Model):
    username=models.CharField(default="", max_length=50)
    guide=models.ForeignKey(guide, on_delete=models.CASCADE, default="")
    team_std_div = models.CharField(max_length=10, default="")
    start_date=models.DateField( auto_now=False, auto_now_add=False)
    end_date=models.DateField( auto_now=False, auto_now_add=False)
    work_name=models.CharField(default="", max_length=50)
    work_des=models.CharField(default="", max_length=50)

    def __str__(self):
        return self.username 
    

class work_assign_by_guide(models.Model):
    username=models.CharField(default="", max_length=50)
    guide=models.ForeignKey(guide, on_delete=models.CASCADE, default="")
    team_std_div = models.CharField(max_length=10, default="")
    team_no = models.CharField(max_length=2, default="")
    start_date=models.DateField( auto_now=False, auto_now_add=False)
    end_date=models.DateField( auto_now=False, auto_now_add=False)
    work_name=models.CharField(default="", max_length=50)
    work_des=models.CharField(default="", max_length=50)
