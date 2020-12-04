# librerias
import pandas as pd
from statsmodels.graphics.gofplots import qqplot

import matplotlib.pyplot as plt
# modulo de trabajo
from src.module import ttest


def comments_():
    """
    PREGUNTA 3:
    3) Analísis estadístico para determinar si el el promedio es diferente
    de la muestra al real

    Suposiciones:
        - Se asume la última medición hecha muy precisamente
        - Que corresponde a la media


    Respuesta:
        Dado los intervalos de confianza tanto de la columna DIFF
        (diferencia entre BD y medición actual) como del error relativo son
        son muy bajas, con un intervalo e confianza al 99%
        Error absoluto =  1.606 (+-) 0.289 % --> máx error  3.779 %
        Error medio = 30.803 (+-) 6.068
        Avanzamos a la medición.

        Fallamos en aceptar el ttest sobre la base de datos, no tenemos
        suficiente evidencia para aceptar la hipotesis de la muestra de la
        base de datos su media es igual a la de la real

        La recomendación entregada sería no utilizar los datos que actualmente
        en la base de datos para medir la proxima etapa en donde se va
        a estimar la cantidad fija y variable del costo

    """
    return True


# lectura de los datos
data = pd.read_excel("data/ryder.xlsx")
# media base de datos
mu_bd = data["REC_SQFT"].mean()
# medida muy precisamente
mu_act = data["ACT_SQFT"].mean()

# distribuciones --> pinta de ser normales, hagamos qqplot
# data["REC_SQFT"].hist()
# data["ACT_SQFT"].hist()

# hacemos graficos cuantil cuantil para ver que tan cerca están los datos
# de una distribución normal (normal estimada)

# desde la base de datos
qqplot(data["REC_SQFT"], line='r')
plt.title('qqplot ')
plt.show()

# test
alpha = ttest(data["REC_SQFT"], mu_act)
condicion_aceptacion = 0.05

if alpha > condicion_aceptacion:
    print("Fallamos en aceptar la hipotesis, no tenemos suficiente evidencia")
else:
    print("Se acepta la hipotesis")
