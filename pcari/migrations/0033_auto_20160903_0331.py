# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-03 03:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pcari', '0032_quantitativequestion_tagalog_tag'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='rating',
            unique_together=set([('user', 'qid')]),
        ),
    ]