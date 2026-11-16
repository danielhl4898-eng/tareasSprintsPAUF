import json
from json import JSONDecodeError
from urllib import request

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from scrum.models import Tarea, Sprint, Programador, Etiqueta
from scrum.validaciones import validar_tareas

def bienvenida(Request):
    return HttpResponse("SOS LA SISISAAASS")
'''
def listar_tareas(request):
    if request.method != "GET":
        return JsonResponse("Metodo equivocado")

    tareas = Tarea.objects.all().values()

    return JsonResponse( list(tareas), safe=False)

def listar_tarea(request, id):
    if request.method != "GET":
        return JsonResponse("Metodo equivocado")
    tarea = Tarea.objects.get(id=id)
    datos = {
        "id" : tarea.id,
        "nombre" : tarea.nombre,
        "fecha_inicio" : {
            tarea.fecha_inicio.isoformat()
            if tarea.fecha_inicio else None
        },
        "fecha_fin" : {
            tarea.fecha_fin.isoformat()
            if tarea.fecha_fin else None
        },
        "completa" : tarea.completa,
        "sprint_id": tarea.sprint,
        "programador_id" : tarea.programador
    }
    return JsonResponse(list(datos), safe=False)

def listar_tarea_mejorado(request, id):
    if request.method != "GET":
        return JsonResponse("Metodo equivocado")

    tarea = Tarea.objects.filter(id=id).values().first()

    return JsonResponse(tarea)

def listar_tareas_completas(request):
    if request.method != "GET":
        return JsonResponse("Metodo equivocado")
    tareas = Tarea.objects.filter().values()
    tareas_completadas = tareas.filter(completa=True)
    return JsonResponse(list(tareas_completadas), safe=False)'''

@csrf_exempt
def crear_tarea(request):
    if request.method != "POST":
        return JsonResponse({"error": "Metodo incorrecto"}, status=400)
    try:
        tareaJson= json.loads(request.body)
        errores = validar_tareas(tareaJson)
        tarea = Tarea.objects.create(
            nombre=tareaJson.get("nombre"),
            fecha_inicio=tareaJson.get("fecha_inicio"),
            fecha_fin=tareaJson.get("fecha_fin"),
            completa=tareaJson.get("completa", "False"),
            sprint_id=tareaJson.get("sprint_id"),
            programador_id=tareaJson.get("programador_id")
        )
        etiquetas = tareaJson.get("etiquetas", [])
        crear_etiquetas(etiquetas,tarea)

        if errores:
            return JsonResponse({"errores": errores}, status=400)
        return JsonResponse({"exito": True, "tarea": tarea.id}, status=201)

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)


def crear_etiquetas(etiquetas,objeto):
    for etiqueta in etiquetas:
        etiqueta_model, creada = Etiqueta.objects.get_or_create(nombre=etiqueta)
        objeto.etiquetas.add(etiqueta_model)
        if not creada:
            print("No se ha creado la etiqueta")
        else:
            print("Etiqueta nueva")







