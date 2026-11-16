from django.test import TestCase

# Create your tests here.
class TareaTest(TestCase):
    def test_suma(self):
        resultado = 4+4
        self.assertEqual(resultado, 8)

    def test_resta(self):
        resultado = 10-5
        self.assertEqual(resultado, 5)

    def test_comparacion(self):
        comprobacion = True
        nombre = "Francisco"
        nombre2 = "francisco"
        if nombre.strip().lower() != nombre2:
            comprobacion = False
        self.assertTrue(comprobacion)

































