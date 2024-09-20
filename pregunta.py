from alternativa import Alternativa

class Pregunta():
    def __init__(self, enunciado, ayuda=None, requerida=True):
        self.__enunciado = enunciado
        self.__ayuda = ayuda
        self.__requerida = requerida
        self.__alternativas = []

    def agregar_alternativa(self, contenido, ayuda=None):
        nueva_alternativa = Alternativa(contenido, ayuda)
        self.__alternativas.append(nueva_alternativa)

    @property
    def enunciado(self):
        return self.__enunciado

    @enunciado.setter
    def enunciado(self, new_enunciado):
        self.__enunciado = new_enunciado

    @property
    def ayuda(self):
        return self.__ayuda

    @ayuda.setter
    def ayuda(self, new_ayuda):
        self.__ayuda = new_ayuda

    @property
    def requerida(self):
        return self.__requerida
    
    @requerida.setter
    def requerida(self, new_requerida):
        if new_requerida not in (True, False):
            raise ValueError("El valor debe ser True o False")
        else:    
            self.__requerida = new_requerida

    def mostrar_enunciado(self) -> None:
        print(self.enunciado, '[{}]'.format(self.ayuda) if self.ayuda else '')
        print('(pregunta requerida)' if self.requerida else '(pregunta opcional)')
        for num, alternativa in enumerate(self.__alternativas, 1):
            print(f"{num})", end=" ")
            alternativa.mostrar_alternativa()

if __name__ == "__main__":
    p1 = Pregunta('¿Cómo se dice hola en inglés?', requerida=False)
    p1.agregar_alternativa("Hi")
    p1.agregar_alternativa("Yes")
    p1.agregar_alternativa("Thanks")
    p1.mostrar_enunciado()
