from estudiante import Estudiante
from organismo import Organismo
class Mentor(Organismo):
    def __init__(self, nombre):
        super().__init__(nombre) 
        self.grupo = []
        
    def agregar_estudiante(self, nuevo_estudiante):
        if isinstance(nuevo_estudiante, Estudiante):
            if not nuevo_estudiante.get_pertenece():  
                self.grupo.append(nuevo_estudiante)
                nuevo_estudiante.set_pertenencia_a_grupo(True)
                print(f"{nuevo_estudiante.get_nombre()} ha sido agregado con éxito")  
            else:
                print("No se pudo agregar ya que ya pertenece a un grupo")
        else:
            print("El dato no es de tipo estudiante")
    
    def quitar_estudiante(self, estudiante):
        if isinstance(estudiante, Estudiante):
            if estudiante in self.grupo:
                self.grupo.remove(estudiante)
                estudiante.set_pertenencia_a_grupo(False)
                print(f"Se elimino a {estudiante.get_nombre()}") 
            else:
                print(f"{estudiante.get_nombre()} no está en el grupo.")
        else:
            print("El dato no es de tipo estudiante")
    def entrenar_grupo(self, habilidad_a_aprender):
        if self.grupo:
            for estudiante in self.grupo:
                    estudiante.set_habilidades(habilidad_a_aprender)
                    estudiante.set_puntosevolutivos(estudiante.get_puntosevolutivos() + 1)
        print("Se ha enseñado correctamente al grupo")


    def describirse(self):
        print(f"mentor: {self.nombre} grupo: {self.grupo}")