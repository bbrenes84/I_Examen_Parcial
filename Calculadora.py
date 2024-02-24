# Calculadora básica en Python
import os

def sum(a, b):
    return a + b

def rest(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    return a / b
  
# Opciones de calculo
try:
    os.system("cls || clear")
except:
    print("Error")
print("Selecciona una operación:")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")

opcion = int(input("Ingresa el número de la operación deseada: "))

num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

if opcion > 4:
    print("Opción no válida. Por favor, selecciona una opción válida (1-4).")
elif opcion == 1:
    print(f"Resultado de la suma: {sum(num1, num2)}")
elif opcion == 2:
    print(f"Resultado de la resta: {rest(num1, num2)}")
elif opcion == 3:
    print(f"Resultado de la multiplicación: {multiplication(num1, num2)}")
elif opcion == 4:
    print(f"Resultado de la división: {division(num1, num2)}")
else:
    print(f"Digite una opción")