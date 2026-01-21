import threading
import time

def desayunar():
    print('Tomando desayuno...')
    time.sleep(3)
    print('Finalizando.')

def tomarCafe():
    print('Tomando cafe...')
    time.sleep(4)
    print('Finalizando.')

def estudiar():
    print('Estudianding...')
    time.sleep(5)
    print('Finalizando.')


inicio = time.perf_counter()

x = threading.Thread(target=desayunar, args=())
x.start()
y = threading.Thread(target=tomarCafe, args=())
y.start()
z = threading.Thread(target=estudiar, args=())
z.start()


x.join()
y.join()
z.join()

# desayunar()
# tomarCafe()
# estudiar()

print(threading.active_count())
print(threading.enumerate())

fin = time.perf_counter()
tiempo = fin - inicio
print(tiempo)
