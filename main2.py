import json
from os import system
from datetime import date
from collections import defaultdict

#Menu
def abrirMenu():
    mijsonMenu=[]
    with open('Menu.json', 'r', encoding='utf=8') as openfile:
        mijsonMenu = json.load(openfile)
    return mijsonMenu

def guardarMenu(dataMenu):
    with open('Menu.json', 'w', encoding='utf=8') as outfile:
        json.dump(dataMenu,outfile,indent=4)

#Pagos
def abrirPagos():
    mijsonPagos=[]
    with open('Pagos.json', 'r', encoding='utf=8') as openfile:
        mijsonPagos = json.load(openfile)
    return mijsonPagos

def guardarPagos(dataPagos):
    with open('Pagos.json', 'w', encoding='utf=8') as outfile:
        json.dump(dataPagos,outfile,indent=4)

#Pedidos
def abrirPedidos():
    mijsonPedidos=[]
    with open('Pedidos.json', 'r', encoding='utf=8') as openfile:
        mijsonPedidos = json.load(openfile)
    return mijsonPedidos

def guardarPedidos(dataPedidos):
    with open('Pedidos.json', 'w', encoding='utf=8') as outfile:
        json.dump(dataPedidos,outfile,indent=4)


#Inicio

Todo = True
while Todo == True:
    MenuTodo = abrirMenu()
    booleanoMenu = True

    while booleanoMenu == True:
        print("---------------------------------")
        print("            Moli Pollito         ")
        print("---------------------------------") 

        try:
            seleccion = int(input("(1).Tomar pedido | (2).Estado del Pedido: | (3).Pagar Pedidos:  (4).Cambiar Pedido: (5).Salir \nIngrese opcion: "))
        
            booleanoMenu = False
        except ValueError:
            input("ingrese un valor valido")
            system("cls")

    if seleccion == 1:
        nombreCliente = input("Ingrese el Nombre del Cliente: ")

        itemPedido = []
        boolPedido = True
        while boolPedido == True:

            contMenu = 1
            menu = abrirMenu()
            print("---------")
            print("  Menu   ")
            print("---------")
                
                
            for i in menu:
                    
                        
                print(contMenu,i["categoria"],":", i["nombre"] ,"$",i["precio"])

                contMenu +=1


            eleEntra = int(input("Ingrese el id de la entrada: "))
            eleCategoria = menu[eleEntra-1]["categoria"]
            eleNombre = menu[eleEntra-1]["nombre"]
            precio = menu[eleEntra-1]["precio"]


            itemPedido.append({
                    "categoria": eleCategoria,
                    "nombre": eleNombre,
                    "precio": precio
                    })
            

            seguir = int(input("Desea Seguir agregando mas items al pedido?: (1).Si.  (2).No "))
            if seguir == 2:
                boolPedido = False


        
        pedidos = abrirPedidos()
        pedidos.append({
                "cliente": nombreCliente,
                "items": itemPedido,
                "estado": "creado"
                }
                )
        guardarPedidos(pedidos)
        print("se guardo el pedido")
            
                
            
    if seleccion == 2:
        pedido = abrirPedidos()
        conta = 1
        for i in pedido:


            print(conta, i["cliente"],"|","Estado del Pedido: ", i["estado"])
            conta += 1

        estado = int(input("que pedido desea Modificar?: "))


        nuevoestado = int(input("(1).Preparacion (2).Servido  (3).No modificar"))

        if nuevoestado == 1:
            pedido[estado-1]["estado"] = "preparacion"

        if nuevoestado == 2:
            pedido[estado-1]["estado"] = "preparacion"

        if nuevoestado == 3:
            break
        guardarPedidos(pedido)


    if seleccion == 3:
        pedidoPagar = abrirPedidos()
        conta = 1
        for i in pedidoPagar:
            total = 0
            for a in i["items"]:
                total = total + a["precio"]

            print(conta, i["cliente"], total)
            conta += 1
            

        estado = int(input("que pedido desea Pagar?: "))
        
        

        
        nuevoestado = int(input("(1).Pagar (2).No pagar "))

        if nuevoestado == 1:
            pedidoPagar[estado-1]["estado"] = "pagado"

        
        guardarPedidos(pedidoPagar)

        if nuevoestado == 2:
            input("Hasta pronto")
            break
        
    if seleccion == 4:
        cambiar = abrirPedidos()
        conta = 1
        for i in cambiar:
            print(conta,i["cliente"])


    if seleccion == 5: 
        input("Gracias  por preferir FarmCamp, nos vemos luego :)")
        booleanoMenu = False
        break
            
    
