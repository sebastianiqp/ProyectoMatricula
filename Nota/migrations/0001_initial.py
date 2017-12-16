# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-27 23:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Docente', '0001_initial'),
        ('Alumno', '0003_auto_20171127_1718'),
        ('Curso', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nota',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cod_nota', models.CharField(max_length=10, unique=True)),
                ('nota1', models.IntegerField(blank=True, default=0, null=True)),
                ('nota2', models.IntegerField(blank=True, default=0, null=True)),
                ('nota3', models.IntegerField(blank=True, default=0, null=True)),
                ('promedio', models.DecimalField(decimal_places=0, default=0, max_digits=8)),
                ('estado', models.CharField(blank=True, max_length=15, null=True)),
                ('alumno', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Alumno.Alumno')),
                ('curso', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Curso.Curso')),
                ('docente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Docente.Docente')),
            ],
        ),
    ]