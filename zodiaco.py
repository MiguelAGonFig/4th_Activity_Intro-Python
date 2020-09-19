# El script muestra el signo zodiacal del usuario segun su dia y mes de nacimiento

continuar = True
while continuar == True:
    print("Para conocer tu signo zodiacal ingresa los siguientes datos")
    print("Ejemplo: Dia de nacimiento: 12 - Mes de nacimiento: 4")
    dia = int(input("Dia de nacimiento: "))
    mes = int(input("Mes de nacimiento: "))
    if dia >= 21 and dia <= 31 and mes == 3:
        print("Tu signo zodiacal es Aries")
    elif dia <= 20 and dia >= 1 and mes == 4:
        print("Tu signo zodiacal es Aries")
    elif dia >= 21 and dia <= 30 and mes == 4:
        print("Tu signo zodiacal es Tauro")
    elif dia <= 20 and dia >= 1 and mes == 5:
        print("Tu signo zodiacal es Turo")
    elif dia >= 21 and dia <= 31 and mes == 5:
        print("Tu signo zodiacal es Géminis")
    elif dia <= 20 and dia >= 1 and mes == 6:
        print("Tu signo zodiacal es Géminis")
    elif dia >= 21 and dia <= 30 and mes == 6:
        print("Tu signo zodiacal es Cáncer")
    elif dia <= 20 and dia >= 1 and mes == 7:
        print("Tu signo zodiacal es Cáncer")
    elif dia >= 21 and dia <= 31 and mes == 7:
        print("Tu signo zodiacal es Leo")
    elif dia <= 20 and dia >= 1 and mes == 8:
        print("Tu signo zodiacal es Leo")
    elif dia >= 21 and dia <= 31 and mes == 8:
        print("Tu signo zodiacal es Virgo")
    elif dia <= 20 and dia >= 1 and mes == 9:
        print("Tu signo zodiacal es Virgo")
    elif dia >= 21 and dia <= 30 and mes == 9:
        print("Tu signo zodiacal es Libra")
    elif dia <= 20 and dia >= 1 and mes == 10:
        print("Tu signo zodiacal es Libra")
    elif dia >= 21 and dia <= 31 and mes == 10:
        print("Tu signo zodiacal es Escorpio")
    elif dia <= 20 and dia >= 1 and mes == 11:
        print("Tu signo zodiacal es Escorpio")
    elif dia >= 21 and dia <= 30 and mes == 11:
        print("Tu signo zodiacal es Sagitario")
    elif dia <= 20 and dia >= 1 and mes == 12:
        print("Tu signo zodiacal es Sagitario")
    elif dia >= 21 and dia <= 31 and mes == 12:
        print("Tu signo zodiacal es Capricornio")
    elif dia <= 20 and dia >= 1 and mes == 1:
        print("Tu signo zodiacal es Capricornio")
    elif dia >= 21 and dia <= 31 and mes == 1:
        print("Tu signo zodiacal es Acuario")
    elif dia <= 20 and dia >= 1 and mes == 2:
        print("Tu signo zodiacal es Acuario")
    elif dia >= 21 and dia <= 29 and mes == 2:
        print("Tu signo zodiacal es Piscis")
    elif dia <= 20 and dia >= 1 and mes == 3:
        print("Tu signo zodiacal es Piscis")
    else:
        print("Datos ingresados erroneos")
    print("¿Desea continuar?")
    print("1.- Sí")
    print("2.- No")
    opc = int(input("Ingrese una opción: "))
    if opc == 1:
        continuar = True
    elif opc == 2:
        continuar = False
        print("Hasta luego :)")
    else:
        print("Valor Ingresado Erroneo, fin del programa")