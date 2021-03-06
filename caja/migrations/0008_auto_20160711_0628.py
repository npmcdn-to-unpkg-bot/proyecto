# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-11 06:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caja', '0007_auto_20160710_1751'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='estadoCivil',
            field=models.CharField(choices=[('viudo', 'viudo'), ('soltero', 'soltero'), ('divorciado', 'divorciado'), ('casado', 'casado')], max_length=10),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='genero',
            field=models.CharField(choices=[('femenino', 'femenino'), ('masculino', 'masculino')], max_length=10),
        ),
        migrations.AlterField(
            model_name='transaccion',
            name='tipo',
            field=models.CharField(choices=[('deposito', 'deposito'), ('retiro', 'retiro')], max_length=30),
        ),
    ]
