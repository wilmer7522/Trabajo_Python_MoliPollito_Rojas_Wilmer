import json
from os import system
from datetime import date

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
            seleccion = int(input("(1).Tomar pedido | (2).Estado del Pedido: | (3).Pagar Pedidos:  \nIngrese opcion: "))
        
            booleanoMenu = False
        except ValueError:
            input("ingrese un valor valido")
            system("cls")

    if seleccion == 1:
        entra = int(input("(1).Entrada: \n(2).Plato Fuerte: \n(3).Bebida: "))
        nombreCliente = input("Ingrese Nombre del Cliente: ")
        contMenu = 1
        contMenuPla = 1
        contMenuBebi = 1
        
        num = 0
        numPlato = 0
        numBebi = 0
        if entra == 1:
            menu = abrirMenu()
            print("---------")
            print("  Menu   ")
            print("---------")
            
            
            for i in menu:
                
                if i["categoria"] == "entrada":
                    if num == 0:
                        print("Entradas")
                        print("--------")
                        num += 1
                    print(contMenu,i["categoria"], i["nombre"], i["precio"])

                    contMenu +=1

            eleEntra = int(input("Ingrese el id de la entrada: "))
            eleNombre = menu[eleEntra-1]["nombre"]
            precio = menu[eleEntra-1]["precio"]
            
            pedidos = abrirPedidos()
            pedidos.append({
                "cliente": nombreCliente,
        "items": [
            {
                "categoria": "entrada",
                "nombre": eleNombre,
                "precio": precio
            }]})
            guardarPedidos(menu)
            
        if entra == 2:
            menu = abrirMenu()
            for i in menu:
                if i["categoria"] == "plato_fuerte":
                    if numPlato == 0:
                        print("------------")
                        print("Plato Fuerte")
                        print("------------")
                    numPlato += 1
                
                    print(contMenuPla,i["categoria"], i["nombre"], i["precio"])
                    contMenuPla += 1
                
            
        
        if entra == 3:
            menu = abrirMenu()
            for i in menu:
                if i["categoria"] == "bebida":
                    if numBebi == 0:
                        print("------------")
                        print("Bebidas")
                        print("------------")
                        numBebi += 1
                    print(contMenuBebi,i["categoria"], i["nombre"], i["precio"])
                    contMenuBebi += 1
                
            

        



    if seleccion == 5: 
        input("Gracias  por preferir FarmCamp, nos vemos luego :)")
        booleanoMenu = False
        break
            
    
