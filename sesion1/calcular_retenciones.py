"""
Calculadora de Retenciones por Transacción
Cruza transacciones.csv con catalogo_tasas.csv para obtener impuestos aplicables
"""

import pandas as pd
import os

# Obtener directorio del script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Cargar los archivos CSV
transacciones = pd.read_csv(os.path.join(script_dir, 'transacciones.csv'))
catalogo = pd.read_csv(os.path.join(script_dir, 'catalogo_tasas.csv'))

print("=" * 70)
print("📊 CÁLCULO DE RETENCIONES POR TRANSACCIÓN")
print("=" * 70)

# Cruzar transacciones con catálogo usando giro y región
resultado = transacciones.merge(
    catalogo,
    on=['giro', 'region_geografica'],
    how='left'
)

# Calcular montos de impuestos
resultado['monto_iva'] = resultado['monto'] * resultado['iva'] / 100
resultado['monto_isr_ret'] = resultado['monto'] * resultado['isr_retencion'] / 100
resultado['monto_iva_ret'] = resultado['monto'] * resultado['iva_retencion'] / 100
resultado['monto_imp_local'] = resultado['monto'] * resultado['impuesto_local'] / 100

# Total de retenciones
resultado['total_retenciones'] = resultado['monto_isr_ret'] + resultado['monto_iva_ret']
resultado['pct_retencion_total'] = resultado['isr_retencion'] + resultado['iva_retencion']

# Mostrar resultados
print("\n📋 DETALLE POR TRANSACCIÓN:\n")

for idx, row in resultado.iterrows():
    print(f"Transacción #{idx + 1}: {row['concepto']}")
    print(f"   Monto: ${row['monto']:,.2f} | Giro: {row['giro']} | Región: {row['region_geografica']}")
    print(f"   ├─ IVA ({row['iva']}%): ${row['monto_iva']:,.2f}")
    print(f"   ├─ Retención ISR ({row['isr_retencion']}%): ${row['monto_isr_ret']:,.2f}")
    print(f"   ├─ Retención IVA ({row['iva_retencion']}%): ${row['monto_iva_ret']:,.2f}")
    print(f"   ├─ Impuesto Local ({row['impuesto_local']}%): ${row['monto_imp_local']:,.2f}")
    print(f"   └─ 🔴 TOTAL RETENCIONES ({row['pct_retencion_total']}%): ${row['total_retenciones']:,.2f}")
    print()

# Resumen
print("=" * 70)
print("📈 RESUMEN GENERAL")
print("=" * 70)
print(f"Total transacciones: {len(resultado)}")
print(f"Monto total: ${resultado['monto'].sum():,.2f}")
print(f"Total IVA a cobrar: ${resultado['monto_iva'].sum():,.2f}")
print(f"Total retenciones ISR: ${resultado['monto_isr_ret'].sum():,.2f}")
print(f"Total retenciones IVA: ${resultado['monto_iva_ret'].sum():,.2f}")
print(f"Total impuestos locales: ${resultado['monto_imp_local'].sum():,.2f}")

# Guardar resultado completo a CSV
columnas_exportar = [
    'monto', 'concepto', 'giro', 'region_geografica',
    'iva', 'isr_retencion', 'iva_retencion', 'impuesto_local',
    'monto_iva', 'monto_isr_ret', 'monto_iva_ret', 'monto_imp_local',
    'total_retenciones', 'pct_retencion_total'
]
resultado[columnas_exportar].to_csv(os.path.join(script_dir, 'transacciones_con_impuestos.csv'), index=False)
print("\n✅ Archivo exportado: transacciones_con_impuestos.csv")
