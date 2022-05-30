import tkinter as tk
from tkinter import ttk
import menus
import database.models.productos  as Prd
# Database 
import database.database as db
import os 


clear = lambda: os.system('cls')


#-----------bucle para el menu------------#
#-----------------------------------------#

# ------------------------- MENU DE CONSOLA ------------------------#
active = True

#ACTIVADORES DE MENU
activeMenu1 = True
activeMenu2 = True


#OPCIONES DE MENU
opciones = 0

while active: 
    clear()
    print(menus.returnMenuPrincipal())
    print("\n")
    opciones = int(input("Ingrese una opcion: "))

    if opciones == 1:
        activeMenu1 = True
        while activeMenu1:
            clear()
            ptemo =  object.__new__(Prd.productos,("", 0, 0))
            print ("Ingrese el nombre del producto que desea registrar: ")
            ptemo.nombre = input()
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
                for product in db.GetArrayOfProductsDB():
                    print (product.nombre, product.precio, product.cantidad)
            print ("Desea ver nuevamente los productos? (si/no)")
            if input() == "no":
                activeMenu2 = False
                print ("Adios")


# ------------------------- MENU DE CONSOLA ------------------------# 


#--------------- MENU DE TKINTER ---------------#

# menuprincipal = tk.Tk()
# menuprincipal.geometry("400x400")
# ttk.Label(menuprincipal, text="PROYECTO DE AULA INVENTARIO").pack()
# Opciones = ttk.Label(text=menus.returnMenuPrincipal())
# Opciones.place(x=0, y=30)



# menuprincipal.title("Programa De Inventario")
# menuprincipal.mainloop()