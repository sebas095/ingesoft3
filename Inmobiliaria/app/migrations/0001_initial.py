# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import app.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FotoInmueble',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('foto', models.ImageField(null=True, upload_to=app.models.get_upload_path_Inmueble, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Inmueble',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
                ('numero_habitaciones', models.CharField(max_length=40, null=True, blank=True)),
                ('ubicacion', models.CharField(max_length=100, null=True, blank=True)),
                ('ciudad', models.CharField(max_length=80, null=True, blank=True)),
                ('valor', models.CharField(max_length=20, null=True, blank=True)),
                ('estrato', models.CharField(max_length=20, null=True, blank=True)),
                ('estado', models.CharField(max_length=50, null=True, blank=True)),
                ('activo', models.BooleanField(default=True)),
                ('fecha_registro', models.DateTimeField(auto_now=True)),
                ('usuario', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cedula', models.CharField(unique=True, max_length=30)),
                ('nombres', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=20, null=True, blank=True)),
                ('celular', models.CharField(max_length=20, null=True, blank=True)),
                ('foto', models.ImageField(null=True, upload_to=app.models.get_upload_path_Perfil, blank=True)),
                ('activo', models.BooleanField(default=True)),
                ('fecha_registro', models.DateTimeField(auto_now=True)),
                ('usuario', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='fotoinmueble',
            name='inmueble',
            field=models.ForeignKey(to='app.Inmueble'),
        ),
    ]
