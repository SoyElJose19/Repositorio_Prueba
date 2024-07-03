import time, os
from funciones import *

while True:
    os.system("cls")
    print ("\tPEDIDOS GAS")
    print ("1.-Registrar pedidos")
    print ("2.-Listar todos los pedidos")
    print ("3.-Buscar pedido por RUT")
    print ("4.- Imprimir hoja de ruta")
    print ("5.- Salir")
    opc =int(input("Ingrese Opcion: "))
    os.system("cls")
    if opc==1:
        registrar_pedidos()
    elif opc==2:
        listar_pedidos()
    elif opc==3:
        buscar_pedidos()
    elif opc==4:
        hoja_de_ruta()
    else:
        salir()
    time.sleep(3)