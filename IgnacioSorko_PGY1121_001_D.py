lista_encomienda = []

cntSobre = 0

cntPaquete = 0



menu_tipo = """
         Tipo
----------------------
1. Sobre
2. Paquete
"""

menu = """
          Menú
------------------------
1. Grabar
2. Buscar
3. Listar Encomiendas
4. Salir
"""
while True:
    try:
        opc = int(input(menu))
        if opc == 4: 
            print("Ha cerrado el programa de Ignacio Sorko version 1.0")
            break
        elif opc == 1:
            while True:
                try:
                    tipo = int(input(menu_tipo))
                    if tipo == 1:
                        cntSobre += 1
                        lista_encomienda.append('Sobre')                        
                        break
                    elif tipo == 2:
                        cntPaquete += 1
                        lista_encomienda.append('Paquete')                       
                        break
                    else:
                        print("Error parametro")
                except:
                    print("Ha ocurrido un error")
            while True:
                try:
                    nombre = input("Nombre y Apellido del destinatario: ")
                    if len(nombre) > 1 and len(nombre) < 31:
                        lista_encomienda.append(nombre)
                        break
                    else:
                        print("Error caracteres")
                except:
                    print("Ha ocurrido un error")
            while True:
                try:
                    rut = input("Rut del destinatario: ")
                    if rut[-2] == "-":
                        lista_encomienda.append(rut)
                        break
                    else:
                     print("Por favor colocar bien el guión")
                except:
                    print("Ha ocurrido un error")
            while True:
                try:
                    peso = float(input("Peso en kilogramos de la encomienda: "))
                    if peso > 0:
                        lista_encomienda.append(peso)
                        break
                    else:
                        print("Error [Peso Negativo]")                    
                except:
                    print("Ha ocurrido un error")
            while True:
                try:
                    precio = int(input("Precio de la encomienda[Precio mínimo $2000]: "))
                    if precio > 1999:
                        lista_encomienda.append(precio)
                        break
                    else:
                        print("Error de Precio")
                except:
                    print("Ha ocurrido un error")
            while True:
                try:
                    ciudad = input("Ciudad del destinatario: ")
                    if len(ciudad) > 2:
                        lista_encomienda.append(ciudad)
                        break
                    else:
                        print("Error caracteres")
                except:
                    print("Ha ocurrido un error")
        elif opc == 2:
            buscar = input("Rut del destinatario: ")
            for buscar in range(lista_encomienda):
                if buscar == rut:
                    print(lista_encomienda)
        elif opc == 3:
            print(lista_encomienda)
            print(f"Cantidad de Sobres:   {cntSobre}")
            print(f"Cantidad de Paquetes: {cntPaquete}")
            
        elif opc > 4 or opc < 0:
            print("Error de parametro")
    except:
        print("Ha ocurrido un error")

#No estuve muchas clases y me falto harto estudio, entre irresponsabilidad y problemas personales no pude dar mi rendimiento de siempre pero en el examen voy con todo.