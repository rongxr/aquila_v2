# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-20 16:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('model_model', '0008_auto_20170720_1458'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slowqueryhistory',
            name='checksum',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='model_model.SlowQuery', to_field='checksum'),
        ),
    ]
