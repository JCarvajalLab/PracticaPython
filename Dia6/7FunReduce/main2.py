import functools

factorial = [5,4,3,2,1]
# factorial = [5*4,3,2,1]
# factorial = [20*3,2,1]
# factorial = [60*2,1]
# factorial = [120*1]
# factorial = [120]
resultado = functools.reduce(lambda x,y: x*y, factorial)

print(resultado)