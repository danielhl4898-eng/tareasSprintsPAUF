from django.core.management import BaseCommand
from ...models import Programador, Tarea
class Command(BaseCommand):
    def handle(self, *args, **options):
        programador = Programador.objects.get(pk=1)
        tarea = Tarea(nombre="tarea con programador que muerde vasos", programador=programador)

        tarea.save()
        self.stdout.write(self.style.SUCCESS("Tarea creada con programador que existe"))






















