# Generated by Django 3.0.2 on 2020-03-20 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0023_auto_20200320_1902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goal',
            name='deadline',
            field=models.DateTimeField(),
        ),
    ]
