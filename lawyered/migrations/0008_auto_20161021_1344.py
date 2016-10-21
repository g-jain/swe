# -*- coding: utf-8 -*-
# Generated by Django 1.10.dev20160518135629 on 2016-10-21 13:44
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lawyered', '0007_divorceform_casetype'),
    ]

    operations = [
        migrations.CreateModel(
            name='criminalForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('offense', models.CharField(max_length=250)),
                ('offense_date', models.DateField(default=datetime.date.today)),
                ('situation', models.CharField(max_length=250)),
                ('agency', models.CharField(max_length=250)),
                ('court_past', models.CharField(max_length=250)),
                ('next_date', models.DateField(default=datetime.date.today)),
                ('worked', models.CharField(max_length=250)),
                ('budget', models.CharField(max_length=250)),
                ('details', models.CharField(max_length=250)),
                ('casetype', models.CharField(default='Criminal', max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='duiForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('date_of_citation', models.DateField(default=datetime.date.today, verbose_name='When did you receive the DUI citation?')),
                ('tests', models.CharField(max_length=250)),
                ('bac', models.DecimalField(decimal_places=2, max_digits=6)),
                ('time_of_day', models.CharField(max_length=250)),
                ('reason', models.CharField(max_length=250)),
                ('past', models.CharField(max_length=250)),
                ('next_date', models.DateField(default=datetime.date.today)),
                ('budget', models.CharField(max_length=250)),
                ('details', models.CharField(max_length=250)),
                ('casetype', models.CharField(default='Dui', max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='estateForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('types', models.CharField(max_length=250)),
                ('property_type', models.CharField(max_length=250)),
                ('details', models.CharField(max_length=250)),
                ('need', models.CharField(max_length=250)),
                ('budget', models.CharField(max_length=250)),
                ('casetype', models.CharField(default='Estate', max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='mergerForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('types', models.CharField(max_length=250)),
                ('names', models.CharField(max_length=250)),
                ('circumstances', models.CharField(max_length=250)),
                ('need', models.CharField(max_length=250)),
                ('budget', models.CharField(max_length=250)),
                ('casetype', models.CharField(default='Merger', max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='prenupForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('partner', models.CharField(max_length=250)),
                ('assets', models.CharField(max_length=250)),
                ('debt', models.CharField(max_length=250)),
                ('debt_details', models.CharField(max_length=250)),
                ('assets_exclude', models.CharField(max_length=250)),
                ('exclude_details', models.CharField(max_length=250)),
                ('budget', models.CharField(max_length=250)),
                ('casetype', models.CharField(default='Family', max_length=250)),
            ],
        ),
        migrations.AlterField(
            model_name='divorceform',
            name='casetype',
            field=models.CharField(default='Divorce', max_length=250),
        ),
    ]
