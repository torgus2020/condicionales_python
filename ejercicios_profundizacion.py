#!/usr/bin/env python
'''
Condicionales [Python]
Ejercicios de profundización
---------------------------
Autor: Inove Coding School
Version: 1.3

Descripcion:
Programa creado para que practiquen los conocimietos adquiridos durante la semana
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.3"


def ej1():
    print('Ejercicios de práctica con números')

    '''
    Realice un programa que solicite por consola 2 números
    Calcule la diferencia entre ellos e informe por pantalla
    si el resultado es positivo, negativo o cero.
    '''
    numero_1 = int(input('Ingrese el primer número:\n'))

    numero_2 = int(input('Ingrese el segundo número:\n'))

    resta = numero_1 - numero_2

    if resta > 0:
        print("la diferencia entre los numeros es positiva")
    elif resta < 0:
        print("la diferencia entre los numeros es negativa")
    else:
        print("los numeros son iguales")



def ej2():
    print('Ejercicios de práctica con números')

    '''
    Realice un programa que solicite el ingreso de tres números
    enteros, y luego en cada caso informe si el número es par
    o impar.
    Para cada caso imprimir el resultado en pantalla.
    '''
    numero_1 = int(input('Ingrese el primer número:\n'))

    numero_2 = int(input('Ingrese el segundo número:\n'))

    numero_3 = int(input('Ingrese el tercer número:\n'))

    if numero_1 % 2 == 0:
        print(numero_1, "es par")
    else:
        print(numero_1, "es inpar")

    if numero_2 % 2 == 0:
        print(numero_2, "es par")
    else:
        print(numero_2, "es inpar")

    if numero_3 % 2 == 0:
        print(numero_3, "es par")
    else:
        print(numero_3, "es inpar")

def ej3():
    print('Ejercicios de práctica con números')

    '''
    Realice una calculadora, se ingresará por línea de comando dos números
    Luego se ingresará como tercera entrada al programa el símbolo de la operación
    que se desea ejecutar
    - Suma (+)
    - Resta (-)
    - Multiplicación (*)
    - División (/)
    - Exponente/Potencia (**)

    Se debe efectuar el cálculo correcto según la operación ingresada por consola
    Imprimir en pantalla la operación realizada y el resultado
    '''
    numero_1 = int(input('Ingrese el primer número:\n'))

    numero_2 = int(input('Ingrese el segundo número:\n'))

    simbolo_1 = input("que operación quiere hacer")
    
    suma = numero_1 + numero_2
    resta = numero_1 - numero_2
    multi = numero_1 * numero_2
    divi = numero_1 / numero_2
    potencia = numero_1 ** 2
    
    print("elegiste los numeros", numero_1, "y", numero_2, "y la operación", simbolo_1, "entonces el resultado es")
    
    if simbolo_1 == "+":
        print(suma)
    elif simbolo_1 == "-":
        print(resta)
    elif simbolo_1 == "*":
        print(multi)
    elif simbolo_1 == "/":
        print(divi)
    else:
        print(potencia)

def ej4():
    print('Ejercicios de práctica con cadenas')

    '''
    Realice un programa que solicite por consola 3 palabras cualesquiera
    Luego el programa debe consultar al usuario como quiere ordenar las palabras
    1 - Ordenar por orden alfabético (usando el operador ">")
    2 - Ordenar por cantidad de letras (longitud de la palabra)

    Si se ingresa "1" por consola se deben ordenar las 3 palabras por orden alfabético
    e imprimir en pantalla de la mayor a la menor

    Si se ingresa "2" por consola se deben ordenar las 3 palabras por cantidad de letras
    e imprimir en pantalla de la mayor a la menor
    '''
    palabra_1 = input("insterta la 1er palabra:\n")
    palabra_2 = input("insterta la 2da palabra:\n")
    palabra_3 = input("insterta la 3er palabra:\n")
    orden = int(input("ingresa 1 si queres ordenar alfabeticamente o 2 si queres orden por longitud:\n"))
    if orden == 1:
        print("Elegiste ordenar alfabeticamente")
    else:
        print("Elegiste ordenar por largo de letras")

    if orden == 1:
        if palabra_1 > palabra_2 and palabra_2 > palabra_3:
            print(palabra_3, "esta 1ro,", palabra_2, "esta 2do y", palabra_1, "3ro")
        elif palabra_1 > palabra_3 and palabra_3 > palabra_2:
            print(palabra_2, "esta 1ro,", palabra_3, "esta 2do y", palabra_1, "3ro")
        elif palabra_2 > palabra_1 and palabra_1 > palabra_3:
            print(palabra_3, "esta 1ro,", palabra_1, "esta 2do y", palabra_2, "3ro")
        elif palabra_2 > palabra_3 and palabra_3 > palabra_1:
            print(palabra_1, "esta 1ro,", palabra_3, "esta 2do y", palabra_2, "3ro")
        elif palabra_3 > palabra_1 and palabra_1 > palabra_2:
            print(palabra_2, "esta 1ro,", palabra_1, "esta 2do y", palabra_3, "3ro")
        else:
            print(palabra_1, "esta 1ro,", palabra_2, "esta 2do y", palabra_3, "3ro")
    else:
        if len(palabra_1) > len(palabra_2) and len(palabra_2) > len(palabra_3):
            print("el orden por largo de letras es:", palabra_1, palabra_2, palabra_3)
        elif len(palabra_1) > len(palabra_3) and len(palabra_3) > len(palabra_2):
            print("el orden por largo de letras es:", palabra_1, palabra_3, palabra_2)
        elif len(palabra_2) > len(palabra_1) and len(palabra_1) > len(palabra_3):
            print("el orden por largo de letras es:", palabra_2, palabra_1, palabra_3)
        elif len(palabra_2) > len(palabra_3) and len(palabra_3) > len(palabra_1):
            print("el orden por largo de letras es:", palabra_2, palabra_3, palabra_1)
        elif len(palabra_3) > len(palabra_1) and len(palabra_1) > len(palabra_2):
            print("el orden por largo de letras es:", palabra_3, palabra_1, palabra_2)
        else:
            print("el orden por largo de letras es:", palabra_3, palabra_2, palabra_1)
    


def ej5():
    print('Ejercicios de práctica con números')

    '''
    Realice un programa que solicite ingresar tres valores de temperatura
    De las temperaturas ingresadas por consola determinar:
    1 - ¿Cuáles de ellas es la máxima temperatura ingresada?
    2 - ¿Cuáles de ellas es la mínima temperatura ingresada?
    3 - ¿Cuál es el promedio de las temperaturas ingresadas?

    En cada caso imprimir en pantalla el resultado
    '''
    

    temp_1 = int(input("ingrese la 1er toma de temperatura:\n"))
    temp_2 = int(input("ingrese la 1er toma de temperatura:\n"))
    temp_3 = int(input("ingrese la 1er toma de temperatura:\n"))

    if temp_1 > temp_2 and temp_1 > temp_3:
        print(temp_1, "es la tempertura máxima")
    elif temp_2 > temp_1 and temp_2 > temp_3:
        print(temp_2, "es la temperatura máxima")
    else:
        print(temp_3, "es la temperatura máxima")
    
    if temp_1 < temp_2 and temp_1 < temp_3:
        print(temp_1, "es la tempertura mínima")
    elif temp_2 < temp_1 and temp_2 < temp_3:
        print(temp_2, "es la temperatura mínima")
    else:
        print(temp_3, "es la temperatura mínima")
    


    temperaturas = [temp_1, temp_2, temp_3] 
    suma = 0
    contador = 0 
    
    for elemento in temperaturas:
        suma += elemento
        contador += 1
    
    promedio = suma / contador
    print("el promedio de las temperaturas es:", promedio)
    

if __name__ == '__main__':
    print("Ejercicios de práctica")
    #ej1()
    #ej2()
    #ej3()
    #ej4()
    ej5()
