#PRIMER EJERCICIO
def analizar():
    if contrasenia==confirm:
        return "Las contraseñas coinciden"
    else:
        return "Las contraseñas no coinciden"

print("--------------Ejercicio 1-------------")

contrasenia=str(input("Ingrese su contraseña: ")).lower()

confirm=str(input("Vuelva a ingresar la contraseña: ")).lower()

print(analizar())

#SEGUNDO EJERCICIO

print("--------------Ejercicio 2-------------")

def alumno(**datos):
    nombre=datos["nombre"].lower()
    for i in "abcdefghijklm":
        if nombre[0]==i and datos["sexo"].lower()=="mujer":
            return "Pertenece al grupo A"
    
    for i in "nñopqrstuvwxyz":
        if nombre[0]==i and datos["sexo"].lower()=="hombre":
            return "Pertenece al grupo A"
    
    else:
        return "Pertenece al grupo B"

nombre=str(input("Ingrese su nombre: "))
sexo=str(input("Ingrese su sexo: "))

print(alumno(nombre=nombre,sexo=sexo))
