from django.http import *
from .models import *

def validar_tareas(tarea_json):
    errores=[]
    sprint_id = tarea_json.get("sprint_id")
    programador_id = tarea_json.get("programador_id")
    if not sprint_id:
        errores.append("El campo 'sprint_id' es obligatorio.")
    elif not Sprint.objects.filter(id =sprint_id):
        errores.append(f"El sprint con ID {sprint_id} no existe.")
    if not programador_id:
        errores.append("El campo 'programador_id' es obligatorio.")
    elif not Programador.objects.filter(id=programador_id):
        errores.append(f" El programador conID(programador_id) no existe.")

    if errores:
        return errores