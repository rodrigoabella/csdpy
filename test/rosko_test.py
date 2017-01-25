from unittest import TestCase
from model.rosko_model import RoskoModel

class TestStringMethods(TestCase):

    def test_guardar_respuesta(self):
        rosko = RoskoModel()
        rosko.setRespuesta('ejemplo respuesta');
        respuesta = rosko.respuesta
        self.assertEqual('ejemplo respuesta', respuesta)

    def test_validar_respuesta(self):
        rosko = RoskoModel()
        rosko.setRespuesta('arbol');
        v = rosko.validar()
        self.assertEqual('OK', v)

    def test_validar_respuesta_incorrecta(self):
        rosko = RoskoModel()
        rosko.setRespuesta('incorrecto');
        v = rosko.validar()
        self.assertEqual('NOK', v)

if __name__ == '__main__':
    unittest.main()
