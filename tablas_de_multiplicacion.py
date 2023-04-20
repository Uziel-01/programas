numero = 1

while numero < 13:
    print(f'\nTabla del {numero}:\n')
    for rango in range(13):
        resultado = numero * rango
        print(f'{numero} x {rango} = {resultado}')

    numero += 1