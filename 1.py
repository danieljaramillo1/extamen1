
multiplo2=0
multiplo3=0
try:

    size = int(input("dame el tamaño: "))
except:
    print("debes ingresar un valor entero diferente de cero")
else:
    if(size!=0):

        for i in range(0,size):
        
            numero = int(input("ingresa numero: "))
            if numero%2 == 0 and numero%3 ==0:
                multiplo2 =multiplo2+1
                multiplo3 = multiplo3+1
            elif numero%2 == 0:
                multiplo2 =multiplo2+1
            elif numero%3 == 0:
                multiplo3 = multiplo3+1

        print(f"hay",multiplo2," multiplos de 2 y hay ",multiplo3," multiplo de 3")
    else:
        print("el valor ingresado no puede ser cero")



        

