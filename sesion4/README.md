# Sesión 4 — Motor de reglas configurable (POC)

## Objetivo (de la sesión)
Estructurar una POC con objetivo/entradas/salidas/validaciones claras y ejecutar un **motor de reglas** donde las tasas/umbrales se cambian en un CSV (sin tocar el código).

## Qué hay en esta carpeta
- `sesion4.html`: guía completa para facilitar la sesión
- `motor_reglas_simple.py`: script **mega simple** (para explicar en vivo)
- `motor_reglas.py`: versión más robusta (opcional)
- `reglas_impuesto.csv`: reglas editables
- `ventas.csv`: dataset pequeño
- `ventas_large.csv`: dataset grande
- `ventas_sucio.csv`: dataset con vacíos/NaN/importe inválido para practicar validación

## Cómo correr
Desde la raíz del repo o desde esta carpeta:

- Script simple:
  - `python sesion4/motor_reglas_simple.py`

- (Opcional) Script robusto:
  - `python sesion4/motor_reglas.py --input sesion4/ventas_sucio.csv --rules sesion4/reglas_impuesto.csv`

## Outputs
Se generan en esta misma carpeta:
- `ventas_con_impuesto.csv`
- `ventas_excepciones.csv`
