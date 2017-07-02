# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-07-02 10:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('publication_date', models.DateField(blank=True, null=True)),
                ('artist', models.CharField(blank=True, max_length=30)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('length_secs', models.IntegerField(blank=True, null=True)),
                ('song_type', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Pop'), (2, 'Rock'), (3, 'Rap')], null=True)),
            ],
        ),
    ]