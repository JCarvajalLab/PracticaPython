try:
    numerador = int(input("Ingresa un numero: "))
    denominador = int(input("Ingresa un numero: "))
    resultado = numerador / denominador
    print(resultado)

except ZeroDivisionError as e:
    print(e)
    print("No puedes dividir por 0")

except ValueError:
    print("ingresa solo numeros")
# except Exception:
#     print("Algo salio mal")
