# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-06 15:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lawyered', '0010_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='area',
            field=models.CharField(default='.', max_length=250),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='bar_no',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='contact',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='details',
            field=models.TextField(default='.', max_length=1000),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='first_name',
            field=models.CharField(default='.', max_length=250),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='last_name',
            field=models.CharField(default='.', max_length=250),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='specialization',
            field=models.CharField(default='.', max_length=250),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='type_user',
            field=models.CharField(choices=[('c', 'Client'), ('l', 'Lawyer')], default='c', max_length=250),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='picture',
            field=models.ImageField(blank=True, upload_to='lawyered/media/'),
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
