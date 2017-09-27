# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-27 19:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0004_auto_20170927_1718'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='yearofparticipation',
            name='contract_type',
        ),
        migrations.AddField(
            model_name='company',
            name='contract_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='years', to='companies.ContractType'),
            preserve_default=False,
        ),
    ]
