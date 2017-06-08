import itertools

def ObtenerDatos():
    """Obtiene los datos necesarios por input
    
    return: tuple(ciudades, matriz)
    list ciudades: lista de ciudades
    list[] matriz: lista de las filas (lista) de la matriz de costo
    """
    largo_matriz = int(input("INGRESE N CIDADES: "))
    filas_matriz = []
    print("INSERTE DISTANCIAS: ")
    for i in range(0,largo_matriz):
        fila = input().split()
        fila_enteros = list(map(int, fila))
        filas_matriz.append(fila_enteros)
    cjn_ciudades = list(range(1, largo_matriz))
    return (cjn_ciudades, filas_matriz)

"""
def Subconjuntos(conjunto):
    total_sub = []
    for i in range(0, len(conjunto)+1):
        total_sub += list(itertools.combinations(conjunto, i))
    return total_sub

"""

def Subconjuntos(conjunto):
    total_sub = []
    for i in range(0, len(conjunto)+1):
        if i == len(conjunto):
            #print("aqui va el 0")
            total_sub.append([0,tuple(conjunto)])
            break
        sub = list(itertools.combinations(conjunto, i))
        for j in sub:
            for m in conjunto:
                if m not in j:
                    total_sub.append([m,j])
                    #print(total_sub)
        #print(sub)
    return total_sub

def CalcularRuta(data):
    nodo_ir = data[0]
    conj = data[1]
    llave = str(nodo_ir)+"/"+str(conj)
    if llave in valores_guardados:
        costo = valores_guardados[llave]
        print("hecho por diccionario")
    else:
        costo = matriz[nodo_inicial][nodo_ir]
        print(costo)
        print("hecho por matriz")
    valores_guardados[llave] = costo
    print(valores_guardados)

nodo_inicial = 0    
matriz = [[0, 1, 15, 6], [2, 0, 7, 3], [9, 6, 0, 12],[10, 4, 8, 0]]
conjunto_ciudades = [1,2,3]
#print(matriz[0])
subconjuntos = Subconjuntos(conjunto_ciudades)
valores_guardados = {'2/()': 15}

#print(subconjuntos)

CalcularRuta([2,()])
"""
for i in subconjuntos:
    print(len(i))
    if len(i) == 1:
        print(i[0])
        print('')
    elif len(i) == 2:
        print(str(i[0])+' '+str(i[1]))
        print('')
    else:
        print(i)
        print('')
        """