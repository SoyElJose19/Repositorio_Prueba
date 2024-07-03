import csv
pedidos=[]

def registrar_pedidos():
    while True:
        try:
            rut=input("Ingrese su RUT (si termina en K, reemplacelo por un 0): ")
            if len(str(rut))==9 and str(rut.endswith)=="0":
                rut.endswith="K"
            elif rut.endswith =="k".upper:
                print("ERROR! SI TERMINA EN K REEMPLAELO POR UN 0")
        except:    
            print("ERROR! SU RUT DEBE TENER MÍNIMO 8 DIGITOS Y SI TERMINA EN K, REEMPLAZARLO POR UN 0")
        try:
            nombre= input("Ingrese Nombre: ")
            if len(str(nombre.capitalize))>=3 and nombre.isalpha:
                return nombre
                
        except:
            print("ERROR! SU NOMBRE DEBE TENER POR LO MENOS 3 CARACTERES")

        try:
            direccion= input("Ingrese Dirección: ")
            if len(str(direccion.capitalize))>=6 and direccion.isalpha:
                return direccion
        except:
            print("ERROR! SU DIRECCIÓN NO ES VALIDA, DEBE TENER COMOM MINIMO 6 CARACTERES")
        try:
            comuna= int(input("Ingrese Comuna (1.- Santiago, 2.- Colina, 3.- Recoleta): "))
            comuna=("santiago","colina","recoleta")
            if len(str(comuna)) == comuna():
                return (comuna+1)
        except:
            print("ERROR! SELECCIONE UNA COMUNA VALIDA")

        try:
            cincokg=int(input("Ingrese Cilindros de 5kg a llevar: "))
            if cincokg==0:
                cincokg = 0
                break
            elif cincokg>=1:
                cincokg = 12500
                return cincokg
        except:
            print("ERROR! NÚMERO NO VALIDO, DEBE SER ENTRE 0 y 1 COMO MINIMO")
        
        try:
            quincekg=int(input("Ingrese Cilindros de 15kg a llevar: "))
            if quincekg==0:
                quincekg = 0
                break
            elif cincokg>=1:
                quincekg = 25500
                return quincekg
        except:
            print("ERROR! NÚMERO NO VALIDO, DEBE SER ENTRE 0 y 1 COMO MINIMO")
        
            print ("\nTOTAL:",total)
            if not cincokg:
                break
            elif not quincekg:
                break
            else:
                total = cincokg + quincekg
        
        pedido={"rut":rut,
                "nombre":nombre,
                "direccion":direccion,
                "comuna":comuna,
                "cincokg":cincokg,
                "quincekg":quincekg,
                "total":total}
    pedidos.append(pedido)
    print("PEDIDO GUARDADO CON ÉXITO")
    
def listar_pedidos():
    if not pedidos:
        print("NO EXISTEN PEDIDOS, INGRESE ALMENOS UNO")
    else:
        print("\tPEDIDOS")
        for p in pedidos:
            print("RUT:",p["rut"])
            print("NOMBRE:",p["nombre"])
            print("DIRECCION:",p["direccion"])
            print("COMUNA:",p["comuna"])
            print("CILINDRO DE 5:",p["cincokg"])
            print("CILINDRO DE 15:",p["quincekg"])
            print ("TOTAL: ")
            print()
def buscar_pedidos():
    pass
def hoja_de_ruta():
    nombre_archivo=input("Ingrese Nombre del Archivo: ")
    with open (nombre_archivo+".csv", "w", newline="") as archivo:
        escritor =csv.writer(archivo)
        escritor.writerows(pedidos)
    print("ARCIVHO CREADO CON ÉXITO")

def salir():
    print ("Gracias, saliendo del sistema...")
    exit()
