# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-29 15:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Especialidad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cod_especialidad', models.CharField(max_length=10, unique=True)),
                ('nombre', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]