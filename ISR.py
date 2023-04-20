
articulo = (input('ingrese el el articulo: '))
precio_art = float(input('ingrese el precio: '))
cantidad_art = int(input('ingrese la cantidad de los articulos: '))
total = precio_art*cantidad_art


if articulo=='leche':
    print('el articulo no paga impuesto')
    print('el precio a pagar es : ',total )

else:

    ITBS = total*0.18
    print('el itbs a pagar es',ITBS)
    print('el total a pagar es', ITBS+total)