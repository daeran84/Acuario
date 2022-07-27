# Acuario
Proyecto Curso
Sistema de gestión para un acuario.
Se desea realizar un sistema para gestionar la información de un acuario. Se conoce que en el acuario se exhiben animales y plantas acuáticos, 
y además se realizan espectáculos con algunos animales. De las especies en general se registra su identificador, nombre científico, la familia 
a la que pertenece y si su hábitat natural es el mar o el río. De las plantas se registra el número de ejemplares y si son de aguas profundas. 
De los animales por su parte se guarda el nombre que recibió en el acuario, si se ha reproducido en cautiverio, la edad que tienen y la categoría 
a la que pertenecen (delfines, lobos marinos, peces pequeños, crustáceos, tortugas, tiburones u otros). De los animales que participan en los 
espectáculos se almacenan además la fecha en que comenzó a participar en los espectáculos y los datos de su entrenador. De cada entrenador se 
guarda el carné de identidad, el nombre completo, el nombre artístico, la edad, el sexo, la fecha de nacimiento y los años de experiencia. 
Por otro lado, de los espectáculos se guarda el código, el nombre, la hora de comienzo, la duración, el público al que va dirigido (niños, jóvenes, 
adultos o todas las edades) y los animales que participan en él. Por último, se conoce que el acuario tiene un nombre, una lista de especies, 
una lista de entrenadores y una lista de espectáculos. 

El sistema debe permitir las siguientes funcionalidades: 

a) Implemente la funcionalidad necesaria para gestionar (insertar, actualizar, eliminar y listar) los datos de las especies de forma independiente 
(plantas y animales), de los entrenadores y de los espectáculos. 

b) Implemente la funcionalidad necesaria para determinar el índice de aceptación de una especie dado su identificador, si se conoce que se calcula 
de la siguiente forma:
- Las especies que habitan en el mar tiene un índice de 0.9, mientras que las que habitan 
en el río tienen un índice de 0.75.
- Las plantas de aguas profundas pierden un 0.05 de su índice.
- Los animales que se han reproducido en cautiverio gana 0.1 en su índice.
- Los animales que participan en espectáculos ganan 0.5 en su índice. 
- A las plantas se les suma también el número de ejemplares escalado a un valor entre 0 y 1.
- A los animales se les suma también la diferencia entre 1 y su edad escalada a un valor entre 0 y 1. 

c) Implemente la funcionalidad necesaria para seleccionar un animal para que comience a 
participar en los espectáculos. 

d) Implemente la funcionalidad necesaria para determinar cuál es la familia de plantas más 
representada en el acuario. 

e) Implemente la funcionalidad necesaria para asignarle a un animal un nuevo entrenador. 
Tenga presente que esto es posible sólo si ya el animal ha participado en algún 
espectáculo. 

f) Implemente la funcionalidad necesaria para mostrar el listado de los animales de un 
entrenador dado, ordenados ascendentemente por la edad.

g) Pruebe que las operaciones implementadas en el modelo funcionan correctamente según 
los datos de prueba que usted le entró al programa.
