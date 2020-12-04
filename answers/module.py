import numpy as np
import scipy as sp
import scipy.stats
from sklearn.linear_model import Lasso
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import linear_model
from numpy import arange
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import RepeatedKFold


def graficar_resultados(y, y_pred, titulo="Resultados Regresión"):
    """
    Plot de los resultados

    Parameters
    ----------
    x : TYPE
        DESCRIPTION.
    y : TYPE
        DESCRIPTION.
    model_name : TYPE, optional
        DESCRIPTION. The default is "Resultados Regresión".

    Returns
    -------
    None.

    """
    fig, ax = plt.subplots(1, figsize=(18, 10))
    plt.scatter(y, y_pred, color='blue')
    plt.scatter(y, y, color='red')
    plt.title(titulo, fontsize=25)
    plt.xlabel('TAX: Reales', fontsize=20)
    plt.ylabel('Predicción', fontsize=20)
    ax.tick_params(axis='both', which='major', labelsize=15)
    plt.legend(["TAX: Reales", "Predicción"], fontsize=15,
               loc="lower right")
    plt.ylim(900, 1350)
    plt.xlim(900, 1350)
    plt.show()


def lasso_lars(x, y, alpha=0.001):
    """
    Lasso lars implementación

    Parameters
    ----------
    x : TYPE
        DESCRIPTION.
    y : TYPE
        DESCRIPTION.
    aa : TYPE, optional
        DESCRIPTION. The default is 0.001.

    Returns
    -------
    reg : TYPE
        DESCRIPTION.
    TYPE
        DESCRIPTION.

    """
    reg = linear_model.LassoLars(alpha=alpha)
    reg.fit(x, y)
    predict = reg.predict(x)
    y = y.to_numpy()
    mae = abs(y - predict).mean()
    coeficientes = reg.coef_[0]
    intercept = reg.intercept_[0]
    coeficientes = [coeficientes, intercept]
    return reg, mae, coeficientes


def histograma_columnas(X):
    """
    Generar histograma de las variables
    Parameters
    ----------
    X : dataframe
        DESCRIPTION.
    Returns
    -------
    None.
    """

    for columna in X.columns:
        # print(columna)
        fig, ax = plt.subplots(1, figsize=(16, 8))
        sns.set_context("paper",
                        rc={"font.size": 20, "axes.titlesize": 20,
                            "axes.labelsize": 20})
        x0 = X[columna]
        sns.distplot(x0, color='k')
        ax.set_title(f'Histograma de la variable {columna}',
                     fontname="Arial", fontsize=25)
        plt.legend(labels=[f'Distribución variable {columna}'],
                   ncol=1, loc='upper left',
                   fontsize=20)
        for tick in ax.get_xticklabels():
            tick.set_fontsize(16)
        for tick in ax.get_yticklabels():
            tick.set_fontsize(16)


def calcular_intervalo_confianza(data, columna="DIFF", confianza=0.95):
    """
    Calculamos el intervalo de confianza de la columna DIFF

    Parameters
    ----------
    data : dataframe
        Muestra.
    columna : TYPE, string
        Columna de aplicación. The default is "DIFF".
    confianza : TYPE, int
        Intervalo de confianza. The default is 0.95.
    Returns
    -------
    m : TYPE
        DESCRIPTION.
    TYPE
        DESCRIPTION.
    TYPE
        DESCRIPTION.

    """
    a = np.array(data[columna])
    n = len(a)
    m, se = np.mean(a), scipy.stats.sem(a)
    h = se * sp.stats.t._ppf((1 + confianza) / 2., n - 1)
    return m, m-h, m+h


def alpha_lasso_optimization(x, y):
    """
    Seleccionar el parámetro alpha de la regesión por lasso

    Parameters
    ----------
    x : TYPE
        DESCRIPTION.
    y : TYPE
        DESCRIPTION.

    Returns
    -------
    TYPE
        DESCRIPTION.

    """
    # definri modelo
    model = Lasso()
    # criterios de evaluacion
    cv = RepeatedKFold(n_splits=10, n_repeats=5, random_state=1)
    # define grid
    grid = dict()
    grid['alpha'] = arange(0, 1, 0.01)
    # definir busqyeda
    search = GridSearchCV(model, grid,
                          scoring='neg_mean_absolute_error',
                          cv=cv, n_jobs=-10)
    # fit
    results = search.fit(x, y)
    return results.best_params_["alpha"]


def linear_regression_constraint(x, y):
    """
    Regressión lineal con los parámetros restringidos para que siempre sean
    mayores a cero
    Parameters
    ----------
    x : TYPE
        DESCRIPTION.
    y : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    reg = Lasso(alpha=0.0001, precompute=True, max_iter=1000,
                fit_intercept=True,
                positive=False, random_state=9999, selection='random')
    reg.fit(x, y)
    predict = reg.predict(x)
    y = y.to_numpy()
    mae = abs(y - predict).mean()
    coeficientes = reg.coef_
    return reg, mae, coeficientes


def regression_lineal_lasso(x, y, alpha=0.001):
    """
    Regressión lineal con los parámetros restringidos para que siempre sean
    mayores a cero
    Parameters
    ----------
    x : TYPE
        DESCRIPTION.
    y : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    reg = Lasso(alpha=alpha, max_iter=100000)
    reg.fit(x, y)
    predict = reg.predict(x)
    y = y.to_numpy()
    mae = abs(y - predict).mean()
    coeficientes = reg.coef_[0]
    intercept = reg.intercept_[0]
    coeficientes = [coeficientes, intercept]
    return reg, mae, coeficientes


def ttest(serie, mu):
    """
    Ejemplo
    H0: µ = 15 (el promedio es este mostrado)
    HA: µ ≠15 (el promedio NO ES este mostrado)

    Parameters
    ----------
    serie : pandas series
        la serie de la base de datos que queremos analizar.
    mu : TYPE
        media esperada.
    Returns
    -------
    TYPE
        alpha del test para aceptar o rechazar hipotesis.

    """
    alpha2 = stats.ttest_1samp(serie, mu)[1]
    return alpha2
