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

def Subconjuntos(conjunto):
    """retorna todos los subconjuntos y sus rutas

    return: list(rutas)
    list rutas
    """
    total_sub = []
    for i in range(0, len(conjunto)+1):
        if i == len(conjunto):
            total_sub.append([0,list(conjunto)])
            break
        sub = list(itertools.combinations(conjunto, i))
        for j in sub:
            for m in conjunto:
                if m not in j:
                    total_sub.append([m,list(j)])
    return total_sub

def RutaOptima(ruta,nodo_final):
    #print("**"+str(Llave([ruta[0],ruta[1:]]))+" "+str(Llave(ruta) in valores_guardados))
    if Llave([ruta[0],ruta[1:]]) in valores_guardados:
        return True
    return False

def ReducirDiccionario(nodo):
    pass

def ObtenerSolucion(ultimo):
    largo_string = len(ultimo)
    resultado = []
    resultado.append(nodo_inicial)
    data = valores_guardados[ultimo]
    costo_total = data[0]
    resultado.append(data[1])
    largo_string -= 3
    #print(len(conjunto_ciudades) + 1)

    #print(ultimo)
    #print(largo_string)
    costo_min = []
    nodo_min = []
    while len(resultado) != len(conjunto_ciudades) + 1:
        for llaves, valor in valores_guardados.items():
            
            #print(llaves)
            ##print(largo_string)
            if len(llaves) == largo_string and valor[1] not in resultado:
                #print(llaves)
                #print(llaves[-2])
                valor_min = valor[0]
                nodo_minimo = llaves[-2]
                costo_min.append(int(valor_min))
                nodo_min.append(nodo_minimo)
                #resultado.append(int(llaves[-2]))
        print(costo_min)
        print(nodo_min)
        
        indice_min = costo_min.index(min(costo_min))
        print(indice_min)
        print(nodo_min[indice_min])
        print('')
        resultado.append(int(nodo_min[indice_min]))
        largo_string -=3
                #break
                #print()
        
    resultado.append(nodo_inicial)
    print(resultado)
    
            

def Permutaciones(ruta):
    nodo_final = ruta[0]
    conjunto = ruta[1]
    lista_costo = []
    lista_nodos_ant = []
    lista_rutas = []
    if len(conjunto) <= 1:
        #costo = CalcularCostoRuta(ruta)
        #nodo_ant = 0
        #if len(conjunto) == 1:
        #    nodo_ant = conjunto[0]
        costo, nodo_ant = CalcularCostoRuta(ruta)
        #print(costo)
        Guardar(ruta,costo,nodo_ant)
    else:
        rutas_posibles = []
        permutaciones_rutas = list(itertools.permutations(conjunto))
        #print(permutaciones_rutas) #[(),()]
        for rutas in permutaciones_rutas:
            if RutaOptima(list(rutas),nodo_final):
                rutas_posibles.append(rutas)
        print("rutas pos: "+str(rutas_posibles))
        for ruta in rutas_posibles:
            #print("** "+str(ruta))
            costo, nodo_ant = CalcularCostoRuta([nodo_final, list(ruta)])
            lista_nodos_ant.append(nodo_ant)
            lista_costo.append(costo)
            lista_rutas.append(ruta)
        minimo = min(lista_costo)
        indice_minimo = lista_costo.index(minimo)
        #print("-"+str(conjunto))
        #print("--"+str(Llave(conjunto)))
        Guardar([nodo_final,conjunto], lista_costo[indice_minimo],lista_nodos_ant[indice_minimo])

def Llave(ruta):
    return str(ruta[0])+"/"+str(ruta[1])

def Guardar(ruta, costo,nodo_ant):
    llave = Llave(ruta)
    valores_guardados[llave] = (costo, nodo_ant)

def Cargar(ruta):
    llave_anterior = Llave(ruta)
    if llave_anterior in valores_guardados:
        #print("hay un dato guardado")
        return (True, valores_guardados[llave_anterior])
        #valores_guardados[llave_actual] = costo
    else:
        #print("no hay dato guardado de "+ llave_anterior+", procedo a calcular")
        #print(valores_guardados)
        #CalcularCostoRuta(lista_nodos[0],lista_nodos[1:])
        return (False, 0)



def CalcularCostoRuta(ruta):
    nodo_final = ruta[0]
    lista_nodos = ruta[1]
    if len(lista_nodos) == 0:
        ##llave_actual = Llave(ruta)
        costo = matriz[nodo_inicial][nodo_final]
        ##valores_guardados[llave_actual] = costo
        return (costo, nodo_inicial)
    costo = matriz[lista_nodos[0]][nodo_final]
    ruta_previa = [lista_nodos[0],lista_nodos[1:]]
    estado_previo = Cargar(ruta_previa)
    if estado_previo[0]:
        data_guardada = estado_previo[1]
        return (costo + data_guardada[0], lista_nodos[0])
    else:
        print("algo salio mal")
        #print(Llave(ruta_previa))
        #print(valores_guardados)

nodo_inicial = 0
"""
matriz = [[0, 1, 15, 6], [2, 0, 7, 3], [9, 6, 0, 12],[10, 4, 8, 0]]
conjunto_ciudades = set([1,2,3])
"""
""""
matriz = [[0, 119, 15, 64, 17], [119, 0, 12, 19, 122], [15, 12, 0, 47, 23],[64, 19, 47, 0, 115],[17, 122, 23, 115, 0]]
conjunto_ciudades = set([1,2,3,4])
"""
"""
0 119 15 64 17
119 0 12 19 122
15 12 0 47 23
64 19 47 0 115
17 122 23 115 0
"""

conjunto_ciudades, matriz = ObtenerDatos()


#CostoRuta(nodo_inicial,set([1,2]))


subconjuntos = Subconjuntos(conjunto_ciudades)
#print(subconjuntos)

#Permutaciones(3,[1,2])

valores_guardados = {'2/()': 15, '1/[2]': 15} # llave: (costo, nodo)
valores_guardados = {}
#CalcularCostoRuta([2,[]]) #3,[1,2]

#print(subconjuntos)

#CalcularRuta([2,()])

"""
for ruta in subconjuntos:
    print("* "+str(Llave(ruta)))
    CalcularCostoRuta(ruta)
print(valores_guardados)
"""

for i in range(0,len(subconjuntos)):
    if len(subconjuntos[i][1]) == len(subconjuntos[-1][1]):
        #print()
        #break
        ultimo = Llave(subconjuntos[i])
        print(subconjuntos[i])
        #print("aqui esta "+ultimo)
        pass
    #print("* "+str(subconjuntos[i]))
    Permutaciones(subconjuntos[i])
print(valores_guardados)

ObtenerSolucion(ultimo)


