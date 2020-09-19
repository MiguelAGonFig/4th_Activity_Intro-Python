# Programa main.py, recurre a funciones para calcular el area de un circulo, un traingualo y un cuadrado

def cuadrado(lado):
    return lado**2

def triangulo(base, altura):
    aux = base * altura
    return aux / 2

def circulo(radio):
    radio **= 2
    return radio * 3.14159

continuar = True
while continuar == True:
    print("Elija la figura de la que desea calcular el area")
    print("1.- Cuadrado")
    print("2.- Triangulo")
    print("3.- Circulo")
    respuesta = int(input("Ingrese una opción: "))
    if respuesta == 1:
        lado = float(input("Ingrese longitud del lado: "))
        print("El area del cuadrado es: ", cuadrado(lado), "cm^2")
    elif respuesta == 2:
        base = float(input("Ingrese la longitud de la base: "))
        altura = float(input("Ingrese la longitud de la altura: "))
        print("El area del triangulo es: ", triangulo(base, altura), "cm^2")
    elif respuesta == 3:
        radio = float(input("Ingrese la longitud del radio: "))
        print("El area del circulo es: ", circulo(radio), "cm^2")
    else:
        print("Entrada no valida")
    print("¿Desea calcular el area de otra figura?")
    print("1.- Sí")
    print("2.- No")
    valor = int(input("Elija una opción: "))
    if valor == 1:
        continuar = True
    elif valor == 2:
        continuar = False
        print("Hasta luego :)")
    else:
        continuar = False
        print("Entrada no valida, fin del programa")