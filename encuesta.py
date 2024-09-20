from listado_respuestas import ListadoRespuestas
from pregunta import Pregunta

class Encuesta():
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__preguntas = []
        self.__respuestas = []
    
    def agregar_pregunta(self, pregunta: Pregunta):
        self.__preguntas.append(pregunta)

    def agregar_respuestas(self, respuestas: ListadoRespuestas):
        self.__respuestas = ListadoRespuestas(respuestas)

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, new_nombre):
        self.__nombre = new_nombre
    
    def mostrar_encuesta(self):
        print(self.nombre.upper())
        print("------------------")
        for pregunta in self.__preguntas:
            pregunta.mostrar_enunciado()
            print()

    def mostrar_respuestas(self):
        print(self.__respuestas)

class EncuestaLimitadaEdad(Encuesta):
    EDAD_MINIMA = 18
    EDAD_MAXIMA = 65

    def __init__(self, nombre, edad):
        super().__init__(nombre)
        self.__edad = edad

    @staticmethod
    def validar_edad(edad):
        return (
            True if edad > EncuestaLimitadaEdad.EDAD_MINIMA and edad < EncuestaLimitadaEdad.EDAD_MAXIMA
            else False
        )
    @property
    def edad(self):
        if self.validar_edad(self.__edad):
            return self.__edad

    def agregar_respuestas(self, respuestas):
        if self.validar_edad(self.__edad):
            super().agregar_respuestas(respuestas)
        else:
            print("No cumples con el rango de edad para responder esta encuesta.")

class EncuestaLimitadaRegion(Encuesta):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.__region = 0
        self.__regiones = [region for region in range(1, 17)]

    def agregar_respuestas(self, respuestas):
        if self.validar_edad(self.__region):
            super().agregar_respuestas(respuestas)
        else:
            print("No cumples con el rango de edad para responder esta encuesta.")
if __name__ == "__main__":

    e_normal = Encuesta("encuesta demo 1")
    p1 = Pregunta('¿Cómo se dice hola en inglés?', requerida=False)
    p1.agregar_alternativa("Hi")
    p1.agregar_alternativa("Yes")
    p1.agregar_alternativa("Thanks", "(esto es un distractor)")

    p2 = Pregunta('¿Cómo se dice serpiente en inglés?', requerida=False)
    p2.agregar_alternativa("Dog")
    p2.agregar_alternativa("Cat")
    p2.agregar_alternativa("Snake", "(esta puede tener sentido)")

    from usuario import Usuario
    e_normal.agregar_pregunta(p1)
    e_normal.agregar_pregunta(p2)
    user1 = Usuario("marco.contreras90@mail.com", 19, region=10)
    user1.contestar_encuesta(e_normal, [1, 3])