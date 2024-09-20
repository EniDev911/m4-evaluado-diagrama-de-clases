class Alternativa():

    def __init__(self, contenido, ayuda = '') -> None:
        self.__contenido = contenido
        self.__ayuda = ayuda

    @property
    def contenido(self) -> str:
        return self.__contenido

    @contenido.setter
    def contenido(self, new_contenido) -> None:
        self.__contenido = new_contenido
    
    @property
    def ayuda(self) -> str:
        if self.__ayuda:
            return self.__ayuda

    @ayuda.setter
    def ayuda(self, new_ayuda) -> None:
        self.__ayuda = new_ayuda
    
    def mostrar_alternativa(self) -> None:
        print(self.contenido, '[{}]'.format(self.ayuda) if self.ayuda else '')

if __name__ == "__main__":
    a1 = Alternativa('Alternativa n° 1', 'ayuda de alternativa 1')
    a2 = Alternativa('Alternativa n° 2')
    a1.mostrar_alternativa()
    a2.mostrar_alternativa()

