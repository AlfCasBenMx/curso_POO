Ejercicios – Soluciones rápidas

1) hola.py

Salida: Hola desde Python - Sesión 3

2) suma.py

Salida: 525
Excel: =SUM(A1:A3)

3) filtrar.py

Salida: 2
Excel: =COUNTIFS(A:A, ">=1000")

4) iva.py

Salida: [116.0, 232.0, 348.0]
Excel: en B1 =A1*1.16 y arrastrar

5) Leer CSV

Salida: suma de la columna importe del CSV (depende del archivo de ejemplo)
Excel: importar el CSV y usar =SUM(C:C)

6) Agrupar y sumar por categoría

Salida: dict con sumas por categoría (por ejemplo {'Servicios':1950.0,'Software':3200.5,'Retenciones':200.0})
Excel: Tabla dinámica o =SUMIFS(importe_range,categoria_range,"Servicios")

7) Lookup

Salida: nombre del cliente asociado al id (usar map o dict en Python)
Excel: =XLOOKUP(id, Clientes!A:A, Clientes!B:B)

8) Regla escalonada

Salida: 120.0 para monto=1200
Excel: =IF(A1<=1000,A1*0.05,A1*0.1)

9) Mini reto

Salida: descripción de columnas y fórmulas: XLOOKUP para tasa, IF para condiciones, SUMIFS para totales.

10) IA para fórmula

Salida: fórmula ejemplo: =SUMIFS(C:C,B:B,"Servicios",A:A,">=01/01/2025",A:A,"<=31/12/2025")
