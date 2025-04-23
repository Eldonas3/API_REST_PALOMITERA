from django.db import models
from datetime import date
from django.contrib.auth.hashers import make_password
import random

class Palomitas(models.Model):
    id_palomitas = models.AutoField(primary_key=True)
    precio = models.FloatField()
    tamano = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.tamano} - ${self.precio}"

class Palomitera(models.Model):
    id_palomitera = models.AutoField(primary_key=True)
    ubicacion = models.CharField(max_length=200)
    cantidad_palomitas = models.FloatField()
    cantidad_granos = models.FloatField()
    estatus = models.BooleanField(default=False)

    def __str__(self):
        return f"Palomitera {self.id_palomitera} en {self.ubicacion}"

class Empleado(models.Model):
    id_empleado = models.AutoField(primary_key=True)
    usuario = models.CharField(max_length=30)
    contrasena = models.CharField(max_length=128)
    nombres = models.CharField(max_length=128, default='Sin nombres')
    apellidos = models.CharField(max_length=128, default='Sin apellidos')
    rol = models.CharField(max_length=128, default='Sin rol')
    foto = models.CharField(max_length=200)

    def save(self, *args, **kwargs):
        self.contrasena = make_password(self.contrasena)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Empleado {self.id_empleado}"

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

def generar_codigo_verificacion():
    while True:
        codigo = random.randint(0, 99999999)
        if not Pedido.objects.filter(codigo_verificacion=codigo).exists():
            return codigo

class Estado(models.Model):
    id_estado = models.AutoField(primary_key=True)
    estado = models.CharField(max_length=200, default='por preparar')

    def __str__(self):
        return f"Estado: {self.estado}"

class Pedido(models.Model):
    id_pedido = models.AutoField(primary_key=True)
    palomitas = models.ForeignKey(Palomitas, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, null=True, blank=True)
    codigo_verificacion = models.IntegerField(unique=True, default=generar_codigo_verificacion)
    palomitera = models.ForeignKey(Palomitera, on_delete=models.CASCADE, default=1)
    # estatus = models.BooleanField(default=False)
    estado_pedido = models.ForeignKey(Estado, on_delete=models.CASCADE,default=1)
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE, null =True)
    fecha = models.DateField(default=date.today)
    monto_pagado = models.FloatField(blank=True, null=True)
    cambio = models.BooleanField(default=False)
    motivo = models.ForeignKey(Motivo, on_delete=models.CASCADE, null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.palomitas:
            self.monto_pagado = self.palomitas.precio
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Pedido {self.id_pedido} - Código {self.codigo_verificacion} - Fecha {self.fecha} - Monto ${self.monto_pagado}"