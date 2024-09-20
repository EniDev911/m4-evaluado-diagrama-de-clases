class ListadoRespuestas():
    def __init__(self, respuestas = []) -> None:
        self.__respuestas = respuestas

    @property
    def respuestas(self):
        return self.__respuestas