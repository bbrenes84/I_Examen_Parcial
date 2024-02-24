def calcular_beca(nota):
    if nota >= 95:
        return "¡Felicidades! El estudiante obtiene una beca."
    else:
        return "El estudiante no cumple con el porcentaje mínimo para la beca."

try:
    nota_estudiante = float(input("Ingresa la nota del estudiante (0-100): "))
    if nota_estudiante < 0 or nota_estudiante > 100:
        print("Error: La nota debe estar entre 0 y 100.")
    else:
        print(calcular_beca(nota_estudiante))
except ValueError:
    print("Error: Ingresa un valor numérico válido para la nota.")