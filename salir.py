
numero1 = int(input('ingrese un numero: '))

numero2 = int(input('ingrese otro numero: '))

while True:
    
    if numero1 > numero2:
        print(f'{numero1} es mayor que {numero2}')
    

    if numero1 < numero2:
        print(f'{numero2} es mayor que {numero1}')

    if numero1 == numero2:
        print(f'{numero1} es igual a {numero2}')
    
    print("1- Continuar  \n 2- Salir ")

    opcion=int(input("Elija si quiere salir o continuar el programa: "))

    if opcion == 1:
         numero1 = int(input('ingrese un numero: '))

         numero2 = int(input('ingrese otro numero: '))

    
    if opcion == 2: 
        print("Gracias por utilizar mi programa")
        exit()