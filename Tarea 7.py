#Patricio Mondragón A01748352


#Esta fución encuentra el numero mayor de una serie de numeros
def encontrarelnumeroMayor():
    numero = int(input("Teclea numeros, [-1] para salir:"))
    numeromayor = 0
    while numero != -1:
        numero = int(input("Teclea numeros, [-1] para salir:"))

        if numero > numeromayor:
            numero = numeromayor


    print("El mayor es ",numerommayor)



# Esta función divide a base de restas
def dividirnumeros(divisor,dividendo):
    cociente = 0
    if divisor == 0:
        print("Error matemático, no se puede dividir entre 0")
    elif dividendo>= divisor:
        while dividendo >= divisor:
            dividendo = dividendo - divisor
            cociente = cociente +1
    else:
        print("El dividendo tiene que ser mayor al divisor.")
    print("El cociente es:",cociente)
    print("El residuo es:",dividendo)







def main():
    print("Mision 07: Ciclos while")
    print("Autor: Patricio Mondragón")
    print("Matricula: A01748352")

    print("1: Función que hace divisiones")
    print("2: Funcion que encuentra el numero mayor de los numeros que teclees")
    print("3: salir")
    opcion = int(input("Teclea tu opcion:"))
    if opcion == 1:
        dividendo = int(input("Teclea el dividendo:"))
        divisor = int(input("Teclea el divisor:"))
        dividirnumeros(divisor,dividendo)
    elif opcion == 2:
        encontrarelnumeroMayor()
    elif opcion == 3:
        print("Termina Programa")







main()