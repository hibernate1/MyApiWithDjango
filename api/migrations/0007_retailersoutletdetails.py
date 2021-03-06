# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-20 08:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20170809_1232'),
    ]

    operations = [
        migrations.CreateModel(
            name='RetailersOutletDetails',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('shopName', models.CharField(max_length=150)),
                ('latitude', models.CharField(max_length=20)),
                ('longitude', models.CharField(max_length=20)),
                ('shopCategory', models.CharField(max_length=20)),
                ('shopAddress', models.CharField(max_length=150)),
                ('shopMobileNumber', models.CharField(max_length=20)),
                ('shopServiceList', models.CharField(max_length=250)),
                ('valid', models.BooleanField(default=True)),
            ],
        ),
    ]
