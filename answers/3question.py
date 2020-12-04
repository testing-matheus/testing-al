# librerias
import pandas as pd
from statsmodels.graphics.gofplots import qqplot

import matplotlib.pyplot as plt
# modulo de trabajo
from src.module import ttest


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
# desde la columna precisa realemente
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
