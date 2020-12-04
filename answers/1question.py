import pandas as pd
from pandas import plotting
from module import histograma_columnas


def comments():
    """
    PREGUNTA 1:
    1) Examine los datos de las 80 propiedades residenciales utilizando
    resúmenes estadísticos apropiados. ¿Los datos recopilados sobre las
    80 propiedades residenciales son adecuados para el análisis? Si no es así,
    describa cualquier ajuste que deba realizarse.
    Supuestos: Se hace un analisis pre-eliminar de los datos, del descriptivo
        se aprecia que los ouliers presentes corresponden a terrenos
        abandonados se hace el filtro para eliminar aquellos con
        TAX > 150, en la tarea de regresión no serán utilizados
    Respuesta:
        dataset limpio para el proceso de verificación de pies y metros
    """
    return True


# lectura de los datos
data = pd.read_excel("../data/ryder.xlsx")
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
plotting.scatter_matrix(data, alpha=0.7, figsize=(20,10),
                        ax=None, grid=True, diagonal='hist', marker='*')
# histograma más detallado por variable
histograma_columnas(data)
# verificación de outliers
cleaned = data[data["TAX"] > 150].reset_index(drop=True)
cleaned.to_excel("../data/cleaned.xlsx")
