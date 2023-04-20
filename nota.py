print('Programa para evaluar una calificación')

nota = int(input('favor ingrese su nota: '))

while nota<0 or nota>=100:
    print('Error, el numero debe ser del 1 al 100')
    nota = int(input('favor ingrese su nota: '))

if nota >=90 and nota <100:
    print('Excelente')

elif nota>=80:
    print('bueno')

elif nota>=70:
    print('regular')

else:
    print('Materia reprobada')