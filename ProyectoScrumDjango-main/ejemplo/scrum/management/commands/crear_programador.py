from django.core.management import BaseCommand
from ...models import Programador
class Command(BaseCommand):
    help = "Pa crear un programador nigga"
    def handle(self, *args, **options):
        programador = Programador(nombre = "Daniel", apellido1 = "Hergueta")
        programador.save()
        self.stdout.write("Programador creado correctamente")

