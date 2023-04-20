intentos = 0
factorial = 1
continuar = True

while continuar == True:
    
    numero = int(input('ingrese un numero entero: '))

    if numero >0:
     for i in range(1,numero+1):
         factorial=factorial*i
     print(f'El factorial de {numero} es {factorial}')
     break
      
    
    if numero < 0:
        print('El factorial no puede ser negativo')
        intentos += 1 
        print(f'tiene {intentos} intentos')
        if intentos == 4:
            print('Error, numero maximo de intentos')
        
        while intentos == 4:
            continuar == False
        
    
    
    if numero == 0:
        print('El factorial de 0 es 1')
        break
