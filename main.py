import itertools

def ObtenerDatos():
    """Obtiene por input la matriz de costo, retorna una tupla con el conjunto
    de ciudades y la matriz"""
    return ([1,2,3],[[1, 2, 33, 3], [1, 2, 33, 4], [1, 2, 33, 4]])
    largo_matriz = int(input("INGRESE N CIDADES: "))
    filas_matriz = []
    print("INSERTE DISTANCIAS: ")
    for i in range(0,largo_matriz):
        fila = input().split()
        fila_enteros = list(map(int, fila))
        filas_matriz.append(fila_enteros)
    cjn_ciudades = list(range(1, largo_matriz))
    return (cjn_ciudades, filas_matriz)

def Subconjuntos(conjunto):
    total_sub = []
    for i in range(0, len(conjunto)+1):
        total_sub += list(itertools.combinations(conjunto, i))
    return total_sub
        
matriz = ObtenerDatos()
print(matriz[0])
Subconjuntos(matriz[0])