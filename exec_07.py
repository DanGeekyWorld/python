from multiprocessing.managers import SharedMemoryManager

promMensual = float(input('Ingreso promedio mensual: '))
numhrasTrabajadas = float(input('Numero de Horas trabajadas en fin de semana: '))
bono = promMensual*0.01*numhrasTrabajadas
print(bono)