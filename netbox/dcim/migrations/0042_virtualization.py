# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-29 17:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('virtualization', '0001_virtualization'),
        ('dcim', '0041_napalm_integration'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='cluster',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='devices', to='virtualization.Cluster'),
        ),
        migrations.AddField(
            model_name='interface',
            name='virtual_machine',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='interfaces', to='virtualization.VirtualMachine'),
        ),
        migrations.AlterField(
            model_name='interface',
            name='device',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='interfaces', to='dcim.Device'),
        ),
    ]
