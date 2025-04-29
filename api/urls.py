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
router.register(r'estados',views.EstadoViewSet)

urlpatterns=[
    path('',include(router.urls)),
    path('api/v1/empleados/validar_empleado/', views.EmpleadoViewSet.as_view({'post': 'validar_empleado'}), name='validar_empleado')
]