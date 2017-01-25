from unittest import TestCase
from model.rosko_model import RoskoModel

class TestStringMethods(TestCase):

    def test_guardar_respuesta(self):
        rosko = RoskoModel()
        rosko.setRespuesta('ejemplo respuesta');
        respuesta = rosko.respuesta
        self.assertEqual('ejemplo respuesta', respuesta)

if __name__ == '__main__':
    unittest.main()
