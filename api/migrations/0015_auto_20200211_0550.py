# Generated by Django 3.0.2 on 2020-02-11 05:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0014_category_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goal',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='users_1', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Reward',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('description', models.CharField(blank=True, max_length=300, null=True)),
                ('score', models.CharField(max_length=100)),
                ('used', models.BooleanField(default=False)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='users_2', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Rewards',
            },
        ),
    ]
