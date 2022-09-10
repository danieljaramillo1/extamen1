print(f" ")
print(f". ")

print("1. PARA INGRESAR PRODUCTO")
print("2. VER PRODUCTO")
print("3. EDITAR PRECIO")
print("4. ELIMINAR PRODUCTO")
print("5. PARA SALIR")
print(f" ")
print(f". ")
select = 100
productos = []
while select !=5:
    try:
        select=int(input("Que quieres hacer?: "))
    except:
        print("ingresaste un valor erroneo")
    else:
        if select == 1:
            producto={}
            producto["codigo"]=int(input("ingrese el codigo del producto: "))
            producto["nombre"]=(input("ingrese el nombre del producto: "))
            producto["precio"]=int(input("ingrese el precio del producto: "))
            productos.append(producto)
        elif select == 2:
            print(productos)

        elif select == 3:
            code = int(input("Digite el codigo del producto: "))
            
            for i in range(0, len(productos)):
                if productos[i]["codigo"] == code:
                    precio = int(input("ingrese el nuevo precio: "))
                    productos[i]["precio"] = precio

        elif select == 4:

            code = int(input("Digite el codigo del producto: "))
            
            for i in range(0, len(productos)):
                if productos[i]["codigo"] == code:
                    productos.pop(i)
                    print("el prducto ha sido eliminado")
                    break
        elif select == 5:
            break
        else:
            print("ingresaste un valor erroneo")


                
                


