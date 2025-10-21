# https://pastebin.com/BBdN7XNq

from queue import Queue as Cola

'''
Ejemplo de parcial (colas):
 Un banco recibe a sus clientes y les otorga, a medida que van llegando, una clasificación según si son "prioritarios" o "no_prioritarios". Dicha información se guarda en una Cola de tuplas String x String, donde la primer componente es el nombre del cliente y la segunda componente es la clasificación. Luego un cajero especial atiende a todos aquellos clientes que fueron clasificados como "prioritarios", consevando el orden en que fueron llegando. Se pide implementar la función atencion_con_prioridad, que devuelve una Cola de clientes "prioritarios".
 
atencion_con_prioridad(inout clientes: Cola⟨ String x String ⟩) : Cola⟨ String x String⟩ {
  requiere:{ Las primeras componentes de clientes son strings no vacíos y 
      todos distintos entre sí }
  requiere:{ Las segundas componentes de clientes son strings no vacíos e iguales a 
      "prioritario" o "no_prioritario"}
  asegura: { Todas las primeras componentes de res aparecen en alguna primera componente de 
      clientes@pre cuya segunda componente es igual a "prioritario"}
  asegura: { Todas las primeras componentes de clientes aparecen en alguna primera componente 
      de clientes@pre cuya segunda componente es igual a "no_prioritario"}
  asegura: { |res| + |clientes| = |clientes@pre|}
  asegura: { Para todo cliente c1 y cliente c2 que son "prioritario" pertenecientes a 
      clientes@pre, si c1 aparece antes que c2 en clientes@pre entonces 
      c1 aparece antes que c2 en res}
  asegura: { Para todo cliente c1 y cliente c2 que son "no_prioritario" pertenecientes a 
      clientes@pre, si c1 aparece antes que c2 en clientes@pre entonces 
      c1 aparece antes que c2 en clientes}
}
 
Ejemplo: atencion_con_prioridad(c), donde c es una cola en la cual se insertaron (en orden)
los siguientes elementos:    
    ("Laura", "no_prioritario")     
    ("Juan", "no_prioritario")
    ("Pablo", "prioritario")      
    ("Amalia", "no_prioritario")
    ("Oscar", "prioritario")
 
Debe devolver:      
    ("Pablo", "prioritario")   
    ("Oscar", "prioritario")
 
Y modificar la cola clientes para que ya no aparezcan ahí.
'''

def atencion_con_prioridad(clientes: Cola[(str, str)]) -> Cola[(str, str)]:
    prioritarios: Cola = Cola()
    no_prioritarios: Cola = Cola()

    while not clientes.empty():
        cliente = clientes.get()
        if cliente[1] == "prioritario":
            prioritarios.put(cliente)
        else:
            no_prioritarios.put(cliente)

    # Pongo los no_prioritarios en la cola original de clientes
    while not no_prioritarios.empty():
        clientes.put(no_prioritarios.get())

    return prioritarios

# clientes: Cola = Cola()
# clientes.put(("Laura", "no_prioritario"))
# clientes.put(("Juan", "no_prioritario"))
# clientes.put(("Pablo", "prioritario"))
# clientes.put(("Amalia", "no_prioritario"))
# clientes.put(("Oscar", "prioritario"))

# print("Clientes antes:", clientes.queue)

# prioritarios = atencion_con_prioridad(clientes)

# print("Prioritarios:", prioritarios.queue)
# print("Clientes luego:", clientes.queue)

'''
Ejemplo de parcial (diccionario):
En cada cuatrimestre se almacena en un diccionario las notas de todos los alumnos, 
de tal forma que las claves del diccionario son los nombres de los alummnos que 
cursaron ese cuatrimestre, y sus valores son la nota final que obtuvieron. 
Se desea saber cuántos alumnos que tuvieron que recursar, porque no aprobaron en 
el primer cuatrimestre, finalmente aprobaron en el segundo cuatrimestre. La nota 
para aprobar la materia es 7 o superior, y la materia se puntúa de 0 a 10.
 
problema recursantesAprobados (in cuat1: Diccionario⟨String,Z⟩, in cuat2: Diccionario⟨String,Z⟩): Z {
  requiere: { Cada diccionario de cuatrimestre tiene como valores posibles la nota de 0 a 10}
  requiere: { Si existe una clave que está en cuat1 y cuat2 entonces el valor en cuat1 
              es menor a 7}
  asegura: { res es la cantidad de claves que están cuat1 y cuat2, para cuyo valor en cuat2 
              es mayor o igual a 7}
}
 
 
Ejemplo: recursantesAprobados({'Juan': 10, 'Ana': 6, 'Pablo': 5},
 
  {'Lina': 9, 'Sol': 10, 'Pedro': 7,'Ana': 9}) debe devolver 1. 
'''

def recursantesAprobados(cuat1: dict[str, int], cuat2: dict[str, int]) -> int:
    total = 0
    for estudiante, nota in cuat1.items():
        if nota < 7 and estudiante in cuat2.keys():
            if cuat2[estudiante] >= 7:
                total += 1

    return total

# print(recursantesAprobados({'Juan': 10, 'Ana': 6, 'Pablo': 5}, {'Lina': 9, 'Sol': 10, 'Pedro': 7,'Ana': 9}))

'''
Ejercicio 2 [2,5 puntos]
 
En un supermercado tenemos una fila de clientes esperando para ser atendidos por algún cajero. Cada cliente tiene un nombre, un método de pago y una cantidad de productos. La fila de clientes se representa como una Cola de String x String x Z, donde el primer elemento es el nombre del cliente, el segundo es el método de pago y el tercero es la cantidad de productos. Implementar la función pasar_por_autoservicio:
Nota: los métodos de pago son strings conformados por letras minúsculas.
 
problema pasar_por_autoservicio (inout clientes: Cola⟨ String x String x Z ⟩) : String {
  requiere:{ Las primeras componentes de clientes son strings no vacíos y todos distintos entre sí }
  requiere:{ Las terceras componentes de clientes son números positivos }
  requiere:{ Existe al menos un elemento c dentro de la cola clientes tal que c1 ≠ "efectivo" y c2 ≤ 15 }
  modifica: { clientes }
  asegura: { Sea c el primer elemento insertado en la cola clientes tal que c1 ≠ "efectivo" y c2 ≤ 15, entonces res = c0 }
  asegura: { clientes contiene todos los elementos de clientes@pre excepto la tupla que contiene a res en su primera posición, en el mismo orden que en clientes@pre. }
}
 
Ejemplo: pasar_por_autoservicio(clientes) debe devolver "Bruno" (y quitar su tupla de la cola)
si clientes es una cola en la cual se insertaron (en orden) los siguientes elementos:
1.  ("Ana", "efectivo", 13)
2.  ("Juan", "qr", 22)
3.  ("Bruno", "tarjeta", 14)
'''

def pasar_por_autoservicio(clientes: Cola[(str, str, int)]) -> str:
    cola_aux: Cola = Cola()
    while not clientes.empty():
        cliente = clientes.get()
        if cliente[1] != "efectivo" and cliente[2] <= 15:
            res: str = cliente[0]
        else:
            cola_aux.put(cliente)

    # Reconstruyo cola original en clientes
    while not cola_aux.empty():
        clientes.put(cola_aux.get())

    return res

# clientes: Cola = Cola()
# clientes.put(("Ana", "efectivo", 13))
# clientes.put(("Juan", "qr", 22))
# clientes.put(("Bruno", "tarjeta", 14))
# clientes.put(("Carlos", "efectivo", 10))
# print(pasar_por_autoservicio(clientes))
# print(clientes.queue)

'''
Ejercicio 4 [2 puntos]
 
Se realizaron dos censos en los cuales se le preguntó a cada persona en que localidad vive. Estos datos fueron almacenados en dos diccionarios cuyas claves son los nombres de las personas, y sus valores las localidades en las cuales viven. Implementar la función mantuvieron_residencia:
 
problema mantuvieron_residencia (in censo1: Diccionario⟨String,String⟩, in censo2: Diccionario⟨String,String⟩): Diccionario⟨String,Z⟩ {
  requiere: { Las claves de censo1 son las mismas que las claves de censo2 }
  asegura: { k es clave de res si y sólo si existe alguna clave p en censo1 tal que al obtener su valor tanto en censo1 como en censo2, este es igual a k }
  asegura: { El valor de cada clave de res representa la cantidad de personas que en ambos censos vivía en esa localidad, es decir, que mantuvieron su residencia en la misma localidad entre ambos censos }
}
 
 
Ejemplo: mantuvieron_residencia({'Juan': 'Merlo', 'Ana': 'Merlo'}, {'Juan': 'Castelar', 'Ana': 'Merlo'})
 
debe devolver {'Merlo': 1}
'''

def mantuvieron_residencia(censo1: dict[str, str], censo2: dict[str, str]) -> dict[str, int]:
    res: dict[str, int] = {}
    for nombre, ciudad in censo1.items():
        if ciudad == censo2[nombre]:
            if ciudad in res:
                res[ciudad] += 1
            else:
                res[ciudad] = 1

    return res

print(mantuvieron_residencia({'Juan': 'Merlo', 'Ana': 'Merlo'}, {'Juan': 'Castelar', 'Ana': 'Merlo'}))