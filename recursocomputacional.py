from organismo import Organismo

class RecursoComputacional():
    def __init__(self):
        self.__comida = 0
        self.__cantidad_organismos = 0

    def get_comida(self):
        return self.__comida

    def set_comida(self, N):
        if isinstance(N, int):
            self.__comida = N
        else:
            print("La comida no es int")

    def get_cantidad(self):
        return self.__cantidad_organismos

    def set_cantidad(self, N):
        if isinstance(N, int):
            self.__cantidad_organismos = N
        else:
            print("Error: La cantidad de organismos debe ser un entero no negativo.")

    def comer(self, organismo):
        if isinstance(organismo, Organismo):
            if self.__comida > 0:
                self.__comida -= 1 
                print(f"{organismo.get_nombre()} ha comido. Comida restante: {self.__comida}")
            else:
                print("No hay comida disponible para comer.")
        else:
            print("No se colocó un dato tipo organismo.")   

    def describirse(self):
        print(f"Clase que modela un entorno con sus recursos y capacidad. Comida: {self.__comida}, Cantidad de organismos: {self.__cantidad_organismos}")
