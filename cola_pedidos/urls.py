from django.urls import path
from .views import pedidos_pendientes, actualizar_estado_pedido

urlpatterns = [
    path('pedidos/',pedidos_pendientes),
    path('actualizar/',actualizar_estado_pedido)
]