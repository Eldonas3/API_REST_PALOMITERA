from rest_framework import serializers
from .models import *

class PalomitasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Palomitas
        fields = '__all__'

class PalomiteraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Palomitera
        fields = '__all__'

class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleado
        fields = '__all__'

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class MotivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Motivo
        fields = '__all__'

class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = '__all__'