from rest_framework import viewsets
from .models import *
from .serializer import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.decorators import action
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import check_password


class PalomitasViewSet(viewsets.ModelViewSet):
    queryset = Palomitas.objects.all()
    serializer_class = PalomitasSerializer

class PalomiteraViewSet(viewsets.ModelViewSet):
    queryset = Palomitera.objects.all()
    serializer_class = PalomiteraSerializer

    
class EmpleadoViewSet(viewsets.ModelViewSet):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer
    
    @action(detail=False, methods=['POST'])
    def validar_empleado(self, request):
        usuario = request.data.get('usuario')
        contrasena = request.data.get('contrasena')

        if not usuario or not contrasena:
            return Response(
                {"message": "Usuario y contraseña son requeridos."},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            empleado = Empleado.objects.get(usuario=usuario)
        except Empleado.DoesNotExist:
            return Response(
                {"message": "Empleado no encontrado."},
                status=status.HTTP_404_NOT_FOUND
            )

        if not empleado.contrasena or not check_password(contrasena,empleado.contrasena):
            return Response(
                {"message": "Credenciales incorrectas."},
                status=status.HTTP_401_UNAUTHORIZED
            )

        return Response(
            {"message": "Iniciando sesión",
             "id_empleado":""+ str(empleado.id_empleado),
             "nombres": "" + str(empleado.nombres),
             "apellidos": "" + str(empleado.apellidos),
             "foto": "" + str(empleado.foto),
             "rol": "" + str(empleado.rol)},
            status=status.HTTP_200_OK
        )


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class MotivoViewSet(viewsets.ModelViewSet):
    queryset = Motivo.objects.all()
    serializer_class = MotivoSerializer

class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

    def create(self, request, *args, **kwargs):
        try:
            response = super().create(request, *args, **kwargs)
            return Response(
                {"message": "Pedido creado con éxito", "data": response.data},
                status=status.HTTP_201_CREATED
            )
        except ValidationError as e:
            custom_errors = {}
            for field, error_list in e.detail.items():
                custom_errors[field] = []
                for error in error_list:
                    if 'Invalid pk' in str(error):
                        custom_errors[field].append(f"El valor proporcionado para {field} es incorrecto o no existe.")
                    else:
                        custom_errors[field].append(str(error))

            return Response(
                {"message": "Error al crear el pedido", "errors": custom_errors},
                status=status.HTTP_400_BAD_REQUEST
            )
        except Exception as e:
            return Response(
                {"message": "Error inesperado al crear el pedido", "errors": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )
        
    def update(self, request, *args, **kwargs):
        try:
            response = super().update(request, *args, **kwargs)
            return Response(
                {"message": "Pedido actualizado con éxito", "data": response.data},
                status=status.HTTP_200_OK
            )
        except ValidationError as e:
            custom_errors = {}
            for field, error_list in e.detail.items():
                custom_errors[field] = []
                for error in error_list:
                    if 'Invalid pk' in str(error):
                        custom_errors[field].append(f"El valor proporcionado para {field} es incorrecto o no existe.")
                    else:
                        custom_errors[field].append(str(error))

            return Response(
                {"message": "Error al actualizar el pedido", "errors": custom_errors},
                status=status.HTTP_400_BAD_REQUEST
            )