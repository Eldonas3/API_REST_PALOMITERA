from rest_framework import viewsets
from .models import *
from .serializer import *

class PalomitasViewSet(viewsets.ModelViewSet):
    queryset = Palomitas.objects.all()
    serializer_class = PalomitasSerializer

class PalomiteraViewSet(viewsets.ModelViewSet):
    queryset = Palomitera.objects.all()
    serializer_class = PalomiteraSerializer

class EmpleadoViewSet(viewsets.ModelViewSet):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class MotivoViewSet(viewsets.ModelViewSet):
    queryset = Motivo.objects.all()
    serializer_class = MotivoSerializer

class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer