# Generated by Django 4.1.2 on 2023-06-28 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_connector_app', '0008_updates_by_team_guide'),
    ]

    operations = [
        migrations.AddField(
            model_name='updates_by_team',
            name='team_std_div',
            field=models.CharField(default='', max_length=10),
        ),
    ]
