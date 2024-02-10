'''
Codigo realizado para determinar el total de ventas de un negocio que
registra en un archivo JSONel numero de productos vendidos y el precio de venta
En otro archivo diferente se maneja el inventario con el valor unitario
Usan dos Json en formato utf-8 como entrada
Se puede trabajar con numeros en formato flotante o enteros.
Se convierten negativos en su valor absoluto
Se implementa condicion para retirar productos que no esten en inventario
Parametos: requiere unicamente usar el comando python:
"nombre_archivo.py product_list.json sales.json"
LUIS ALFONSO SABANERO ESQUIVEL A01273286
ENERO 2024
'''
import sys
import json
import time
from tabulate import tabulate
tiempo_inicio = time.time()
precio_producto = {}
subtotal_ventas = {}
cantidad_total = {}
VENTAS_TOTALES = 0
RESULTADO_ARCHIVO = "SalesResults.txt"
NOMBRE_ARCHIVO_LIST = sys.argv[1]
NOMBRE_ARCHIVO_SALES = sys.argv[2]
# Procesar compras
detalles_ventas = []
with open(NOMBRE_ARCHIVO_LIST, 'r', encoding='UTF-8') as archivo:
    productos = json.load(archivo)


for producto in productos:
    title = producto['title']
    description = producto['description']
    price = producto['price']
    subtotal_ventas[title] = 0
    cantidad_total[title] = 0
    precio_producto[title] = abs(float(price))

with open(NOMBRE_ARCHIVO_SALES, 'r', encoding='UTF-8') as archivo:
    compras = json.load(archivo)

for compra in compras:
    SALE_ID = compra['SALE_ID']
    SALE_Date = compra['SALE_Date']
    Product = compra['Product']
    Quantity = compra['Quantity']
    if Product in precio_producto:
        cantidad_total[Product] += Quantity
        subtotal_ventas[Product] += precio_producto[Product]*Quantity
        VENTAS_TOTALES += precio_producto[Product]*Quantity
    else:
        print(f"Producto {Product} no existe en la lista de productos")

for producto, compra in subtotal_ventas.items():
    Product = producto
    if compra > 0:
        detalles_ventas.append([producto, cantidad_total[Product],
                                precio_producto[Product], compra])
tiempo_final = time.time() - tiempo_inicio
with open(RESULTADO_ARCHIVO, 'a', encoding='UTF-8') as ARCHIVO:
    ARCHIVO.write(tabulate(detalles_ventas,
                           headers=['Producto', 'Cantidad',
                                    'Valor Unitario', 'Subtotal']))
    ARCHIVO.write(f"\nTotal Ventas: {VENTAS_TOTALES:.2f}")
    print(tabulate(detalles_ventas,
                   headers=['Producto', 'Cantidad',
                            'Valor Unitario', 'Subtotal']))
    print(f"\nTotal Ventas: {VENTAS_TOTALES:.2f}\n")
    ARCHIVO.write(f"\nTiempo de ejecución:{tiempo_final}\n")
    print(f"\nTiempo de ejecución: {tiempo_final} segundos\n")
