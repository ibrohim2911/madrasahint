# Generated by Django 4.0.1 on 2022-01-11 07:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_advansed_user_beginner_user_elemantry_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='advansed',
        ),
        migrations.RemoveField(
            model_name='user',
            name='beginner',
        ),
        migrations.RemoveField(
            model_name='user',
            name='elemantry',
        ),
        migrations.RemoveField(
            model_name='user',
            name='intermediate',
        ),
        migrations.RemoveField(
            model_name='user',
            name='pre',
        ),
        migrations.RemoveField(
            model_name='user',
            name='upper',
        ),
    ]
