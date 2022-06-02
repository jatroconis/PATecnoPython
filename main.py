import tkinter as tk
from tkinter import N, ttk

from pkg_resources import cleanup_resources
import menus
import database.models.productos  as Prd
import database.models.user as usr
# Database 
import database.database as db
import os 

#utilities string builder
import Utilidaes.stringBuilder as strbld


clear = lambda: os.system('cls')


#-----------bucle para el menu------------#
#-----------------------------------------#

# ------------------------- MENU DE CONSOLA ------------------------#


#PERSON
nameperson = ""

#ACTIVADORES DE MENU
active = True
activeMenu1 = True
activeMenu2 = True
activeMenu3 = True
activeMenu4 = True


#OPCIONES DE MENU
opciones = 0

#lista de opciones

datalistmenu2 = strbld.StringBuilder()

#funcion para obtener el id disponible
def getId():
    id = 0
    for product in db.GetArrayOfProductsDB():
        if product.id > id:
            id = product.id
    return id + 1

def getIdUser():
    id = 0
    for user in db.arrayUsers:
        if user.id > id:
            id = user.id
    return id + 1

clear()
print("INGRESE SU NOMBRE: ")
nameperson = input()

while active:
    clear()
    print("Bienvenido "+nameperson.upper())
    print("\n")

    print(menus.returnMenuPrincipal())
    print("\n")
    opciones = int(input("Ingrese una opcion: "))

    if opciones == 1:
        activeMenu1 = True
        while activeMenu1:
            clear()
            ptemo =  object.__new__(Prd.productos,("", 0, 0))
            ptemo.id = getId()
            print ("Ingrese el nombre del producto que desea registrar: ")
            ptemo.nombre = input().upper()
            print ("Ingrese el precio del producto que desea registrar: ")
            ptemo.precio = input()
            print ("Ingrese la cantidad del producto que desea registrar: ")
            ptemo.cantidad = input()
            db.AddProduct(ptemo)

            print ("Desea registrar otro producto? (si/no)")
            if input() == "no":
                activeMenu1 = False
                print ("Adios")

    if opciones == 2:
        activeMenu2 = True
        while activeMenu2: 
            clear()
            print ("Productos registrados: ")
            if len(db.GetArrayOfProductsDB()) == 0:
                    print ("No hay productos registrados")
            else:
                print(menus.returnlistproducts())
            print ("Desea ver nuevamente los productos? (si/no)")
            if input() == "no":
                activeMenu2 = False
                print ("Adios")

    if opciones == 3:
        activeMenu3 = True
        while activeMenu3:
            clear()
            muser = object.__new__(usr.user,("", 0, 0))
            muser.id = getId()
            muser.nombre = nameperson
            print ("Ingrese el nombre del producto que desea comprar: ")
            nombre = input().upper()
            while db.GetProductByName(nombre) == None:
                clear()
                print ("El producto no existe, ingrese otro nombre")
                nombre = input().upper()
            muser.nombreProductoComprado = nombre

            print ("Ingrese la cantidad del producto que desea comprar: ")
            cantidad = int(input())
            tempcantidad = db.GetProductByName(nombre).cantidad
            while (cantidad > int(db.GetProductByName(nombre).cantidad)):
                print ("La cantidad ingresada es mayor a la disponible, ingrese otra cantidad")
                cantidad = int(input())
            muser.cantidadProductoComprado = cantidad
            muser.valorCompra = int(cantidad) * int(db.GetProductByName(nombre).precio)
            
            # si la cantidad es mayor a 10 hacer un descuento del 15%
            if int(cantidad) > 10:
                muser.valorlorDescontado = int(muser.valorCompra) * 0.15
            else:
                muser.valorlorDescontado = 0

            db.addMovementsUser(muser)

            #----------------- update data products

            db.editProductQuantity(db.GetProductByName(nombre).id, (str(int(db.GetProductByName(nombre).cantidad) - int(muser.cantidadProductoComprado))))
            print("\n")
            print("el precio del producto es: " + str(db.GetProductByName(nombre).precio))
            print("Su compra se ha realizado con exito")
            print("Su compra fue de: " + str(muser.valorCompra))
            print("Su descuento fue de: " + str(muser.valorlorDescontado))
            print("Su total fue de: " + str(muser.valorCompra - muser.valorlorDescontado))
            

            print ("Desea comprar otro producto? (si/no)")
            if input() == "no":
                activeMenu3 = False
                print ("Adios")
        print ("Venta de productos")

    if opciones == 4:
        print ("Eliminar productos")
        activeMenu4 = True
        while activeMenu4:
            clear()
            print ("Desea eliminar por nombre o por id? (nombre/id)")
            opcion = input()
            if opcion == "nombre":
                print ("Ingrese el nombre del producto que desea eliminar: ")
                nombre = input()
                db.deleteProductByName(nombre.upper())
                print ("Producto eliminado")
            elif opcion == "id":
                print ("Ingrese el id del producto que desea eliminar: ")
                id = int(input())
                db.deleteProduct(id)
                print ("Producto eliminado")
            else:
                print ("Opcion invalida")
            print ("Desea eliminar otro producto? (si/no)")
            if input() == "no":
                activeMenu4 = False
                print ("Adios")  

    if opciones == 5:
        print ("Movimiento de Usuarios")
        activeMenu5 = True
        while activeMenu5:
            clear()
            print ("Movimientos registrados: ")
            if len(db.arrayMovementsUser()) == 0:
                    print ("No hay Movimientos registrados")
            else:
                print(menus.returnlistusers())
            print ("Desea ver nuevamente los Movimientos? (si/no)")
            if input() == "no":
                activeMenu5  = False
                print ("Adios")   

    if opciones == 6:
        active = False
        clear()
        print ("Gracias por usar el programa, hasta luego")

        

# ------------------------- MENU DE CONSOLA ------------------------# 


#--------------- MENU DE TKINTER ---------------#

# menuprincipal = tk.Tk()
# menuprincipal.geometry("400x400")
# ttk.Label(menuprincipal, text="PROYECTO DE AULA INVENTARIO").pack()
# Opciones = ttk.Label(text=menus.returnMenuPrincipal())
# Opciones.place(x=0, y=30)



# menuprincipal.title("Programa De Inventario")
# menuprincipal.mainloop()