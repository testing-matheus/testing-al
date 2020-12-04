# librerias
import random
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
# module
from src.module import (regression_lineal_lasso, graficar_resultados,
                        lasso_lars, alpha_lasso_optimization)


def comments_():
    """
    PREGUNTA 3:
    4) Encontrar los coefs de la regresión

    Suposiciones:
        Se considera el supuesto que la muestra es ALEATORIA (variables
        aleatorias independientes e idénticamente distribuidas)-->
        DIST Normal (podemos usar t. central del límite para estimar
                     intervalos de confianza)

    Respuesta:
        Dado los intervalos de confianza tanto de la columna DIFF
        (diferencia entre BD y medición actual) como del error relativo son
        son muy bajas, con un intervalo e confianza al 99%
        Error absoluto =  1.606 (+-) 0.289 % --> máx error  3.779 %
        Error medio = 30.803 (+-) 6.068
        Avanzamos a la medición.

    """
    return True


raw_data = pd.read_excel("data/ryder.xlsx")
x = pd.read_excel("data/cleaned.xlsx", index_col=0)

y = x[["TAX"]]
x = x[['ACT_SQFT']]

# Crear objecto scaler
scaler = MinMaxScaler(feature_range=(0, 1))
# Normalizar
x = scaler.fit_transform(x)
# # Guardar objeto scaler
seed = random.randint(1, 21)
# Dividir los conjuntos de datos
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2,
                                                    random_state=20)

get_alpha = alpha_lasso_optimization(x, y)
print(get_alpha)

# Regresión lineal por lasso
reg_lasso, mae, coeficientes = regression_lineal_lasso(x_train,
                                                       y_train,
                                                       alpha=get_alpha)
print(coeficientes)
print("MAE", mae)
y_pred_lasso = reg_lasso.predict(x_test)
graficar_resultados(y_test, y_pred_lasso,
                    titulo=f"Resultados Regresión: LASSO, MAE: {round(mae)}")


# Regresión lineal por lasso lars
reg_lars, mae, coeficientes = lasso_lars(x_train, y_train, alpha=get_alpha)
print(coeficientes)
y_pred_lars = reg_lars.predict(x_test)
graficar_resultados(y_test, y_pred_lars,
                    titulo=f"Resultados Regresión: LASSO LARS, MAE: {round(mae)}")
