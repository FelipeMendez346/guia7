from habilidad import Habilidad
class Organismo(Genoma):
    def __init__(self, nombre):
        super().__init__()  
        self.__habilidades = []
        self.__puntosevolutivos = 0
        self.__Evolucion = 0

    def get_puntosevolutivos(self):
        return self.__puntosevolutivos
    
    def set_puntosevolutivos(self, N):
        if isinstance(N, int):
            self.__puntosevolutivos = self.__puntosevolutivos + N
        else:
            print("No se ingreso un int")

    def get_habilidades(self):
        return self.__habilidades

    def set_habilidades(self, habilidad):
        if isinstance(habilidad, Habilidad):
            self.__habilidades.append(habilidad)
        else:
            print("No se ingreso una habilidad")

    def retirar_habilidad(self, habilidadretirada):
        if habilidadretirada in self.__habilidades:
            self.__habilidades.remove(habilidadretirada)
            print("Se eliminó la habilidad")
    def evolucionar(self,puntos):
        if self.__puntosevolutivos>2:
            __puntosevolutivos-=2
            evolucion+=1

    def describirse(self):
        print(f"Nombre: {self.__nombre}, Tipo: {self.__tipoSerVivo}, Habilidades: {self.__habilidades}, Puntos Evolutivos: {self.__puntosevolutivos}")