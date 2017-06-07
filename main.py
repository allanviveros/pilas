import itertools

def ObtenerDatos():
    """Obtiene los datos necesarios por input
    
    return: tuple(ciudades, matriz)
    list ciudades: lista de ciudades
    list[] matriz: lista de las filas (lista) de la matriz de costo
    """
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