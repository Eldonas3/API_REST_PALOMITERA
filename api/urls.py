from django.urls import path,include
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'palomitas',views.PalomitasViewSet)
router.register(r'palomiteras',views.PalomiteraViewSet)
router.register(r'empleados',views.EmpleadoViewSet)
router.register(r'clientes',views.ClienteViewSet)
router.register(r'motivos',views.MotivoViewSet)
router.register(r'pedidos',views.PedidoViewSet)

urlpatterns=[
    path('',include(router.urls))
]