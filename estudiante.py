from organismo import Organismo

class Estudiante(Organismo):
    def __init__(self, nombre, habilidades):
        super().__init__(nombre,habilidades) 
        self.Pertenece_a_grupo = False
    
    def get_pertenece(self):
        return self.Pertenece_a_grupo
    
    def set_pertenencia_a_grupo(self, siono):
        if isinstance(siono, bool):
            self.Pertenece_a_grupo = siono
        else:
            print("el dato no es un valor booleano")
    
    def describirse(self):
        print(f"Estudiante: {self.get_nombre()}, Habilidades: {self.habilidades}, Pertenece a grupo: {self.Pertenece_a_grupo}")
