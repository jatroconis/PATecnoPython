import Constantes.menuPrincipalOPC as datamenuP
import Utilidaes.stringBuilder as strbld


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