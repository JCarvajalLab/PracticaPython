import time

# print(time.ctime(1000000))
# print(time.time())
# print (time.ctime(time.time()))

# tiempoActual = time.localtime()
# print(tiempoActual)


# tiempoActual = time.localtime()
# tiempo = time.strftime("%B %d %y %H:%M:%S", tiempoActual)
# print(tiempo)

# tiempoActual= time.gmtime()
# tiempo = time.strftime("%B %d %y %H:%M:%S", tiempoActual)
# print(tiempo)

# cadenaTiempo = '21 January, 2026'
# tiempo = time.strptime(cadenaTiempo, '%d %B, %Y')
# print(tiempo)

# tiempoTupla = (2026, 1, 14, 4, 20, 0, 0, 0, 0)
# cadenaTiempo = time.asctime(tiempoTupla)
# print(cadenaTiempo)

tiempoTupla = (2026, 1, 14, 4, 20, 0, 0, 0, 0)
cadenaTiempo = time.mktime(tiempoTupla)
print(cadenaTiempo)