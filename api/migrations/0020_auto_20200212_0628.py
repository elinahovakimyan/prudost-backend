# Generated by Django 3.0.2 on 2020-02-12 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0019_auto_20200211_0748'),
    ]

    operations = [
        migrations.AddField(
            model_name='goal',
            name='createdAt',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='reward',
            name='createdAt',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='createdAt',
            field=models.DateField(null=True),
        ),
    ]
