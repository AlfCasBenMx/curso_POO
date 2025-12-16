"""Generador simple de Excel con pandas
Ejecutar desde la carpeta raíz del repositorio:

Windows (cmd.exe):

    python -m venv .venv
    .venv\\Scripts\\activate
    python -m pip install --upgrade pip
    python -m pip install pandas openpyxl
    python ejercicios\\generate_xlsx.py

Genera ejercicios/ejercicios.xlsx con una hoja por CSV.
"""
from pathlib import Path
import pandas as pd

BASE = Path(__file__).parent
FILES = {
    'transacciones': 'transacciones.csv',
    'clientes': 'clientes.csv',
    'ventas': 'ventas.csv',
    'tarifas': 'tarifas.csv',
}

def main():
    out = BASE / 'ejercicios.xlsx'
    with pd.ExcelWriter(out, engine='openpyxl') as writer:
        for sheet, fname in FILES.items():
            fpath = BASE / fname
            if not fpath.exists():
                print(f"Warning: {fpath} no existe, se omite")
                continue
            df = pd.read_csv(fpath)
            df.to_excel(writer, sheet_name=sheet[:31], index=False)
    print(f'Generado: {out}')

if __name__ == '__main__':
    main()
