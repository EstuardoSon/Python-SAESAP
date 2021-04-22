print("////////////////Primer Problema//////////////////")
numero=int(input("Ingrese la altura del triangulo: "))

segundo=1
for i in range(0,numero):
    forma=""

    for y in range(0,segundo):
        forma+="*"
    segundo+=1
    print(forma)

print("////////////////Segundo Problema//////////////////")

numero=int(input("Ingrese un numero entero: "))

contador=0
for i in range(1,numero):
    if(numero%i)==0:
        contador+=1

if contador==1:
    print("El numero",numero," es primo")
else:
    print("El numero",numero," NO es primo")

    