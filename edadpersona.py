# edad de una persona tomando en cuenta el año de nacimiento 
import os
os.system("cls")

def calcEdad(añoNac):
    return 2024-añoNac

def evalEdad(edad):
    if edad>=18:
        return "Mayor de edad"
    else:
        return"Menor de edad"
    
def main():

    añoNac = eval(input("Enque año naciste:"))

    print("tu edad es",calcEdad(añoNac),"tu eres",evalEdad(calcEdad(añoNac)))  

main()  