# librerias
import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error
# module
from src.module import (regression_lineal_lasso, graficar_resultados,
                        alpha_lasso_optimization)

# cargamos la data ya limpiada
x = pd.read_excel("data/cleaned.xlsx", index_col=0)

y = x[["FIXED_TAX"]]
x = x[['ACT_SQFT']]

get_alpha = alpha_lasso_optimization(x, y)
print(get_alpha)


# Regresión lineal por lasso
reg_lasso, mae, coeficientes = regression_lineal_lasso(x,
                                                       y,
                                                       alpha=get_alpha)
print(coeficientes)
print("MAE", mae)
y_pred_lasso = reg_lasso.predict(x)
graficar_resultados(y, y_pred_lasso,
                    titulo=f"Resultados Regresión: LASSO, MAE: {round(mae)}")
print("Suma de la predicción", y_pred_lasso.sum())
print("Suma de variable real", y.sum())

mse = mean_squared_error(y, y_pred_lasso)
diff = np.abs(y_pred_lasso.reshape(-1, 1) - y.to_numpy())
std_error = diff.std()
max_error = diff.max()
error_abs_total = diff / y * 100

error_absoluto = error_abs_total.mean()
error_absoluto_max = error_abs_total.max()
