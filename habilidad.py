class Habilidad():
    def __init__(self,nombre):
        self.__funcion =None
        self.__tipo=None
    
    def get_funcion(self):
        return self.__funcion
    
    def set_funcion(self, NewFuncion):
        if isinstance(NewFuncion, str):
            self.__funcion = NewFuncion
        else:
            print("no es string")

    def get_tipo(self):
        return self.__tipo
    
    def set_tipo(self, NewTipo):
        if isinstance(NewTipo, str):
            self.__tipo = NewTipo
        else:
            print("El tipo debe ser un string")
    
    def describirse(self):
        print(f"Función: {self.__funcion}, Tipo: {self.__tipo}")
