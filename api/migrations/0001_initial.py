# Generated by Django 4.2.7 on 2025-03-18 01:22

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id_cliente', models.AutoField(primary_key=True, serialize=False)),
                ('saldo', models.FloatField()),
                ('usuario', models.CharField(max_length=30)),
                ('contrasena', models.CharField(max_length=128)),
                ('foto', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id_empleado', models.AutoField(primary_key=True, serialize=False)),
                ('no_empleado', models.IntegerField(default=0)),
                ('usuario', models.CharField(max_length=30)),
                ('contrasena', models.CharField(max_length=128)),
                ('foto', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Motivo',
            fields=[
                ('id_motivo', models.AutoField(primary_key=True, serialize=False)),
                ('motivo', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Palomitas',
            fields=[
                ('id_palomitas', models.AutoField(primary_key=True, serialize=False)),
                ('precio', models.FloatField()),
                ('tamano', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Palomitera',
            fields=[
                ('id_palomitera', models.AutoField(primary_key=True, serialize=False)),
                ('no_palomitera', models.IntegerField(default=0)),
                ('ubicacion', models.CharField(max_length=200)),
                ('cantidad_palomitas', models.FloatField()),
                ('cantidad_granos', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id_pedido', models.AutoField(primary_key=True, serialize=False)),
                ('no_pedido', models.IntegerField(default=0)),
                ('codigo_verificacion', models.IntegerField(unique=True)),
                ('estatus', models.BooleanField(default=False)),
                ('fecha', models.DateField(default=datetime.date.today)),
                ('monto_pagado', models.FloatField(default=0)),
                ('cambio', models.BooleanField(default=False)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.cliente')),
                ('empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.empleado')),
                ('motivo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.motivo')),
                ('palomitas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.palomitas')),
                ('palomitera', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.palomitera')),
            ],
        ),
    ]
