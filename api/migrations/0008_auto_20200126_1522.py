# Generated by Django 3.0.2 on 2020-01-26 15:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20200126_1512'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='goal_id',
        ),
        migrations.AddField(
            model_name='task',
            name='goal',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='api.Goal'),
            preserve_default=False,
        ),
    ]
