# Generated by Django 5.1.6 on 2025-03-07 13:19

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='todos', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='todolist',
            name='content',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='todolist',
            name='title',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
