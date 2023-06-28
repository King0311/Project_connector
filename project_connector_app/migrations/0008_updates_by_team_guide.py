# Generated by Django 4.1.2 on 2023-06-27 15:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project_connector_app', '0007_remove_updates_by_team_guide'),
    ]

    operations = [
        migrations.AddField(
            model_name='updates_by_team',
            name='guide',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='project_connector_app.guide'),
        ),
    ]
