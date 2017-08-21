# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-07 08:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('field1', models.CharField(max_length=50)),
                ('field2', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='mymodel',
            unique_together=set([('field1', 'field2')]),
        ),
    ]
