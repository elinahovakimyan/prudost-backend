# Generated by Django 3.0.2 on 2020-02-10 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20200210_0803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='score',
            field=models.CharField(default=0, max_length=150, null=True),
        ),
    ]
