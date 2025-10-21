# https://pastebin.com/F6GgXFjs

"""
Ejercicio 1 [2 puntos]
 Implementar la función cantidad_parejas_que_suman:
 problema cantidad_parejas_que_suman (in s: seq⟨Z⟩, in n: Z) : Z {
    requiere: { - }
    asegura: { res es la cantidad de parejas s[i] y s[j] de números de s tales que s[i] + s[j] = n (con i < j) }
 }
 
 Ejemplo: cantidad_parejas_que_suman([1,3,2,5,4,8], 5) debe devolver 2
 """

def cantidad_parejas_que_suman(s: list[int], n: int) -> int:
    total: int = 0
    for i in range(len(s)):
        for j in range(i+1, len(s)): # j es siempre mayor que i
            if n == s[i] + s[j]:
                total += 1           

    return total

# print(cantidad_parejas_que_suman([1,3,2,5,4,8], 5))
# print(cantidad_parejas_que_suman([1,3,2,5,4,8,-3], 5))

"""
3) Ejercicio 3 [2,5 puntos]
 
Implementar la función intercambiar_e_invertir_columnas:
 
problema intercambiar_e_invertir_columnas(inout A: seq⟨seq⟨Z⟩⟩, in col1: Z, in col2: Z) {
  requiere: { Todas las filas de A tienen la misma longitud (estrictamente positiva)}
  requiere: { |A| > 0}
  requiere: { 0 ≤ col1 < |A[0]| }
  requiere: { 0 ≤ col2 < |A[0]| }
  requiere: { col1 ≠ col2 }
  modifica: { A }
  asegura: { A tiene exactamente las mismas dimensiones que A@pre }
  asegura: { A[i][j] = A@pre[i][j] para todo i, j en rango tal que j ≠ col1 y j ≠ col2 }
  asegura: { A[i][col1] = A@pre[|A|-1-i][col2] para todo i tal que 0 ≤ i < |A| }
  asegura: { A[i][col2] = A@pre[|A|-1-i][col1] para todo i tal que 0 ≤ i < |A| }
}
 
 
Ejemplo: Si mat = [[1,2,3],[40,50,60], [-7,-8,-9]], luego de ejecutarse 
 intercambiar_e_invertir_columnas(mat,1,2)
 debería ocurrir que print(mat) muestre [[1, -9, -8], [40, 60, 50], [-7, 3, 2]]

 [
 [1,2,3],
 [40,50,60],
 [-7,-8,-9]
 ]
"""

def intercambiar_e_invertir_columnas(A: list[list[int]], col1: int, col2: int):
    # Itercambio columnas
    intercambiar_columnas(A, col1, col2)

    # Invierto columnas
    invertir_columna(A, col1)
    invertir_columna(A, col2)

def invertir_columna(A: list[list[int]], col: int):
    # modifica A
    for row in range(len(A)//2):
        v: int = A[row][col] # temporal
        A[row][col] = A[len(A)-row-1][col]
        A[len(A)-row-1][col] = v 

def intercambiar_columnas(A: list[list[int]], col1: int, col2: int):
    for row in range(len(A)):
        temp = A[row][col1]
        A[row][col1] = A[row][col2]
        A[row][col2] = temp

mat = [[1,2,3],[40,50,60], [-7,-8,-9]]
intercambiar_e_invertir_columnas(mat,1,2)
print(mat)