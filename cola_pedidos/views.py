from django.http import JsonResponse
from api.models import Pedido,Estado
from django.views.decorators.csrf import csrf_exempt
import json
from django.shortcuts import get_object_or_404

# Cargar lista de pedidos por preparar
def pedidos_pendientes(request):
    if request.method == 'GET':
        pedidos = Pedido.objects.filter(estado_pedido=1).order_by('id_pedido').values()
        return JsonResponse(list(pedidos), safe=False)
    else:
        return JsonResponse({'error':'Metodo no permitido'}, status=405)
    # pedidos = Pedido.objects.filter(estado_pedido=1).order_by('id_pedido').values()
    # return JsonResponse(list(pedidos), safe=False)

# Vista para actualizar el estado de un pedido
@csrf_exempt
def actualizar_estado_pedido(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            id_pedido = data.get('id_pedido')
            nuevo_estado = data.get('estado_pedido')

            if id_pedido is None or nuevo_estado is None:
                return JsonResponse({'error':'Faltan parametros'}, status = 400)
            
            pedido = get_object_or_404(Pedido, id_pedido= id_pedido)
            estado = get_object_or_404(Estado, id_estado = nuevo_estado)
            pedido.estado_pedido = estado
            pedido.save()

            return JsonResponse({'mensaje':f'Pedido {id_pedido} actualizado a estado {nuevo_estado}'})
        except Exception as e:
            return JsonResponse({'error':str(e)}, status = 500)
    else:
        return JsonResponse({'error':'Metodo no permitido'}, status = 405)

# Función que procesa el pedido en segundo plano
# def procesar_pedido_en_segundo_plano(pedido_id):
#     try:
#         pedido = Pedido.objects.get(id_pedido=pedido_id)

#         # Paso 1: cambiar de estado 1 → 2
#         pedido.estado_pedido = 2
#         pedido.save()
#         print(f"[PROCESO] Pedido {pedido_id} cambiado a estado 2")
#         time.sleep(10)

#         # Paso 2: cambiar de estado 2 → 3
#         pedido.estado_pedido = 3
#         pedido.save()
#         print(f"[PROCESO] Pedido {pedido_id} cambiado a estado 3")
#         time.sleep(5)

#         print(f"[PROCESO] Pedido {pedido_id} finalizado (estado 3, no eliminado)")
#     except Pedido.DoesNotExist:
#         print(f"[ERROR] Pedido {pedido_id} no existe")
#     except Exception as e:
#         print(f"[ERROR] Fallo procesando pedido {pedido_id}: {str(e)}")

# @csrf_exempt
# def actualizar_estado_pedido(request):
#     if request.method == 'POST':
#         try:
#             data = json.loads(request.body)
#             id_pedido = data.get('id_pedido')

#             if id_pedido is None:
#                 return JsonResponse({'error': 'Falta el parámetro id_pedido'}, status=400)

#             pedido = Pedido.objects.get(id_pedido=id_pedido)

#             if pedido.estado_pedido != 1:
#                 return JsonResponse({'error': f'El pedido no está en estado 1, sino en {pedido.estado_pedido}'}, status=400)

#             # Lanzar procesamiento en background
#             thread = threading.Thread(target=procesar_pedido_en_segundo_plano, args=(id_pedido,))
#             thread.start()

#             return JsonResponse({'mensaje': f'El pedido {id_pedido} comenzó su procesamiento en segundo plano.'})

#         except Pedido.DoesNotExist:
#             return JsonResponse({'error': 'Pedido no encontrado'}, status=404)
#         except Exception as e:
#             return JsonResponse({'error': str(e)}, status=500)
#     else:
#         return JsonResponse({'error': 'Método no permitido'}, status=405)

# Me di cuenta que esto se puede procesar en la ESP32 