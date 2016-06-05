# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import app.models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20160602_0109'),
    ]

    operations = [
        migrations.AddField(
            model_name='inmueble',
            name='foto1',
            field=models.ImageField(null=True, upload_to=app.models.get_upload_path_Inmueble, blank=True),
        ),
        migrations.AddField(
            model_name='inmueble',
            name='foto2',
            field=models.ImageField(null=True, upload_to=app.models.get_upload_path_Inmueble, blank=True),
        ),
        migrations.AddField(
            model_name='inmueble',
            name='foto3',
            field=models.ImageField(null=True, upload_to=app.models.get_upload_path_Inmueble, blank=True),
        ),
        migrations.AddField(
            model_name='inmueble',
            name='foto4',
            field=models.ImageField(null=True, upload_to=app.models.get_upload_path_Inmueble, blank=True),
        ),
    ]
