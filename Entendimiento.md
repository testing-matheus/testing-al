# Repo de testing de cosas
[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

###  1) Entendimiento del problema:

- RAD: Agencia responsable de los impuestos a la propiedad.
- 12.000 propiedades en el condado, de los cuales tenemos una muestra.
- Propiedad no mejorada: (Lote residencial sin una casa) $ 150 fijos.
- Propiedades mejoradas: cantidad fija + variables dependiendo de la casa,
    (pies de superficie con calefacción, refrigeración/ número de dormitorios
     baños, etc..).
- Condiciones de rebaja:
    1- Vive en la casa --> se reduce en un 10 % fijo.
    2- Si además es jubilidado hay otro descuento de 10 %.
- Los que reclaman salen ganando dado que es frecuente que se les
    haga una rebaja, el problema es que generan inconsistencias.
- Reevaluación cada 3 añitos (partamos por ahí xd)
- Llega el papi Bradford a poner orden y decide implementar un sistema de
    impuestos el cual considera las mismas condiciones anteriores, pero
    no especifica los coeficientes de las reglas, con esto planea postularse
    a ser el salvador de este injusto sistema
- Preocupaciones:
    1- Importante tratar de mantener las cosas lo más parecido a lo que esta
    actualmente (classic)
    2- El sistema debe ser neutral en cuanto a los ingresos (sumatoria debe
    ser parecida a lo que hay anteriormente)
- Problemas con los datos:
    1- Datos imprecisos: El RAD nunca verifica los pies cuadrados que hay
- Solución de papi Bradford, saco 80 muestas aleatorias, en las cuales
    la cual el tasador le puso voluntad a la cosa y se dio la pega de medir
    bien.
- Las TANGAS (? xdd) de Bradford:
    1- Quiere saber si las estimaciones en pies cuadrados en la base de datos
    difieren significativamente de los valores reales.
    2- Quiere usar los datos de muestra para estimar el impuesto único y la
    tasa impositiva por pies cuadrados (coefs de la regresión) para minimizar
    los cambios del sistema impositivo.

### 2) Comprensión de la BD:

> Descripción de la ubicación de la propiedad en 3 carácteristicas
- SUB: Subdivisión en la que se ubica la propiedad
- BLOCK: Bloque de fraccionamiento en el cual se encuentra la propiedad
- LOT:  Número de lote

> Tipo de casa
- IMP: 1, si se mejora 0 si no

> Excención de pago
- HSX: 1 si vive 0 si no
- RET: 1 si se jubiló 0 sino

> propiedades de la casa
- REC_SQFT: Metraje de registrado en la base de datos
- ACT_SQFT: Metraje reales medidos por el tasador (ponele voluntaaaad)

> output
- TAX: Impuesto actual del condado
