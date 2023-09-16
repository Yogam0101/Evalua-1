print("FESTIVAL DE ROCK")
print("*****")
print("1.Registrar Banda")
print ("2.Buscar Bandas que aun no se presentan")
print("3.cambiar La Hora de presentacion de una Banda")
print("4.Eliminar regsitro de una Banda")
print("5.Salir")
print("****")

opcion=90

def init(self, id, nombre, genero, hora, pago, estado):
        self.id = id
        self.nombre = nombre
        self.genero = genero
        self.hora = hora
        self.pago = pago
        self.estado = estado

bandasm=[]
while opcion!=5:
    banda={ }

    opcion= int(input("Digite la Opcion de desea Realizar__"))

    if opcion==1:
    
        banda["id"]= int(input("Ingrese el ID de la banda: "))
        banda["nombre"]= input("Ingrese el nombre de la Banda: ")
        banda["genero"]= input("Ingrese el genero de la agrupación: ")
        banda["hora"]=input("Ingrese la hora de presentación de la agrupación: ")
        banda["pago"]= float(input("Ingrese el pago que se le dará a la agrupación: "))
        banda["estado"]= input("¿La agrupación ya se presentó? (1 = Sí , 2 = No): ")
        print("Agrupación registrada exitosamente.")

    elif opcion==2:
        def nosehanpresentado():
                for banda in bandasm:
                    if banda["estado"]==1:
                        estado = True
                else:
                        estado =False
                        banda =bandasm(id,nombre,estado)
                        bandasm.append(banda)
                        print("la banda aun no se presenta.")

    elif opcion==3:
        id=input("Ingrese el nombre de la banda")
        for  banda in bandasm:
                if banda["id"]==id:
                    if banda["estado"]==2:
                        newh=input("ingrese la nueva hora de presentacion :")
                    banda["hora"]=newh
                    print(" Actualizada la hora de presentacion")
                    print(f"{banda['id']},{banda['nombre']},{banda['hora']}")
                    
                else:
                    print("No se puede hacer cambios, la banda ya se presento")
                
        else:
                print("la banda no existe")

    elif opcion==4:
        nombre=input("Ingrese el nombre de la banda")
        for banda in bandasm:
                if banda["nombre"]== nombre:
                    bandasm.remove(banda)
                print(f"banda {'nombre'} eliminado con éxito.")
            
        else:
                    print(f"No se encontró el usuario {nombre}.")
                    
    elif opcion ==5:
        print("Saliendo del programa...")
else:
        print("Opción inválida. Por favor, seleccione una opción válida.")

        print("Programa finalizado.")

