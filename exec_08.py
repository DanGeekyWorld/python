counter = 0
total = 0
while True:
    categoria = input("Introduce la categoría:")
    
    counter = counter + 1
    if categoria == 'cancelar':
        print('Compra cerrada')
        print('Monto a pagar:',total)
        break
    else:

        precio = float(input("Introduce precio del producto:"))
        cantidad = float(input("Cantidad del producto:"))
        if categoria == 'productos lacteos':
            total += (cantidad*precio - (cantidad*precio*0.10))
            print('Descuento de 10% por Pagar ',total)
        if categoria == 'productos horneados':
            total += (cantidad*precio - (cantidad*precio*0.30))
            print('Descuento de 30% por Pagar ',total)
        else:
            total += cantidad*precio
    
    print('Monto a pagar:',total)
