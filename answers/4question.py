# librerias
import random
import pandas as pd
# from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
# module
from src.module import (regression_lineal_lasso, graficar_resultados,
                        lasso_lars, alpha_lasso_optimization)


# cargamos la data ya limpiada
x = pd.read_excel("data/cleaned.xlsx", index_col=0)

y = x[["FIXED_TAX"]]
x = x[['ACT_SQFT']]

# Crear objecto scaler
# scaler = MinMaxScaler(feature_range=(0, 1))
# # Normalizar
# x = scaler.fit_transform(x)

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
print("Suma de la predicción", y_pred_lasso.sum())
print("Suma de variable real", y_test.sum())


# Regresión lineal por lasso lars
reg_lars, mae, coeficientes = lasso_lars(x_train, y_train, alpha=get_alpha)
print(coeficientes)
y_pred_lars = reg_lars.predict(x_test)
graficar_resultados(y_test, y_pred_lars,
                    titulo=f"Resultados Regresión: LASSO LARS, MAE: {round(mae)}")
print("Suma de la predicción", y_pred_lasso.sum())
print("Suma de variable real", y_test.sum())
