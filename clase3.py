'''
if (condiciones o muchas condiciones){
    // conjunto de codigo en caso se cumpla las condiciones
}
'''

#sintaxis 
#if condicion o muchas condiciones :
#--Conjunto de instrucciones

#Pasos
#palabra if
#condicion
#sentencia de ejcucion, si cumplo la condicion
#sentencia de ejecucion, donde no cumple condicion

#Condiciones de Python y declaraciones If

#Condiciones de Python y declaraciones If
print("---")
print("condiciones de Python y declaraciones if")
a=100
b=200
if b>a:
    print("B is greater than a")

print("----")

#Ejemplo else if

a=33
b=33

if a>b:
    print("b is greater than a")

elif a==b:
    print("a and b are equal")

#Ejemplo else

print("----")

a=200
b=33

if b>a:
    print("b is greater than a")

elif a==b:
    print("a and b are equal")

else:
    print("a is grether than b")

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
print("Fin 3 Ejemplo")