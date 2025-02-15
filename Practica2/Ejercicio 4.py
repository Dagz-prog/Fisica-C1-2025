

"""
Dos pilotos de carritos están separados por 10 m en una pista larga y recta,
mirando en direcciones opuestas. Ambos parten al mismo tiempo y aceleran con
una tasa constante de
2. 0 𝑚/𝑠2 1.0 𝑚/𝑠2
 y
, respectivamente.
a.  ¿Qué separación tendrán los carritos luego de 3.0 s?
b.  ¿Cuánto tiempo le toma a los pilotos toparse en la pista?
c. Realice un programa que permita calcular los incisos a y b recibiendo como
parámetros los 3 datos que se indican en el enunciado

"""

import math


def calcular_separacion_y_tiempo(d0, a1, a2, t):
    # Cálculo de distancias recorridas
    d1 = (1 / 2) * a1 * (t ** 2)
    d2 = (1 / 2) * a2 * (t ** 2)

    # Nueva separación entre los carritos después de cierto tiempo
    D_final = d0 + d1 + d2

    # Cálculo del tiempo en que se encuentran (solo si a1 > a2)
    if a1 > a2:
        t_meet = math.sqrt((2 * d0) / (a1 - a2))
    else:
        t_meet = None  # No se encontrarán si a1 <= a2

    return D_final, t_meet


# Ejemplo de uso
d0 = 10.0  # Separación inicial en metros
a1 = 2.0  # Aceleración del carrito 1 en m/s²
a2 = 1.0  # Aceleración del carrito 2 en m/s²
t = 3.0  # Tiempo en segundos

D_final, t_meet = calcular_separacion_y_tiempo(d0, a1, a2, t)
print(f"Separación después de {t} s: {D_final:.2f} m")
if t_meet:
    print(f"Tiempo para encontrarse: {t_meet:.2f} s")
else:
    print("Los carritos no se encontrarán.")