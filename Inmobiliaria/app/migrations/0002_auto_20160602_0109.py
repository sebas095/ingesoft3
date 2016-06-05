# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inmueble',
            old_name='nombre',
            new_name='tipo',
        ),
        migrations.RemoveField(
            model_name='inmueble',
            name='estado',
        ),
        migrations.AddField(
            model_name='inmueble',
            name='descripcion',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='inmueble',
            name='para',
            field=models.CharField(max_length=20, null=True, blank=True),
        ),
    ]
