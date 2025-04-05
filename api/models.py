from django.db import models
from datetime import date
from django.contrib.auth.hashers import make_password

class Palomitas(models.Model):
    id_palomitas = models.AutoField(primary_key=True)
    precio = models.FloatField()
    tamano = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.tamano} - ${self.precio}"

class Palomitera(models.Model):
    id_palomitera = models.AutoField(primary_key=True)
    no_palomitera = models.IntegerField(default=0)
    ubicacion = models.CharField(max_length=200)
    cantidad_palomitas = models.FloatField()
    cantidad_granos = models.FloatField()

    def __str__(self):
        return f"Palomitera {self.no_palomitera} en {self.ubicacion}"

class Empleado(models.Model):
    id_empleado = models.AutoField(primary_key=True)
    usuario = models.CharField(max_length=30)
    contrasena = models.CharField(max_length=128)
    nombres = models.CharField(max_length=128)
    apellidos = models.CharField(max_length=128)
    rol = models.CharField(max_length=128)
    foto = models.CharField(max_length=200)

    def save(self, *args, **kwargs):
        self.contrasena = make_password(self.contrasena)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Empleado {self.no_empleado}"

class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    saldo = models.FloatField()
    usuario = models.CharField(max_length=30)
    contrasena = models.CharField(max_length=128)
    foto = models.CharField(max_length=200)

    def save(self, *args, **kwargs):
        self.contrasena = make_password(self.contrasena)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Cliente {self.usuario} - Saldo: ${self.saldo}"

class Motivo(models.Model):
    id_motivo = models.AutoField(primary_key=True)
    motivo = models.CharField(max_length=200)

    def __str__(self):
        return f"Motivo: {self.motivo}"

class Pedido(models.Model):
    id_pedido = models.AutoField(primary_key=True)
    no_pedido = models.IntegerField(default=0)
    palomitas = models.ForeignKey(Palomitas, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    codigo_verificacion = models.IntegerField(unique=True)
    palomitera = models.ForeignKey(Palomitera, on_delete=models.CASCADE)
    estatus = models.BooleanField(default=False)
    empleado = models.ForeignKey(Empleado,on_delete=models.CASCADE)
    fecha = models.DateField(default=date.today)
    monto_pagado = models.FloatField(default=0)
    cambio = models.BooleanField(default=False)
    motivo = models.ForeignKey(Motivo, on_delete=models.CASCADE)

    def __str__(self):
        return f"Pedido {self.id_pedido} - Código {self.codigo_verificacion} - Fecha {self.fecha} - Monto ${self.monto_pagado}"