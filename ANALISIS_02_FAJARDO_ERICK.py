# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
"""
Proyecto 2 Introducción al análisis de datos

Alumno: Erick Gabriel Fajardo Martínez

Correo: erickfama@outlook.es
"""

### Cargar base de datos

import csv

df = []
with open("synergy_logistics_database.csv", "r") as dat:
    lector = csv.reader(dat)
    for columna in lector:
        df.append(columna)

df_dicc = []
with open("synergy_logistics_database.csv", "r") as dat:
    diccionario = csv.DictReader(dat)
    for columna in diccionario:
        df_dicc.append(columna)

# Se crea una lista con los nombres de las variables
nombres = list(dict.keys(df_dicc[0]))

# Función para extraer cualquier valor del df
def extraer(lista, clave_extraer):
    for elemento in df_dicc:
        lista.append(elemento[clave_extraer])
        
# función extraer con condición de importación/exportación

def extraer_ruta(lista, condicion = "Imports"):
    for elemento in df_dicc:
        if elemento["direction"] == condicion:
            ruta = str(elemento["origin"]) + "-" + str(elemento["destination"])
            lista.append(ruta)

# Función para obtener los valores únicos de una lista
def unico(lista):
    check = []
    for valor in lista:
        if valor not in check:
            check.append(valor)
    return check

# función para unir dos listas

def unir_listas(lista1, lista2):
    lista_final = []
    sublist = []
    n = 0
    while len(lista_final) < len(lista1):
        sublist.append(lista1[n])
        while len(sublist) == 1:
            sublist.append(lista2[n])
            if len(sublist) == 2:
                lista_final.append(sublist)
                n += 1
                sublist = []
    lista_final.sort(key = lambda elemento: elemento[1], reverse = True)
    return lista_final

# Función contar las veces que se repite un valor
        
def numero_repite(lista):
    check = unico(lista)
    count_list = []
    n = 0
    count = 0
    for valor in check:
        for elemento in lista:
            n += 1
            if valor == elemento:
                count += 1
            else:
                continue
        if n == len(lista):
            count_list.append(count)
            count = 0
            n = 0
        if len(count_list) == len(check):
            variable_veces = unir_listas(check, count_list)
            for i in range(0, len(variable_veces)):
                print(variable_veces[i][0] + ": " + str(variable_veces[i][1]))
    return variable_veces
        
# Función que extrae los x valores más altos de una lista

def x_valores_max(lista, mostrar = 10):
    check = []
    count_list = []
    paises = []
    n = 0
    count = 0
    for valor in lista:
        if valor not in check:
            check.append(valor)
    for valor in check:
        paises.append(valor)
        for elemento in lista:
            n += 1
            if valor == elemento:
                count += 1
            else:
                continue
        if n == len(lista):
            count_list.append(count)
            count = 0
            n = 0
        if len(count_list) == len(check):
            max10 = []
            max10 = unir_listas(paises, count_list)
            print("Estos son los 10 valores máximos:")
            for i in range(0, mostrar):
                print(max10[i][0] + ":" + str(max10[i][1]))
    return max10
        

# función que obtiene el valor total de las rutas 
                    
def valor_total_ruta(rutas, condicion, mostrar = 10):
    n = 0
    total_ruta = []
    valor_total = []
    rutas_unicas = unico(rutas)
    ruta_valor = []
    for x in rutas_unicas:
        for elemento in df_dicc:
            n += 1
            if elemento["direction"] == condicion:
                ruta = elemento["origin"] + "-" + elemento["destination"]
                valor = elemento["total_value"]
                if x == ruta:
                    total_ruta.append(int(valor))
            if n == len(df_dicc):
                valor_total.append(sum(total_ruta))
                total_ruta = []
                n = 0
            if len(valor_total) == len(rutas_unicas):
                ruta_valor = unir_listas(rutas_unicas, valor_total)
                print("Estos son las 10 rutas con los mejores valores totales:")
                for i  in range(0, mostrar):
                    print(ruta_valor[i][0] + ":" + str(ruta_valor[i][1]))
                return ruta_valor
            
    n = 0
    total_ruta = []
    valor_total = []
    rutas_unicas = unico(exportaciones)
    ruta_valor = []
    for x in rutas_unicas:
        for elemento in df_dicc:
            n += 1
            if elemento["direction"] == "Exports":
                ruta = elemento["origin"] + "-" + elemento["destination"]
                valor = elemento["total_value"]
                if x == ruta:
                    total_ruta.append(int(valor))
            if n == len(df_dicc):
                valor_total.append(sum(total_ruta))
                total_ruta = []
                n = 0
            if len(valor_total) == len(rutas_unicas):
                ruta_valor = unir_listas(rutas_unicas, valor_total)
                print("Estos son las 10 rutas con los mejores valores totales:")
                for i  in range(0, 10):
                    print(ruta_valor[i][0] + ":" + str(ruta_valor[i][1]))
                

# Función para obtener los valores totales de cualquier variable fuera de exp/imp

def valor_total(key, mostrar = 10):
    lista_variable = []
    extraer(lista_variable, key)
    n = 0
    total_variable = []
    valor_total = []
    variable_unicas = unico(lista_variable)
    variable_valor = []
    for x in variable_unicas:
        for elemento in df_dicc:
            n += 1
            if elemento[key] == x:
                total_variable.append(int(elemento["total_value"]))
            else: 
                continue
        if n == len(df_dicc):
            valor_total.append(sum(total_variable))
            total_variable = []
            n = 0
        if len(valor_total) == len(variable_unicas):
            variable_valor = unir_listas(variable_unicas, valor_total)
            for i  in range(0, mostrar):
                print(variable_valor[i][0] + ": " + str(variable_valor[i][1]))
    return variable_valor

# función para obtener proporciones

def prop(lista, mostrar = 3):
    cantidades = []
    proporciones = []
    for valor in lista:
        cantidades.append(int(valor[1]))
    for valor in lista:
        proporcion = (int(valor[1])/sum(cantidades))*100
        proporciones.append(round(proporcion, 2))
    print("""
Estas son las proporciones:""")
    for i in range(0, mostrar):
        print(lista[i][0] + ": " + str(proporciones[i]) + "%")

                    
### OPCION 1 -------------------------------------------------------------------

print("""
######### OPCION 1 ############################################################
      """)

### Extraer rutas de Exportaciones ---------------------------------------------
print("""
######### Exportaciones
      """)
exportaciones = []
extraer_ruta(exportaciones, "Exports") # Solo se puede usar "Exports" o "Imports"

    # 10 rutas más demandadas de exportaciones
print("""
-------- Rutas exportación demandadas ----------
      """)
prop(x_valores_max(exportaciones, mostrar = 10), mostrar = 10)

    # 10 mejores valores totales por ruta
print("""
-------- Valores Totales Exp -----------
      """)
prop(lista = valor_total_ruta(exportaciones, "Exports", mostrar = 10), mostrar = 10)


### Extraer rutas de Importaciones ----------------------------------------------
print("""
######### Importaciones
      """)
importaciones = []
extraer_ruta(importaciones, "Imports") # Solo se puede usar "Exports" o "Imports"

    # 10 rutas más demandadas de importaciones
print("""
-------- Rutas importación demandadas ----------
      """)
prop(x_valores_max(importaciones, mostrar = 10) )

    # 10 mejores valores totales por ruta
print("""
-------- Valores Totales Imp -----------
      """)
prop(valor_total_ruta(importaciones, "Imports", mostrar = 10), mostrar = 10)

### -----------------------------------------------------------------------------

### OPCION 2 --------------------------------------------------------------------

print("""
######### OPCION 2 ############################################################
      """)
# Extraer variable transporte de df_dicc
transporte = []
extraer(transporte, "transport_mode")

# Número de viajes y proporción
print(" ------ Número de viajes por transporte:")
prop(numero_repite(transporte), mostrar = 4)

# Se extraen los mejores transportes con base en el valor
print("""
 ------- Valor por transporte:""")
prop(valor_total("transport_mode", mostrar = 4), mostrar = 4)


### OPCION 3 --------------------------------------------------------------------

print("""
######### OPCION 3 ############################################################
      """)
### Origen ---------------------------
      
# Extraer países de origen de df_dicc
paises_origen = []
extraer(paises_origen, "origin")

# Países origen más populares y proporciones
print(""" ------ Países de origen más populares
      """)
prop(x_valores_max(paises_origen), mostrar = 10)

# Países origen mayor valor y proporciones
print(""" ------ Países de origen por mayor valor
      """)
prop(valor_total("origin"), mostrar = 10)

### Destino ---------------------------

# Extraer paises destino de df_dicc
paises_destino = []
extraer(paises_destino, "destination")

# Países destino más populares y proporciones
print("""
------- Países destino más populares
      """)
prop(x_valores_max(paises_destino), mostrar  = 10)

# Países destino mayor valor y proporciones
print("""
------- Países destino por mayor valor
      """)
prop(valor_total("destination"), mostrar = 10)





        
