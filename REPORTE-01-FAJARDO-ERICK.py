# -*- coding: utf-8 -*-
"""
Proyecto 1 Introducción a Python

Alumno: Erick Gabriel Fajardo Martínez
"""

# - Consigna 1: Productos más vendidos y productos rezagados - #

# Cargar listas del archivo lifestore_file.py

from lifestore_file import *

"""
lifestore-searches = [id_search, id product]
lifestore-sales = [id_sale, id_product, score (from 1 to 5), date, refund (1 for true or 0 to false)]
lifestore-products = [id_product, name, price, category, stock]
"""

##############################################################################

### ------------------------- Ventas de productos ------------------------ ###

product_sold = [] 
for n in range(0, len(lifestore_sales)): # Se extraen los ID de los productos en las búsquedas
    product_sold.append(lifestore_sales[n][1])

id_product_sold = [] # Se filtran los id únicos de los productos vendidos
for product1 in lifestore_products:
    if product1[0] in product_sold:
            id_product_sold.append(product1[0])

# Contabilizar el número total de ventas por ID
count = 0
control = [0]
number_product_sold = []
for product in lifestore_products: 
    i = product[0]
    for sale in product_sold:
        if i == sale:
            count += 1
            control.append(count)
        else: 
            count = 0
    if count == 0 and max(control) != 0 or i == 94: 
        number_product_sold.append(max(control))
    control = [0]
if len(number_product_sold) == len(id_product_sold):
    count = 0
    control = [0]
    print("Correcto: Los valores máximos de la venta de cada producto se extrajeron correctamente")
else:
    print("Algo salió mal")

# Promedio de ventas
mean_sales = sum(number_product_sold)/len(number_product_sold)


# Unir cada ID buscado con su cantidad de ventas
A_products_sales = [] # En esta lista el indice [0] <- ID y [1] <- Cantidad de ventas
sublist = []
n = 0
while len(sublist) == 0:
    sublist.append(id_product_sold[n])
    while len(sublist) == 1:
        sublist.append(number_product_sold[n])
        while len(sublist) == 2:
            n += 1
            A_products_sales.append(sublist)
            sublist = []
    if n == len(id_product_sold):
        print("B_products_sales contiene el listado de los productos vendidos con su número de ventas")
        break
    
# Juntar categorías con ventas B_product_sales

for product1 in lifestore_products:
    for product2 in A_products_sales:
        if product1[0] == product2[0]:
            product2.append(product1[3])
            count += 1
    if count == len(A_products_sales):
        count = 0
        print("Las categorías se añadieron correctamente a las ventas")
        
# Juntar reseña promedio con ventas B_product_sales

score = []
for product1 in A_products_sales:
    for product2 in lifestore_sales:
        if product1[0] == product2[1]:
            count += 1
            score.append(product2[2])
        else:
            count = 0
    if count == 0 or product1[0] == 94:
        product1.append(sum(score)/len(score))
    score = []
        
##############################################################################

### Búsquedas de productos

product_search = [] 
for n in range(0, len(lifestore_searches)): # Se extraen los ID de los productos en las búsquedas
    product_search.append(lifestore_searches[n][1])

id_product_search = []
for product in lifestore_products: # Se filtran los ID sin repetir
        if product[0] in product_search:
            id_product_search.append(product[0])

# Contabilizar el número total de búsquedas por ID
number_product_search = [] 
for product in id_product_search: 
    i = product
    for search in product_search:
        if i == search:
            count += 1
            control.append(count)
        else:
            count = 0
    if count == 0 or i == max(id_product_search):
        number_product_search.append(max(control)) # Se agrega el número máximo de la búsqueda n por cada producto n
    control = [0]
if len(id_product_search) == len(number_product_search):
    count = 0
    print("Correcto: Los valores máximos de la búsqueda de cada producto se extrajeron correctamente")
else:
    print("Algo salió mal")

# Promedio de búsquedas
mean_search = sum(number_product_search)/len(number_product_search)

# Unir cada ID buscado con su cantidad de búsqueda
B_products_search = [] # En esta lista el indice [0] <- ID y [1] <- Cantidad de búsquedas
sublist = []
n = 0
while len(sublist) == 0:
    sublist.append(id_product_search[n])
    while len(sublist) == 1:
        sublist.append(number_product_search[n])
        while len(sublist) == 2:
            n += 1
            B_products_search.append(sublist)
            sublist = []
    if n == len(id_product_search):
        print("B_products_search contiene el listado de los productos con su número de búsquedas")
        break

# Juntar categorías con búsquedas B_products_search

for product1 in lifestore_products:
    for product2 in B_products_search:
        if product1[0] == product2[0]:
            product2.append(product1[3])
            count += 1
    if count == len(B_products_search):
        count = 0
        print("Las categorías se añadieron correctamente a las ventas")
        
##############################################################################

### --------------------- Reseñas por producto ------------------ ###

# Mejores reseñas
print("Estos son los id de los productos con mejor reseña (score >= 3):")
print("ID, Score")
for product in A_products_sales:
    if product[3] > 3:
        print([product[0], int(product[3])])
        
        
# Peores reseñanas
print("Estos son los id de los productos con peor reseña (score >= 3):")
print("ID, Score")
for product in A_products_sales:
    if product[3] <= 3:
        print([product[0], int(product[3])])
        
##############################################################################

### --------------------- Resumen de Ingresos -------------------- ###

# Total de ingresos


all_month_sales = [] # Se extrae una lista con el mes de cada venta
for date in lifestore_sales:
    all_month_sales.append(int(date[3][3:5]))
    
month_sales = []    
for month in range(1, 13): # Se extraen los meses sin repetir
        if month in all_month_sales:
            month_sales.append(month)
  

total_month_sales = []
n = 0
for month in month_sales: # Se contabiliza las veces que se repite cada mes
    for date in all_month_sales:
        n += 1
        if month == date:
            count += 1
            control.append(count)
        if n == len(all_month_sales):
            count = 0
    if count == 0 or i == 11:
        n = 0
        total_month_sales.append(max(control))
    control = [0]

# Agregar meses a ventas
dates_sales = []
n = 0
while len(sublist) == 0:
    sublist.append(month_sales[n])
    while len(sublist) == 1:
        sublist.append(total_month_sales[n])
        while len(sublist) == 2:
            n += 1
            dates_sales.append(sublist)
            sublist = []
    if len(month_sales) == len(dates_sales):
        print("Fecha de venta agregada al total de ventas")
        n = 0
        break


n = 0
id_month = []
while len(sublist) == 0:
    sublist.append(product_sold[n])
    while len(sublist) == 1:
        sublist.append(all_month_sales[n])
        while len(sublist) == 2:
            n += 1
            id_month.append(sublist)
            sublist = []
    if len(id_month) == len(lifestore_sales):
        print("Fecha de venta por ID extraída correctamente.")
        n = 0
        break

id_price_month = [] # Cada lista corresponde al mes en la lista month_sales
for month in month_sales:
    for date in id_month:
        n += 1
        if date[1] == month:
            sublist.append(date[0])
    if n == len(id_month):
        id_price_month.append(sublist)
        sublist = []
        n = 0

for product1 in A_products_sales: # Se agrega el precio a los productos vendidos
    for product2 in lifestore_products:
        if product1[0] == product2[0]:
            product1.append(product2[2])

C_month_income = [] # Se agregan los precios de los ID vendidos en cada mes 
for month in id_price_month:
    for i in month:
        n += 1
        for product in A_products_sales:
            if product[0] == i:
                sublist.append(product[4])
    if n == len(month):
        C_month_income.append(sublist)
        sublist = []
        n = 0
if len(C_month_income) == len(month_sales):
    print("Correcto: Ingreso por mes extraído exitosamente")

total_month_income = [] # Se suman los ingresos por mes
for month in C_month_income:
    total = sum(month)
    total_month_income.append(total)

C_total_month_income = []
n = 0
sublist = []
while len(sublist) == 0:
    sublist.append(month_sales[n])
    while len(sublist) == 1:
        sublist.append(total_month_income[n])
        while len(sublist) == 2:
            n += 1
            C_total_month_income.append(sublist)
            sublist = []
    if len(month_sales) == len(C_total_month_income):
        n = 0
        break

D_id_refund = [] # Se integran las devoluciones con sus precios
for product in lifestore_sales:
    if product[4] == 1:
        sublist.append(product[1])
    if len(sublist) == 1:
        D_id_refund.append(sublist)
        sublist = []
for refund in D_id_refund:
    for product in A_products_sales:
        if refund[0] == product[0]:
            refund.append(product[4])
            
###############################################################################

### ---------------------- Login -------------------------------------------###
users_passwords = [["Javier", "lepondre10"], ["Erick", "pongame10"], ["Emtech", "datascience"], ["q", "q"]]


menu_principal = """
                MENU PRINCIPAL

¿Qué desea desplegar?
      
1. Productos más vendidos y productos rezagados
2. Productos por reseña en el servicio
3. Reporte de Ingresos
4. Salir
---------------------------------------------------------------------
"""

menu_ventas = """
                MENU DE VENTAS

¿Qué desea conocer?

1. Productos vendidos
2. Productos con mayores ventas por categoría
3. Productos con menores ventas por categoría
4. Productos buscados
5. Productos con mayores búsquedas por categoría
6. Productos con menores búsquedas por categoría
0. Regresar
---------------------------------------------------------------------
"""

menu_reseñas = """
                MENU DE RESEÑAS

¿Qué desea conocer?

1. Productos con mejores reseñas
2. Productos con peores reseñas
0. Regresar
---------------------------------------------------------------------
"""

menu_ingresos = """
                MENU DE INGRESOS

¿Qué desea conocer?

1. Total de ingresos (Anual)
2. Ingreso total mensual
3. Ingreso promedio mensual
4. Ventas totales anuales
5. Ventas promedio mensuales
6. Meses con mayores ventas
7. Meses con mayores ingresos
0. Regresar
---------------------------------------------------------------------
"""


print( """
      ¡Bienvenido a Lifestore! 
      
      Por favor, inicie sesión.
      """)

usuario = input("Usuario: ")
contraseña = input("Contraseña: ")
login = [usuario, contraseña]
login_control = 0

while login_control == 0:
    if login in users_passwords:
        print("Hola de nuevo " + usuario + "!")
        login_control = 1
        principal = 1
    else:
        print("Usuario o contraseña incorrectos.")
        break

    while principal == 1:
        print(menu_principal)
        principal = 0
        opcion_principal = int(input("Introduzca el número de la opción correspondiente: "))
        while principal == 0:
            # ------------------- ventass -----------------------#
            if opcion_principal == 1:
                print(menu_ventas)
                opcion_ventas = int(input("Introduzca el número de la opción correspondiente: "))
                if opcion_ventas == 1: # opcion 1 productos vendidos
                    print("""
        ---------------------------------------------------------------------
        Estos son los productos vendidos:
        ID, Número de ventas""")
                    for i in range(0, len(A_products_sales)):
                        print(A_products_sales[i][0:2])
                if opcion_ventas == 2: # opcion 2 productos con mayores ventas por categoría
                    print("""
        ---------------------------------------------------------------------
        Estos son los productos con mayores ventas por categoría:
        ID, Número de ventas, Categoría""")
                    for i in range(0, len(A_products_sales)):
                        sale = A_products_sales[i][0:3]
                        if sale[1] > mean_sales:
                            print(sale)
                if opcion_ventas == 3: # opcion 3 productos con menores ventas por categoría
                    print("""
        ---------------------------------------------------------------------
        Estos son los productos con menores ventas por categoría:
        ID, Número de ventas, Categoría""")
                    for i in range(0, len(A_products_sales)):
                        sale = A_products_sales[i][0:3]
                        if sale[1] <= mean_sales:
                            print(sale)
                if opcion_ventas == 4: # opcion 4 productos buscados
                    print("""
        ---------------------------------------------------------------------
        Estos son los productos buscados:
        ID, Número de búsquedas""")
                    for i in range(0, len(B_products_search)):
                        print(B_products_search[i][0:2])
                if opcion_ventas == 5: # opcion 5 productos con mayores busquedas por categoría
                    print("""
        ---------------------------------------------------------------------
        Estos son los productos con mayores búsquedas por categoría:
        ID, Número de búsquedas, Categoría""")
                    for i in range(0, len(B_products_search)):
                        search = B_products_search[i][0:3]
                        if search[1] > mean_search:
                            print(search)
                if opcion_ventas == 6: # opcion 6 productos con menores busquedas por categoría
                    print("""
        ---------------------------------------------------------------------
        Estos son los productos con menores búsquedas por categoría:
        ID, Número de búsquedas, Categoría""")
                    for i in range(0, len(B_products_search)):
                        search = B_products_search[i][0:3]
                        if search[1] <= mean_search:
                            print(search)
                if opcion_ventas == 0:
                    principal = 1
                # ------------------- Reseñas -----------------------#
            elif opcion_principal == 2: # Se despliega el menu de reseñas
                print(menu_reseñas)
                opcion_reseñas = int(input("Introduzca el número de la opción correspondiente: "))
                if opcion_reseñas == 1: # opcion 1 mejores reseñas
                    print("""
        ---------------------------------------------------------------------
        Estos son los productos con mejores reseñas:
        ID, Puntuación de reseña, Categoría""")
                    for i in range(0, len(A_products_sales)):
                        score = (A_products_sales[i][0:4:3])
                        if score[1] >= 3:
                            print(score)
                if opcion_reseñas == 2: # opcion 2 peores reseñas
                    print("""
        ---------------------------------------------------------------------
        Estos son los productos con peores reseñas:
        ID, Puntuación de reseña""")
                    for i in range(0, len(A_products_sales)):
                        score = (A_products_sales[i][0:4:3])
                        if score[1] < 3:
                            print(score)
                if opcion_reseñas == 0:
                    principal = 1
            # ------------------- Ingresos -----------------------#
            elif opcion_principal == 3: # Se despliega el menu de ingresos
                print(menu_ingresos)
                opcion_ingresos = int(input("Introduzca el número de la opción correspondiente: "))
                if opcion_ingresos == 1: # opcion 1 total de ingresos (anual)
                    print("""
        ---------------------------------------------------------------------
        Este fue el ingreso anual:
        Ingreso anual""")
                    print("$ " + str(sum(total_month_income)))
                if opcion_ingresos == 2: # opcion 2 total de ingresos mensuales
                    print("""
        ---------------------------------------------------------------------
        Estos fueron los ingresos mensuales:
        Mes, Ingreso""")
                    for month in C_total_month_income:
                        print(month)
                    print("No se registraron ingresos en Octubre y Diciembre")
                if opcion_ingresos == 3: # 3 Ingreso promedio mensual
                    print("""
        ---------------------------------------------------------------------
        Este fue el ingreso promedio mensual:
        Ingreso promedio""")
                    print("$" + str(sum(total_month_income)/12))
                if opcion_ingresos == 4: #  4 Ventas totales anuales
                    print("""
        ---------------------------------------------------------------------
        Estas fueron las ventas totales anuales: 
        Ventas totales""")
                    print(len(lifestore_sales))
                if opcion_ingresos == 5: #  5 Ventas promedio mensuales
                    print("""
        ---------------------------------------------------------------------
        Estas fueron las ventas totales anuales: 
        Ventas totales""")
                    print(len(lifestore_sales)/12) 
                if opcion_ingresos == 6: #  6 Meses con mayores ventas
                    print("""
        ---------------------------------------------------------------------
        Estos fueron los meses con mayores ventas: 
        Mes, Ventas""")
                    for month in dates_sales: 
                        if month[1] > len(lifestore_sales)/12:
                            print(month)
                if opcion_ingresos == 7: #  6 Meses con mayores ingresos
                    print("""
        ---------------------------------------------------------------------
        Estos fueron los meses con mayores ventas: 
        Mes, Ventas""")
                    for month in C_total_month_income: 
                        if month[1] > sum(total_month_income)/12:
                            print(month)
                if opcion_ingresos == 0:
                    principal = 1
            if opcion_principal == 4:
                print("¡Hasta luego " + usuario + "!")
                break
        