import pandas as pd
from pandas import plotting
from src.module import (histograma_columnas, dependiente_superficie)


# lectura de los datos
data = pd.read_excel("data/ryder.xlsx")
# imprimir head
print(data.head(10))
# tipo de valores --> todos enteros y flotantes
print(data.dtypes)
# verificación de nulos (nans)
nulos = data.isna().sum()
print(nulos)
# describe
describe = data.describe()
print(describe)
# plot de los datos
plotting.scatter_matrix(data, alpha=0.7, figsize=(20, 10),
                        ax=None, grid=True, diagonal='hist', marker='*')
# histograma más detallado por variable
histograma_columnas(data)
# verificación de outliers
cleaned = data[data["TAX"] > 150].reset_index(drop=True)
# TAX únicamente dependiente de los pies construidos
cleaned["FIXED_TAX"] =\
    cleaned.apply(lambda x:
                  dependiente_superficie(x["HSX"], x["RET"], x["TAX"]),
                  axis=1)
cleaned.to_excel("data/cleaned.xlsx")
