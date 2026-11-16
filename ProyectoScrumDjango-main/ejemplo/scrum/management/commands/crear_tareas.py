from django.core.management import BaseCommand
from ...models import Tarea
class Command(BaseCommand):
    help = "Este comando crea tareas de prueba"

    def handle(self, *args, **options):

        try:

            #CREACION DE TAREA
            tarea = Tarea(nombre = "Tarea de prueba")
            tarea.save()
            self.stdout.write(self.style.SUCCESS(f"La tarea con nombre {tarea.nombre} se ha insertada correctamente"))
        except Exception as e:
            print(e)