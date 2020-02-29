# Generated by Django 3.0.2 on 2020-01-27 17:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_auto_20200127_1656'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='goal',
            name='tasks',
        ),
        migrations.AddField(
            model_name='task',
            name='goal',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='api.Goal'),
        ),
    ]
