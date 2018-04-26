from django.test import TestCase

# Create your tests here.
class TravisTest(TestCase):

    def test_prueba(self):
        number = 1
        self.assertEquals(number, 1)