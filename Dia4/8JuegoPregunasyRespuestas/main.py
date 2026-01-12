#-------------------------------------
def newGame():
    respuestas = []
    respuestaCorrecta = 0
    preguntaNum = 0

    for key in preguntas:
        print("*****************************")
        print(key)
        for i in opciones[preguntaNum]:

            print(i)

        respuesta = input('Ingresa (A, B, C, D): ').upper()
        respuestas.append(respuesta)

        respuestaCorrecta += checkAnswe(preguntas.get(key), respuesta)


        preguntaNum += 1
    
    displayScore(respuestaCorrecta, respuestas)

#-------------------------------------
def checkAnswe(respuestaCorrecta, respuesta):
    if respuestaCorrecta == respuesta:
        print('Correcto!')
        return 1
    else:
        print('Incorrecto')
        return 0
        
#-------------------------------------
def displayScore(respuestaCorrecta, respuesta):
    print('*****************************')
    print('Resultado')
    print('*****************************')
    print('Respuestas correctas: ', end="")
    for i in preguntas: 
        print(preguntas.get(i), end=" ")
    print()

    print('Tus Respuestas: ', end="")
    for i in respuesta: 
        print(i, end=" ")
    print()

    puntaje = int((respuestaCorrecta/len(preguntas))*100)
    print('puntaje: ' + str(puntaje) + '%')
#-------------------------------------
def playAgain():
    respuesta = input('Quieres volver a jugar? (SI/NO): ').upper()

    if respuesta == 'SI':
        return True
    else:
        return False


preguntas = {
    'Que idioma se habla en brasil?: ': 'A',
    'Cual es el oceano mas grande del mundo?: ': 'B',
    'Cual es la estrella mas cercana a la tierra?: ': 'C',
    'Cual es el segundo pais mas grande del mundo?: ': 'A'
}

opciones = [
    ['A. Portugues', 'B. Espanol', 'C. Brasilero', 'D. Ingles'],
    ['A. Atlantico', 'B. Pacifico', 'C. Artico', 'D. Indico'],
    ['A. La Luna', 'B. Alfa centauri', 'C. El sol', 'D. Ninguna'],
    ['A. Canada', 'B. Rusia', 'C. EE.UU.', 'D. China'],
]

newGame()

while playAgain():
    newGame()
print("Adios!!")