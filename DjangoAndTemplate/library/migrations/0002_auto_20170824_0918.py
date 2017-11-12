# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-24 09:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='book',
            name='authors',
            field=models.ManyToManyField(blank=True, related_name='books', to='library.Author'),
        ),
        migrations.AlterField(
            model_name='book',
            name='subjects',
            field=models.ManyToManyField(blank=True, related_name='books', to='library.Subject'),
        ),
    ]
