frutas = []
costos = []

#Función para calcular el costo total del salpicón
def costo_total(frutas):
    total=0
    for fruta in frutas:
        total +=
        fruta['precio_unitario'] *
        fruta ['cantidad']
        return Total
    
    #Función para mostrar las frutas ordenadas por costo

    def mostrar_frutas_ordenadas(frutas):
        frutas_ordenadas = sorted(frutas,key=lambda x: x['precio_unitario'],reverse=True):
        for fruta in frutas_ordenadas:
            print (f"Fruta: {fruta['NOMBRE']}")

            Costo Unitario:
            {fruta ['precio_unitario']} - cantidad: {
                fruta['cantidad']}")
            
            #FUNCIÓN PARA ENCONTRAR LA FRUTA MAS BARATA Y MAS CARA
            def fruta_mas_barata (frutas)
        def fruta_mas_cara(frutas):
            frutas_ordenadas = sorted(frutas,key=lambda x: x['precio_unitario']):
            fruta_mas_barata =
            frutas_ordenadas[0]
            fruta_mas_cara =
            frutas_ordenadas[-1]
            return fruta_mas_barata, fruta_mas_cara
        
        #SE PIDE AL USUARIO LA CANTIDAD DE FRUTAS QUE VA A INGRESAR

        n = int(input("INGRESE LA CANTIDAD DE FRUTAS: "))

        #DETALLES DE FRUTAS Y AGREGAR A LA LISTA O3O
        for i in range(n):
id_fruta = i+ 1
nombre = input(f "nombre de la fruta"{id_fruta}: ")
               precio_unitario =
               float(input(f"precio unitario de la fruta {id_fruta}:"))
               cantidad = int(input (f"CANTIDAD DE LA FRUTA{id_fruta}: "))
               fruta = {'id': id_fruta, 'nombre':nombre,'precio_unitario':
                        precio_unitario,'cantidad': cantidad}
                        frutas.append(fruta)

                        #MOSTRAMOS COSTO TOTAL DEL SALPICÓN

                        print (f"COSTO TOTAL DEL SALPICÓN: {costo_total(frutas)}")
                    
                    #MOSTRAR LAS FRUTAS DE BARATO A CARO
                    print(f"FRUTAS MAS BARATA ES:" {fruta_mas_barata ['nombre']}) con un precio de $
                    {fruta_mas_cara ['precio_unitario']:.2f}")
