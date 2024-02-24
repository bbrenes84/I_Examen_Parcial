# Lista de Contactos

class Contacto:
    def __init__(self, nombre, telefono):
        self.nombre = nombre
        self.telefono = telefono

def agregar_contacto(agenda):
    nombre = input("Ingresa el nombre del contacto: ")
    telefono = input("Ingresa el teléfono del contacto: ")
    nuevo_contacto = Contacto(nombre, telefono)
    agenda[nombre] = nuevo_contacto

def mostrar_agenda(agenda):
    print("\nAgenda de contactos:")
    for nombre, contacto in agenda.items():
        print(f"{nombre}: {contacto.telefono}")

def main():
    agenda = {}  

    while True:
        print("\nSelecciona una opción:")
        print("1. Agregar contacto")
        print("2. Mostrar agenda")
        print("3. Salir")

        opcion = input("Ingresa el número de la opción deseada: ")

        if opcion == "1":
            agregar_contacto(agenda)
        elif opcion == "2":
            mostrar_agenda(agenda)
        elif opcion == "3":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, selecciona una opción válida (1-3).")

if __name__ == "__main__":
    main()