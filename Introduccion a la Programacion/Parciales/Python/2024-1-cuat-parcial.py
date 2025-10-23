from queue import Queue as Cola
"""ACLARACIONES :: 
aclaraciones este parcial NO ESTA PERFECTO, lo subo para aportar a la comunidad, la nota fue de 9.28 los ejercicios que generan conflicto son el 3 y el 4 en este ultimo el error es que no considero el caso
en el que el registro esta vacio y hago una division por 0, y en el 3 el problema es cuando la matriz es de 6*6 
"""

"""
1) Alerta Enfermedades Infecciosas (3 puntos)

Necesitamos detectar la aparición de posibles epidemias. Para esto contamos con un lista de enfermedades infecciosas y los registros de atención por guardia dados por una lista expedientes. Cada expediente es una tupla con ID paciente y enfermedad que motivó la atención. Debemos devolver un diccionario cuya clave son las enfermedades infecciosas y su valor es la proporción de pacientes que se atendieron por esa enfermedad. En este diccionario deben aparecer solo aquellas enfermedades infecciosas cuya proporción supere cierto umbral.

problema alarma_epidemiologica (registros: seq⟨ZxString⟩, infecciosas: seq⟨String⟩, umbral: R) : dict⟨String,R⟩ {
  requiere: {0 < umbral < 1}
  asegura: {claves de res pertenecen a infecciosas}
  asegura: {Para cada enfermedad perteneciente a infecciosas, si el porcentaje de pacientes que se atendieron por esa enfermedad sobre el total de registros es mayor o igual al umbral, entonces res[enfermedad] = porcentaje}
  asegura: {Para cada enfermedad perteneciente a infecciosas, si el porcentaje de e pacientes que se atendieron por esa enfermedad sobre el total de registros es menor que el umbral, entonces enfermedad no aparece en res}
}
"""

def alarma_epidemiologica_carlos(registros: list[tuple[int, str]], infecciosas: list[str], umbral: float) -> dict[str, float]:
  res: dict[str, float] = {}
  for enfermedad in infecciosas:
    p = calcular_porcentaje(registros, enfermedad)
    if p >= umbral:
      res[enfermedad] = p

  return res

def calcular_porcentaje(registros, enfermedad):
  total = len(registros)
  cant = 0
  for i in range(total):
    if registros[i][1] == enfermedad:
      cant += 1

  if total == 0:
    p = 0
  else:
    p = cant/total

  return p

# registros = [
#   (1, "viruela"),
#   (2, "viruela"),
#   (3, "covid19"),
#   (4, "covid19"),
#   (5, "covid19"),
#   (6, "viruela"),
#   (7, "covid19"),
#   (8, "salmonela"),
#   (9, "covid19"),
# ]
# registros = []

# infecciosas = ["viruela", "covid19", "salmonela", "otro"]
# infecciosas = []

# umbral = 0.5

# print(alarma_epidemiologica_carlos(registros, infecciosas, umbral))



def porcentaje_infeccion (enfermadad: str, resgistro:list[tuple[int, str]]) -> float: 
  cantidad_personas : int = 0
  for infeccion in resgistro: 
    if infeccion[1] == enfermadad: 
      cantidad_personas += 1
  porcentaje : float = ((cantidad_personas / len(resgistro)))
  return porcentaje




def alarma_epidemiologica (registros: list[tuple[int, str]], infecciosas: list[str], umbral: float) -> dict[str, float]:
  res : dict[str,float] = {}
  i : int = 0 
  for enfermadad in infecciosas: 
    if enfermadad not in res : 
      if porcentaje_infeccion(enfermadad,registros) >= umbral: 
        res[enfermadad] = porcentaje_infeccion(enfermadad,registros)
  return res 

"""
2) Orden de atención (1 punto)

Desde el Hospital Fernandez nos pidieron solucionar una serie de problemas relacionados con la información que maneja sobre los pacientes y el personal de salud. En primer lugar debemos resolver en qué orden se deben atender los pacientes que llegan a la guardia. En enfermería, hay una primera instancia que clasifica en dos colas a los pacientes: una urgente y otra postergable (esto se llama hacer triage). A partir de dichas colas que contienen la identificación del paciente, se pide devolver una nueva cola según la siguiente especificación.

problema orden_de_atencion ( in urgentes: cola⟨Z⟩, in postergables: cola⟨Z⟩) : cola⟨Z⟩ {
  requiere: {no hay elementos repetidos en urgentes}
  requiere: {no hay elementos repetidos en postergables}
  requiere: {la intersección entre postergables y urgentes es vacía}
  requiere: {|postergables| = |urgentes|}
  asegura: {no hay repetidos en res }
  asegura: {res es permutación de la concatenación de urgentes y postergables}
  asegura: {Si urgentes no es vacía, en tope de res hay un elemento de urgentes}
  asegura: {En res no hay dos seguidos de urgentes}
  asegura: {En res no hay dos seguidos de postergables}
  asegura: {Para todo c1 y c2 de tipo "urgente" pertenecientes a urgentes si c1 aparece antes que c2 en urgentes entonces c1 aparece antes que c2 en res}
  asegura: {Para todo c1 y c2 de tipo "postergable" pertenecientes a postergables si c1 aparece antes que c2 en postergables entonces c1 aparece antes que c2 en res}
"""

def orden_de_atencion(urgentes: Cola[int], postergables: Cola[int]) -> Cola[int]:
  urgentes_aux = Cola()
  postergables_aux = Cola()

  res: Cola[int] = Cola()

  while not urgentes.empty():
    elem_en_urgente = urgentes.get()
    res.put(elem_en_urgente)
    urgentes_aux.put(elem_en_urgente)

    elem_en_postergable = postergables.get()
    res.put(elem_en_postergable)
    postergables_aux.put(elem_en_postergable)

  # Reconstruyo colas originales
  while not urgentes_aux.empty():
    urgentes.put(urgentes_aux.get())
    postergables.put(postergables_aux.get())

  return res





def orden_de_atencion (urgentes: Cola[int], postrgables: Cola[int]) -> Cola[int]:
  urgentes_copia = urgentes
  postrgables_copia = postrgables
  lista_pos : list[int] = []
  lista_urg : list[int] = []
  nueva_cola : Cola[int] = Cola()
  while not urgentes_copia.empty(): 
    lista_urg.append(urgentes_copia.get())
    lista_pos.append(postrgables_copia.get())
  for i in range(0,len(lista_pos)): 
    nueva_cola.put(lista_urg[i])
    nueva_cola.put(lista_pos[i]) 
  for urg in lista_urg : 
    urgentes.put(urg)
  for pos in lista_pos: 
    postrgables.put(pos)
  return nueva_cola


"""
3) Camas ocupadas en el hospital (2 puntos)
Queremos saber qué porcentaje de ocupación de camas hay en el hospital. El hospital se representa por una matriz en donde las filas son los pisos, y las columnas son las camas. Los valores de la matriz son booleanos que indican si la cama está ocupada o no. Si el valor es verdadero (True) indica que la cama está ocupada. Se nos pide programar en Python una función que devuelve una secuencia de enteros, indicando la proporción de camas ocupadas en cada piso.

problema nivel_de_ocupacion(camas_por_piso:seq⟨seq⟨Bool⟩⟩) : seq⟨R⟩ {
  requiere: {Todos los pisos tienen la misma cantidad de camas.}
  requiere: {Hay por lo menos 1 piso en el hospital.}
  requiere: {Hay por lo menos una cama por piso.}
  asegura: {|res| = |camas|}
  asegura: {Para todo 0<= i < |res| se cumple que res[i] es igual a la cantidad de camas ocupadas del piso i dividido el total de camas del piso i)}
}
"""

def nivel_de_ocupacion_carlos(camas_por_piso: list[list[bool]]) -> list[float]:
  res: list[float] = []
  for piso in camas_por_piso:
    p = calcular_porcentaje_ocupacion_en_piso(piso)
    res.append(p)

  return res

def calcular_porcentaje_ocupacion_en_piso(piso: list[bool]) -> float:
  total: int = len(piso)
  contador: int = 0
  for cama in piso:
    if cama:
      contador += 1

  porcentaje: float
  if total > 0:
    porcentaje = contador / total
  else:
    porcentaje = 0

  return porcentaje

# print(nivel_de_ocupacion_carlos([[True, False, True], [True, True, True], [False, False, False]])) # [0.67, 1, 0]


def nivel_de_ocupacion(camas_por_piso:list[list[bool]]) -> list[float]:
  res : list[float] = []
  contador : int = 0
  cantidad_camas = len(camas_por_piso)
  for fila in range(0,len(camas_por_piso)) : 
    for elem in range(0,len(camas_por_piso)):
      if camas_por_piso[fila][elem] == True:
        contador += 1
    res.append(contador/cantidad_camas)
    contador = 0
  return res  

"""
4) Quiénes trabajaron más? (2 puntos)
Dado un diccionario con la cantidad de horas trabajadas por empleado, en donde la clave es el ID del empleado y el valor es una lista de las horas trabajadas por día, queremos saber quienes trabajaron más para darles un premio. Se deberá buscar la o las claves para la cual se tiene el máximo valor de cantidad total de horas, y devolverlas en una lista.

problema empleados_del_mes(horas:dicc⟨Z,seq⟨Z⟩⟩) : seq⟨Z⟩ {
  requiere: {No hay valores en horas que sean listas vacías}
  asegura: {Si ID pertence a res entonces ID pertence a las claves de horas}
  asegura: {Si ID pertenece a res, la suma de sus valores de horas es el máximo de la suma de elementos de horas de todos los otros IDs}
  asegura: {Para todo ID de claves de horas, si la suma de sus valores es el máximo de la suma de elementos de horas de los otros IDs, entonces ID pertences a res}
}


}
"""

def empleados_del_mes_carlos(horas: dict[int, list[int]]) -> list[int]:
  # res: list[int] = []
  maximo_hasta_ahora: int = 0
  maximos_id: list[int] = []
  for id, horas_por_dia in horas.items():
    s = suma_lista(horas_por_dia)
    if s > maximo_hasta_ahora:
      maximo_hasta_ahora = s
      maximos_id = [id]
    elif s == maximo_hasta_ahora:
      maximos_id.append(id)

  return maximos_id

def suma_lista(s: list[int]) -> int:
  total: int = 0
  for n in s:
    total += n

  return total

# horas = {
#   1: [1],
#   2: [5,7,9,14,15],
#   3: [1,2,3],
#   4: [4,4,4,4],
#   5: [1,1],
#   6: [9,7,5,14,15],
#   7: [1,1,1,2],
#   8: [50],
# }

# print(empleados_del_mes_carlos(horas)) # [2, 6, 8]


def suma_total (s:list) -> int: 
  suma : int = 0
  for num in s : 
    suma += num
  return suma

def mayor1 (s:list[int])-> int : 
  mayor : int = 0
  for num in s : 
    if num > mayor:
      mayor = num
  return mayor

def mayor(s:list[int]) -> list[int] : 
  mayor : int = mayor1(s) - 1
  res : list[int] = []
  for i in range(0,len(s)): 
    if s[i] > mayor: 
      res.append(i)
  return res

def empleados_del_mes(horas:dict[int, list[int]]) -> list[int]:
  res : list[int] = []
  sumas : list[int] =[]
  lista_ids : list[int] = []
  for ids in horas.keys():
    lista_ids.append(ids)
  for ids in horas.keys():
    horas_trabajadas = horas[ids]
    sumas.append(suma_total(horas_trabajadas))
  mas_horas = mayor(sumas)
  for i in range (0,len(mas_horas)):
      res.append(lista_ids[mas_horas[i]])
  return res 

