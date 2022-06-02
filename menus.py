import Constantes.menuPrincipalOPC as datamenuP
import Utilidaes.stringBuilder as strbld
import database.database as db

def returnMenuPrincipal():
    opcmenus = strbld.StringBuilder()
    position = 1
    opcmenus.Append("[*] Menu Principal [*]\n")
    for data in datamenuP.inventarioMenus:
        opcmenus.Append("\n")
        opcmenus.Append("["+str(position)+"] ")
        opcmenus.Append(data)
        position += 1
    position = 1
    return opcmenus

def returnlistproducts():
    opcmenus = strbld.StringBuilder()
    position = 1
    opcmenus.Append("[*] Lista de productos [*]\n")
    opcmenus.Append("[ID]\t[Nombre]\t[Precio]\t[Cantidad]\n")
    for data in db.GetArrayOfProductsDB():
        opcmenus.Append("\n")
        #opcmenus.Append("["+str(position)+"]\t")
        opcmenus.Append("["+str(data.id)+"]\t")
        opcmenus.Append(data.nombre)
        opcmenus.Append("\t\t")
        opcmenus.Append(data.precio)
        opcmenus.Append("\t\t")
        opcmenus.Append(data.cantidad)
        position += 1
    position = 1
    return opcmenus

def returnlistusers():
    opcmenus = strbld.StringBuilder()
    position = 1
    opcmenus.Append("[*] Lista de Movimientos De Usuarios [*]\n")
    opcmenus.Append("[ID]\t[Nombre]\t[Producto]\t[Valor Compra]\t[Valor Descuento]\t[Cantidad Comprada]\n")
    for data in db.arrayMovementsUser():
        opcmenus.Append("\n")
        #opcmenus.Append("["+str(position)+"]\t")
        opcmenus.Append("["+str(data.id)+"]\t")
        opcmenus.Append(data.nombre)
        opcmenus.Append("\t\t")
        opcmenus.Append(data.nombreProductoComprado)
        opcmenus.Append("\t\t")
        opcmenus.Append(str(data.valorCompra))
        opcmenus.Append("\t\t")
        opcmenus.Append(str(data.valorlorDescontado))
        opcmenus.Append("\t\t")
        opcmenus.Append(str(data.cantidadProductoComprado))
        position += 1
    position = 1
    return opcmenus