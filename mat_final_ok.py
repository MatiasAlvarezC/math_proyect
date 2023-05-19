"""""
Desarrollar un software que cumpla los siguientes requerimientos:

Debe contar con un menú que permita seleccionar entre las siguientes opciones:

Rectas paralela y perpendicular a una dada.
Análisis de una función lineal.
Análisis de una función cuadrática.

1) Rectas paralela y perpendicular a una dada: En esta opción el usuario deberá ingresar por teclado el coeficiente principal y el término independiente. 
Se deberá mostrar por pantalla al menos 3 (tres) rectas paralelas y 3 (tres) perpendiculares. 
No se permite que el sistema arroje como resultado de alguna de las consignas la misma recta ingresada por el usuario.
Además como información en pantalla deberá enunciarse la condición de paralelismo y también la de perpendicularidad.
2) Análisis de una recta: En esta opción el usuario deberá ingresar por teclado el coeficiente principal y el término independiente. 
Se deberá mostrar por pantalla la siguiente información: corte con el eje x, corte con el eje y, comportamiento de la recta (creciente o decreciente).
3) Análisis de una parábola: En esta opción el usuario deberá ingresar por teclado el coeficiente principal, el coeficiente lineal y el término independiente.
Se deberá mostrar por pantalla la siguiente  información: corte con el eje x, corte con el eje y, intervalo de crecimiento e intervalo de decrecimiento, coordenadas del vértice, concavidad de la parábola (cóncava hacia arriba o cóncava hacia abajo).
Además deberá informarse en el caso que la parábola no posea soluciones reales como así también cuando la solución tenga doble multiplicidad.
"""
opcion = 0
coePrin = 0
terIndep = 0
paralela1 = 0
paralela2 = 0
paralela3 = 0
corteY = 0
fraccion = 0
fraccion2 = 0
parax = 0
resultado = 0
perpendicular1 = 0
perpendicular2 = 0
perpendicular3 = 0
termCuadratico = 0
termLineal = 0
ejeSimetria = 0
verticeX = 0
verticeY = 0
discriminante = 0
opciones_validas = [1, 2, 3, 4]
bandera = 1

import random
from fractions import Fraction
import math 
#import sys

while bandera == 1:
    while True:
        try:
            opcion = int(input("Seleccione una opción:\n 1-Recta paralela y perpendicular a una dada\n 2-Análisis de una recta\n 3-Análisis de una parábola\n 4-Salir del programa\n"))
            if opcion in opciones_validas:
                break # El usuario ingresó una opción válida, salir del bucle
            else:
                # El usuario ingresó una opción inválida, mostrar mensaje de error y continuar en el bucle
                print("Opción inválida. Intente nuevamente.") # para numeros
        except ValueError:
            # El usuario ingresó algo que no es un número, mostrar mensaje de error y continuar en el bucle
            print("Debe ingresar un número válido. Intente nuevamente.")
    
    if opcion == 1:
        print("Ha elegido la opción 1: Función lineal")
        print("\nCondición de paralelismo: ")
        print("Dos rectas son paralelas si tienen la misma pendiente y diferentes términos independientes.")
        print("--------------------------------------------------------------------------------------------------------------")
        print("Condición de perpendicularidad: ")
        print("Dos rectas son perpendiculares si la pendiente de una recta es el inverso aditivo y multiplicativo de la pendiente de la otra.")
        input("\nOprima Enter para continuar\n")
        coePrin = 0
        terIndep = 0
        while (coePrin == 0):
            coePrin = Fraction(input("Ingrese el coeficiente principal (distinto de 0): "))
        terIndep = (input("Ingrese el termino independiente: "))
        print("\n---------------------------------------")
        print("Su función ingresada es: " + str(coePrin) + "x" + " + (" + str(terIndep) + ")")
        print("---------------------------------------\n") 
        
        paralela1 = random.randint(1,100)
        while(paralela1 == terIndep): # para que no sea igual al termino independiente
            paralela1 = random.randint(1,100)
        print("Recta paralela 1: " + str(coePrin) + "x" + " + " + str(paralela1))

        paralela2 = random.randint(1,100) 
        while(paralela2 == terIndep or paralela2 == paralela1): #paralela 2 diferente a termino indp y a paralela 1
            paralela2 = random.randint(1,100)
        print("Recta paralela 2: " + str(coePrin) + "x" + " + " + str(paralela2))

        paralela3 = random.randint(1,100)
        while(paralela3 == terIndep or paralela3 == paralela2 or paralela3 == paralela1): #paralela 3 diferente a termino inde, paralela 1 y paralela 2
            paralela3 = random.randint(1,100)
        print("Recta paralela 3: " + str(coePrin) + "x" + " + " + str(paralela3))

        print("---------------------------------------")
        #CALCULO PERPENDICULARES
        perpendicular = (1/coePrin)*(-1)   #para calcular el negativo inverso
        independiente1 = random.randint(1,100)
        while(independiente1 == terIndep):
            independiente1 = random.randint(1,100)
        print(("perpendicular 1: ") + str(perpendicular) + "x" + " + " + str(independiente1))
        
        
        independiente2 = random.randint(1,100)
        while(independiente2 == terIndep or independiente2 == independiente1):
            independiente2 = random.randint(1,100)
        print(("perpendicular 2: ") + str(perpendicular) + "x" + " + " + str(independiente2))
        
        
        
        independiente3 = random.randint(1,100)
        while(independiente3 == terIndep or independiente3 == independiente2 or independiente3 == independiente1):
            independiente3 = random.randint(1,100)
        print(("perpendicular 3: ") + str(perpendicular) + "x" + " + " + str(independiente3))
        input("\nOprima una tecla para continuar\n")

        
    elif opcion == 2:
        coePrin = 0
        terIndep = 0
        print("Ha elegido la opción 2: Análisis de una recta")
        while (coePrin == 0):
            coePrin = Fraction(input("Ingrese el coeficiente principal(distinto de 0): "))
        terIndep = Fraction(input("Ingrese el termino independiente: "))
        print("\n---------------------------------------")
        print("Su función ingresada es: " + str(coePrin) + "x" + " + (" + str(terIndep) + ")")
        print("---------------------------------------\n")
            
        fraccion = Fraction(terIndep)
        print("El corte con el eje y es: " + str(fraccion))
        # CORTE CON EL EJE X        x = -b/m
        parax = -terIndep
        fraccion2 = parax / coePrin
        resultado = Fraction(fraccion2) 
        print("El corte con el eje x es: " + str(resultado))

        if (coePrin > 0):
            print ("La recta es creciente")
        elif (coePrin < 0):
            print ("La recta es decreciente")
        input("\nOprima una tecla para continuar\n")

    elif opcion == 3:
        termCuadratico = 0
        termLineal = 0
        terIndep = 0
        print("Ha elegido la opción 3: Análisis de una parábola")
        # SOLICITUD DATOS
        while (termCuadratico == 0):
            termCuadratico = Fraction(input("Ingrese el término cuadrático (distinto de 0): "))
        termLineal = Fraction(input("Ingrese el coeficiente principal: "))
        terIndep = Fraction(input("Ingrese el termino independiente: "))
        print("\n---------------------------------------")
        print("Su función ingresada es: (" + str(termCuadratico) + "x)\u00B2" + " + (" + str(termLineal) + "x)"+ " + (" + str(terIndep) + ")") #u000B2 es al cuadrado
        print("---------------------------------------\n")
        # CALCULO DISCRIMINANTE
        discriminante = termLineal**2 - (4*float(termCuadratico)*terIndep)  #   Δ = b*2 - 4.a.c   
        
        if(discriminante > 0):  #aplicamos baskhara
            corteX1 = (-termLineal + math.sqrt(discriminante)) / (2*float(termCuadratico))  #match.sqrt raiz cuadrada x1 = (-b +sqrt(b**2-(4*a*c)))/(2*a)
            print("La ecuación tiene dos soluciones reales: ")  
            print("x1: " + str(corteX1))
            corteX2 = (-termLineal - math.sqrt(discriminante)) / (2*float(termCuadratico))
            print("x2: " + str(corteX2))
            print("\n")

        if(discriminante == 0):
            corteX1 = (-termLineal + math.sqrt(discriminante)) / (2*float(termCuadratico))
            print("La ecuación tiene exactamente una solucion real (doble multiplicidad): " + str(corteX1))
            print("\n")

        if(discriminante < 0):
            print("La ecuación no tiene soluciones reales.")
            print("\n")

        # PUTNO DE CORTE EN Y
        y = terIndep
        print("Punto de corte en el eje y: " + str(y)) 
        print("\n")
        # COORDENADAS DEL VERTICE
        verticeX = (-termLineal) / (2*termCuadratico)  # -b / 2*a
        verticeX = Fraction(verticeX)
        verticeY = (verticeX**2) + (termLineal * verticeX) + terIndep   # reemplazo verticeX en la funcion
        verticeY = Fraction(verticeY)
        print("Coordenadas del vértice: (" + str(verticeX) + ", " + str(verticeY) + (")"))
        print("\n")

        # INTERVALO CRECIMIENTO 
        if(termCuadratico > 0):
            print("Intervalo de decrecimiento: (-∞, " + str(verticeX) + ")")
            print("Intervalo de crecimiento: (" + str(verticeX) + ", ∞)")
            print("\n")
        else:
            print("Intervalo de crecimiento: (-∞, " + str(verticeX) + ")")
            print("Intervalo de decrecimiento: (" + str(verticeX) + ", ∞)")
            print("\n")
        # CONCAVIDAD 
        if(termCuadratico > 0):
            print("La parábola es cóncava positiva con ramas hacia arriba ")
        else:
            print("La parábola es cóncava negativa con ramas hacia abajo ")
        input("\nOprima una tecla para continuar\n")

    elif opcion == 4:
        print("Programa finalizado")
        bandera = 0
        break
        #sys.exit()