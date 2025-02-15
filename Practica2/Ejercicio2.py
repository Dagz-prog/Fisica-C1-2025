"""
El cabello corto crece a una tasa aproximada de
2 𝑐𝑚/𝑚𝑒𝑠
 . Un estudiante
universitario se corta el cabello para dejarlo de un largo de 1.5 cm. Se cortará de
nuevo el cabello cuando éste mida 3.5 cm.
a. ¿Cuánto tiempo transcurrirá hasta su siguiente visita al peluquero?.
b. Cree una solución en software que permita realizar dicho cálculo para
cualquier longitud final deseada de cabello. El usuario debe poder elegir las
unidades de tiempo de la respuesta, en tanto estas sean razonables.

"""

def crecimientoCabello(largoActual, largoDeseado, unidad):
    crecimientoNecesario = largoDeseado - largoActual
    crecimientoDeCabello = 2
    if crecimientoNecesario <= 0:
        return "El cabello esta mas largo de lo deseado o esta en el largo deseado"
    #Calculamos el timepo que duro en crecer el pelo en meses
    tiempoMeses = crecimientoNecesario / crecimientoDeCabello

    match unidad:
        case "dias":
            return tiempoMeses * 30
        case "semanas":
            return tiempoMeses * 4.3
        case "meses":
            return tiempoMeses
        case _:
            return "Porfavor use una unidad validad como dias, semanas o meses..."










if __name__ == '__main__':
    print("Para calcular el tiempo estimado que requeire su pelo para crecer al largo deseado porfavor ingrese los siguientes daots: ")
    largoInicial = float(input("Largo inicial de su cabello: "))
    largoFinal = float(input("Largo deseado de su cabello: "))
    unidad = str(input("Unidad en la que desea calcular el tiempo estimado en crecer el cabello (dias, semanas, meses): "))
    tiempo = crecimientoCabello(largoInicial, largoFinal, unidad)

    print("El tiempo estimado es: ", tiempo)