#!/usr/bin/env python

# Imprimir en consola
print("show this in the console")

# Para saber que tipo de dato tiene asignado una variable
type(nombreVariable)

# FECHAS
# Se usan fechas para: archivo de copia de seguridad, condición o métrica
from datetime import date
print(date.today())

# Conversión a string
print("Today's date is: " + str(date.today()))

# Conversión a int
print(int(first_number) + int(second_number))

# RECOPILACIÓN DE ENTRADAS
# Entrada de la línea de comandos. Mediante el módulo sys, puede recuperar los argumentos de la línea de comandos y usarlos en el programa
import sys

print(sys.argv)
print(sys.argv[0]) # program name
print(sys.argv[1]) # first arg

# Para capturar información del usuario
print("Welcome to the greeter program")
name = input("Enter your name: ") # input() almacena un resultado como una cadena
print("Greetings " + name)