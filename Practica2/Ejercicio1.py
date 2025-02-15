

"""
(20%) La rapidez de un impulso nervioso en el cuerpo humano es de
aproximadamente 100 m/s.
a. Si su dedo del pie tropieza accidentalmente en la oscuridad, estime el
tiempo que tarda el impulso nervioso en viajar a su cerebro.
b. Basándose en su respuesta anterior, realice un pequeño software que
permita calcular el tiempo de manera precisa para cualquier persona.

"""

# este funcion se usara para calcular el tiempo que se toma para el nervio llegar al cerebro
def caluclarTiempo(distancia):
    #El movimineto involucrado es MRU
    # formula de la velocidad = distnacia / tiempo
    # se utiliza para despejar el tiempo = distancia / velocidad
    distancia = float(distancia)
    velocidad = 100
    return (distancia  /velocidad) *1000



if __name__ == '__main__':

#Funcion principal donde se le pedira al usuario que ingrese su estatura o alguna estatura la cual quiera medir.
    estatura = float(input("Escriba la distancia que se espera recorrer en metros (estatura): "))
    tiempoRecorrido = caluclarTiempo(estatura)


    print(f"El tiempo que tarda en recorrer es de: {tiempoRecorrido} milisegundos")





