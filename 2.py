frutas = []


for i in range(0,10):
    fruta={}
    fruta["nombre"]=input("dame el nombre de la fruta: ")
    fruta["color"]=input("dame el color de la fruta: ")
    fruta["precio"]=input("dame el precio de la fruta: ")
    frutas.append(fruta)
print(f"frutas bien: ",frutas)
frutas.reverse()
print(f"frutas al revez: ",frutas)


