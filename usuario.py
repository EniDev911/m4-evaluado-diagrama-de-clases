from encuesta import Encuesta

class Usuario():
    def __init__(self, correo, edad, region):
        self.__correo = correo
        self.__edad = edad
        self.__region = region
    
    @property
    def correo(self):
        return self.__correo

    @correo.setter
    def correo(self, new_correo):
        self.__correo = new_correo

    @property
    def edad(self):
        return self.__edad
    
    @edad.setter
    def edad(self, new_edad):
        self.__edad = new_edad
    
    @property
    def region(self):
        return self.__region

    @region.setter
    def region(self, new_region):
        self.__region = new_region
    
    def contestar_encuesta(self, encuesta: Encuesta, respuestas):
        encuesta.mostrar_encuesta()
        encuesta.agregar_respuestas(respuestas)
            # respuesta = Respuesta(respuesta_texto)

if __name__ == "__main__":
    usuario1 = Usuario("marco@mail.com", 30, 3)
