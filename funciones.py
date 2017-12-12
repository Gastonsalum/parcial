#!/usr/bin/env python
import csv 
import os
from datetime import datetime

#Validar archivos CSV........
def validar_archivo(archivo):
    try:
        open(archivo).close()
    except FileNotFoundError:
        print('El archivo no encontrado')
        
    with open(archivo) as archivo1:
        print('se abrio')
        linea = archivo1.readline().strip().split(',')
        cabecera = ['CODIGO', 'PRODUCTO', 'CLIENTE', 'CANTIDAD', 'PRECIO']
        col_cod = linea.index(cabecera[0])
        col_prod = linea.index(cabecera[1])
        col_cli = linea.index(cabecera[2])
        col_cant = linea.index(cabecera[3])
        col_pre = linea.index(cabecera[4])
        
        n = 0
        for x in archivo1:
            lista = x.strip().split(',')
            n += 1
            if len(lista) != 5:
                raise Exception('La linea {} tiene un numero invalido de campos'.format(n+1))
            if lista[col_cod] == '':
                raise Exception('El campo Codigo de la linea {}  esta vacio'.format(n+1))
            elif lista[col_prod] == '':
                raise Exception('El campo Producto de la linea {}  esta vacio'.format(n+1))
            elif lista[col_cli] == '':
                raise Exception('El campo Cliente de la linea {}  esta vacio'.format(n+1))
            elif lista[col_cant] == '':
                raise Exception('El campo Cantidad de la linea {}  esta vacio'.format(n+1))
            elif lista[col_pre] == '':
                raise Exception('El campo CODIGO de la linea {}  esta vacio'.format(n+1))
            try:
                int(float(lista[col_cant]))
            except ValueError:
                raise Exception('El campo CANTIDAD de la linea {} no es un numero entero'.format(n+1))
            try:
                float(lista[col_pre])
            except ValueError:
                raise Exception('El campo PRECIO de la linea {} no es un valor decimal'.format(n+1))
        print('archivo OK')

#Generando Clase de registro

def generar_clase(archivo):
    class Registro:
        def __init__ (self, cliente, codigo, producto, cantidad, precio):
            self.cliente = cliente
            self.codigo = codigo
            self.producto = producto
            self.cantidad = cantidad
            self.precio = precio
        def __str__ (self):
            return '{}, {}, {}, {}, {}'.format(self.cliente, self.codigo, self.producto, self.cantidad, self.precio)
        def __repr__ (self):
            return '{}, {}, {}, {}, {}'.format(self.cliente, self.codigo, self.producto, self.cantidad, self.precio)
        def __gt__ (self, otro):
            return self.cantidad > otro.cantidad
        def compra (self):
            return self.cantidad * self.precio
    registros = []
    with open(archivo) as archivo1:
        linea = archivo1.readline().strip().split(',')
        cabecera = ['CODIGO', 'PRODUCTO', 'CLIENTE', 'CANTIDAD', 'PRECIO']
        col_cod = linea.index(cabecera[0])
        col_prod = linea.index(cabecera[1])
        col_cli = linea.index(cabecera[2])
        col_cant = linea.index(cabecera[3])
        col_pre = linea.index(cabecera[4])

        n = 1

        for x in archivo1:
            lista = x.strip().split(',')
            n += 1
            registros.append(Registro(cliente = lista[col_cli].upper(), codigo = lista[col_cod], producto = lista[col_prod].upper(), cantidad = int(float(lista[col_cant])), precio = float(lista[col_pre])))
    return (registros)


#Validacion de caracteres ingresados para la busqueda tanto como para la de clientes y la de producto; Utilizo la misma Funcion)

def min_caracteres(palabra):
    if len(palabra) >= 3:
        return
    else:
        return -1

#Busqueda de clientes ingresados en la lista de registros retorna una lista con todos los clientes encontrados

def clientes(registros, clientes):
    cliente = []
    for x in range(len(registros)):
        if clientes in registros[x].cliente:
            if registros[x].cliente in cliente:
                pass
            else:
                cliente.append(registros[x].cliente)
        else:
            pass
    return cliente

#Busqueda de productos ingresados en la lista de registros retorna una lista con todos los productos encontrados

def productos (registros, productos):
    producto = []
    for x in range(len(registros)):
        if productos in registros[x].producto:
            if registros[x].producto in producto:
                pass
            else:
                producto.append(registros[x].producto)
        else:
            pass
    return producto


# Busqueda del producto/Cliente encontrado y trae una lista con los objetos del registro que tengan el Producto/Cliente


def buscar_cli_o_prod(registros, palabra, busque):
    if busque == None:
        clientes=[]
        for x in range(len(registros)):
            if palabra in registros[x].cliente:
                clientes.append(registros[x])
            else:
                pass
            x += 1

        return clientes

    if busque == True:
        productos=[]
        for x in range(len(registros)):
            if palabra in registros[x].producto:
                productos.append(registros[x])
            else:
                pass
            x += 1

        return productos    

#Suma la cantidad de los productos y me muestra una lista con la suma de lo productos mas vendidos y los ordena de mayor a menor

def mas_vendidos(registros, cantidad):
    producto = []
    cant_producto = []
    colunna=0
    for x in range(len(registros)):
        if x == 0:
            producto.append(registros[x].producto)
            cant_producto.append([])
            cant_producto[colunna]= [0, registros[x]]
        else:
            if registros[x].producto in producto:
                pass
            else:
                colunna = colunna + 1
                producto.append(registros[x].producto)
                cant_producto.append([])
                cant_producto[colunna]= [0, registros[x]]
    for x in range(len(producto)):
        for y in range(len(registros)):
            if producto[x] in registros[y].producto:
                cant_producto[x][0]= cant_producto[x][0] + registros[y].cantidad
            else:
                pass
    cant_producto.sort(reverse=True)
    while cantidad > len(producto):
        cantidad -= 1
    list_cant = []
    for x in range(cantidad):
        list_cant.append([0]*2)
        list_cant[x][0] = cant_producto[x][0]
        list_cant[x][1] = cant_producto[x][1]
    return list_cant


#Busqueda de clientes que gastarons mas dinero y se reconocen como clientes VIP multiplicando las cantidades por el precio.

def clientes_vip(registros, cantidad):
    clientes = []
    cant_cliente = []
    colunna=0
    for x in range(len(registros)):
        if x == 0:
            clientes.append(registros[x].cliente)
            cant_cliente.append([])
            cant_cliente[colunna]=[0, registros[x]]
        else:
            if registros[x].cliente in clientes:
                pass
            else:
                clientes.append(registros[x].cliente)
                colunna = colunna + 1
                cant_cliente.append([])
                cant_cliente[colunna]=[0, registros[x]]

    for x in range(len(clientes)):
        for y in range(len(registros)):
            if clientes[x] in registros[y].cliente:
                cant_cliente[x][0]= cant_cliente[x][0] + (registros[y].cantidad * registros[y].precio)
            else:
                pass
    cant_cliente.sort(reverse=True)
    while cantidad > len(clientes):
        cantidad -= 1
    list_cant = []
    for x in range(cantidad):
        list_cant.append([0]*2)
        list_cant[x][0] = cant_cliente[x][0]
        list_cant[x][1] = cant_cliente[x][1]
    return list_cant


#------------------------------------------------------------
# funcion para buscar si el usuario existe

def existe(usuario):
    open('usuarios').close()
    with open('usuarios') as archivo1:
        for x in archivo1:
            linea = x.strip().split(',')
            if usuario == linea[0]:
                return(True)
            else:
                pass
    archivo1.close()
    return(False)
        
#Funcion para cambiar de clave

def cambiarclave(usuario, nueva_clave):
    print (usuario)
    print (nueva_clave)
    open('usuarios').close()
    with open('usuarios') as archivo:
        for x in archivo:
            linea = x.strip().split(',')
            if usuario == linea[0]:
                with open('usuariosn', 'a+') as archivo1:
                    archivo_csv = csv.writer(archivo1)
                    registro = [usuario, nueva_clave]
                    archivo_csv.writerow(registro)
            else:
                with open('usuariosn', 'a+') as archivo1:
                    archivo_csv = csv.writer(archivo1)
                    registro = [linea[0], linea[1]]
                    archivo_csv.writerow(registro)
    os.rename('usuariosn', 'usuarios') 

#Funcion para exportar consultas

def exportar(datos,consulta):
    nombre = 'consulta.csv'

    with open(nombre, 'w') as archivo1:
        if consulta == 'vendidos':
            archivo_csv = csv.writer(archivo1)
            registro = ['Productos más Vendidos']
            archivo_csv.writerow(registro)
            archivo_csv = csv.writer(archivo1)
            registro = ['CODIGO', 'PRODUCTO', 'CANTIDAD']
            archivo_csv.writerow(registro)
            for x in datos:
                linea = x

                archivo_csv = csv.writer(archivo1)
                registro = [linea[1].codigo,linea[1].producto,linea[0]]
                archivo_csv.writerow(registro)
        elif consulta == 'vips':
            archivo_csv = csv.writer(archivo1)
            registro = ['Mejores Clientes']
            archivo_csv.writerow(registro)
            archivo_csv = csv.writer(archivo1)
            registro = ['CLIENTE', 'VALOR']
            archivo_csv.writerow(registro)
            for x in datos:
                linea = x

                archivo_csv = csv.writer(archivo1)
                registro = [linea[1].cliente,linea[0]]
                archivo_csv.writerow(registro)
        elif consulta == 'productos':
            archivo_csv = csv.writer(archivo1)
            registro = ['productos por cliente']
            archivo_csv.writerow(registro)
            archivo_csv = csv.writer(archivo1)
            registro = ['CODIGO','PRODUCTO','CLIENTE','CANTIDAD', 'PRECIO']
            archivo_csv.writerow(registro)
            for x in datos:
                linea = x

                archivo_csv = csv.writer(archivo1)
                registro = [linea.codigo,linea.producto,linea.cliente,linea.cantidad,linea.precio]
                archivo_csv.writerow(registro)
        elif consulta == 'clientes':
            archivo_csv = csv.writer(archivo1)
            registro = ['Clientes por Productos']
            archivo_csv.writerow(registro)
            archivo_csv = csv.writer(archivo1)
            registro = ['CODIGO','PRODUCTO','CLIENTE','CANTIDAD', 'PRECIO']
            archivo_csv.writerow(registro)
            for x in datos:
                linea = x

                archivo_csv = csv.writer(archivo1)
                registro = [linea.codigo,linea.producto,linea.cliente,linea.cantidad,linea.precio]
                archivo_csv.writerow(registro)





   


    


