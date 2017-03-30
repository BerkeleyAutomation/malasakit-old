# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-21 21:09
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(default='', max_length=1000)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('accumulated_score', models.IntegerField(default=0)),
                ('rated_count', models.IntegerField(default=0)),
                ('tag', models.CharField(default='', max_length=200)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Progression',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('landing', models.BooleanField(default=False)),
                ('rating', models.BooleanField(default=False)),
                ('review', models.BooleanField(default=False)),
                ('evaluation', models.BooleanField(default=False)),
                ('comment', models.BooleanField(default=False)),
                ('logout', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('qid', models.AutoField(primary_key=True, serialize=False)),
                ('question', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qid', models.IntegerField(default=-1)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('score', models.IntegerField(default=-1)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]