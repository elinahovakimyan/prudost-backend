# Generated by Django 3.0.2 on 2020-04-18 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0026_category_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goal',
            name='order',
            field=models.IntegerField(default=0),
        ),
    ]
