from organismo import Organismo
class Genoma():
    def __init__(self):
        self.__nombre = None
        self.__organismosdelecosistema = []

    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self, nombre):
        if isinstance(nombre, str):
            self.__nombre = nombre
        else:
            print("No se ingresó un string")
    
    def get_ecosistema(self):
        return self.__ecosistema

    def set_ecosistema(self, neworganismo):
        if isinstance(neworganismo, Organismo):
            self.__ecosistema.append(neworganismo)
        else:
            print("No se ingresó un organismo")

    def describirse(self):
        print(f"Genoma - Nombre: {self.__nombre}, Ecosistema: {self.__ecosistema}")
