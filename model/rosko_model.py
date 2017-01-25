class RoskoModel:

	def __init__(self):
		self.respuesta_valida = "arbol"
		self.respuesta = ""

	def setRespuesta(self, respuesta):
		self.respuesta = respuesta

	def validar(self):
		if (self.respuesta_valida == self.respuesta):
			return 'OK'
