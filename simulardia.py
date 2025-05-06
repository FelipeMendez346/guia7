from genoma import Genoma
from organismo import Organismo
from habilidad import Habilidad
from recursocomputacional import RecursoComputacional
from estudiante import Estudiante
from mentor import Mentor  
def simular_dia():
    #inicializacion de datos
    mundo=Genoma()
    recursos = RecursoComputacional() 
    recursos.set_comida(50)  
    recursos.set_cantidad(100)
    organismo1 = Organismo("numero1")
    organismo2 = Organismo("numero2")
    organismo3 = Organismo("numero3")
    organismo4 = Organismo("John")
    estudiante1 = Estudiante(organismo1,[])
    estudiante2 = Estudiante(organismo2,[])
    estudiante3 = Estudiante(organismo3,[])
    mentor = Mentor(organismo4)  
    #se crea una habilidad 
    habilidad = "secuenciacion"
    mentor.set_habilidades(habilidad)
    #se crea grupo de estudiantes con un mentor
    mentor.agregar_estudiante(estudiante1)
    mentor.agregar_estudiante(estudiante2)
    mentor.agregar_estudiante(estudiante3)
    mentor.entrenar_grupo(habilidad)
    #se leen los organisos y sus caracteristicas
    print("Lectura de organismos")
    organismo1.describirse()
    estudiante1.describirse()
    organismo2.describirse()
    estudiante2.describirse()
    organismo3.describirse()
    estudiante3.describirse()
    organismo4.describirse()
    mentor.describirse()
    #se quitan recuros iniciales
    comer(organismo1)
    comer(organismo2)
    comer(organismo3)
    comer(organismo4)
    #se guardan los datos en un mundo
    mundo.set_ecosistema(organismo1)
    mundo.set_ecosistema(organismo2)
    mundo.set_ecosistema(organismo3)
    mundo.set_ecosistema(organismo4)


simular_dia()
