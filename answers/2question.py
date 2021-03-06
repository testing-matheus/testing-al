# librerias
import pandas as pd
import numpy as np
# modulo de trabajo
from src.module import calcular_intervalo_confianza


# lectura de los datos
data = pd.read_excel("data/ryder.xlsx")

# ERROR DE MEDICIÓN
# diffrencia entre la BD y la medición para el feature de pies de la casa
data["DIFF"] = data["REC_SQFT"] - data["ACT_SQFT"]
data["DIFF_ABS"] = np.abs(data["REC_SQFT"] - data["ACT_SQFT"])
# eliminación de los nans (sitios vacios sin habitación)
data.dropna(inplace=True)
# media y desviación del error absoluto
media = data["DIFF_ABS"].mean()
desv = data["DIFF_ABS"].std()

# # histograma de la variable diff --> ver que muy normal
# hist1 = data["DIFF"].hist(bins=15)
print("La impresición absoluta es:", round(media, 3))
print("La desviación típica del error es:", round(desv, 3))

# INTERVALOS DE CONFIANZA DE LOS ERRORES Y ERRORES RELATIVOS
# calculamos el intervalo de confianza de la columna DIFF
x_barra, l_inferior, l_superior =\
    calcular_intervalo_confianza(data, columna="DIFF_ABS", confianza=0.99)
# Intervalo de confianza de la columna DIFF_ABS
print("El intervalo de confianza con alpha=0.95 de la columna DIFF es:",
      round(x_barra, 3), "(+-)", round(l_superior - x_barra, 3))

# Errores relativos
data["ERROR_RELATIVO"] = np.abs((data["REC_SQFT"] -
                                 data["ACT_SQFT"])) / data["ACT_SQFT"] * 100
# eliminación de los nans (sitios vacios sin habitación)
data.dropna(inplace=True)
# bordes inferiores y superiores del error relativo
x_barra, l_inferior, l_superior =\
    calcular_intervalo_confianza(data, columna="ERROR_RELATIVO",
                                 confianza=0.99)
# Intervalo de confianza de la columna DIFF_ABS
print("El intervalo de confianza con alpha=0.95 de",
      "la columna ERROR_RELATIVO es:",
      round(x_barra, 3), "(+-)", round(l_superior - x_barra, 3),
      "Máximo error: ", round(data["ERROR_RELATIVO"].max(), 3))

# historgrama del error relativo
hist2 = data["ERROR_RELATIVO"].hist()
