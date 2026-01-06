comida = ['pizza', 'suchi', 'hamburguesa', 'spaggetis'] ## tambien se pueden almacenar numeros, decimales y booleanos [1, 0.5, false]

comida[2] = 'helado'

comida.append('completo') ## agregar un elemento al final de la lista
comida.remove('completo') ## elimina un elemento de la lista
comida.pop() ##Elimina el ultimo elemento de la lista
comida.insert(0, "Pastel") ## se cambia un objeto de la lista en la posicion que necesitemos
comida.sort() ##ordena la lista alfabeticamente
comida.clear() ##se limpia la lista


for x in comida:
    print(x)

# print(comida[2])