import csv
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path


# Rutas (cambia INPUT_CSV si quieres usar otro dataset)
BASE_DIR = Path(__file__).resolve().parent
INPUT_CSV = BASE_DIR / "ventas_large.csv"  # o ventas.csv / ventas_sucio.csv
RULES_CSV = BASE_DIR / "reglas_impuesto.csv"
OUTPUT_CSV = BASE_DIR / "ventas_con_impuesto.csv"
EXCEPTIONS_CSV = BASE_DIR / "ventas_excepciones.csv"


def is_missing(x) -> bool:
    if x is None:
        return True
    t = str(x).strip().lower()
    return t in {"", "nan", "na", "n/a", "null", "none"}


def to_decimal(x) -> Decimal:
    # Acepta 1500.00, 1500,00 o 1,500.00
    s = str(x).strip()
    if "," in s and "." in s:
        s = s.replace(",", "")
    else:
        s = s.replace(",", ".")
    return Decimal(s)


def main():
    if not INPUT_CSV.exists():
        raise SystemExit(f"No encontré: {INPUT_CSV}")
    if not RULES_CSV.exists():
        raise SystemExit(f"No encontré: {RULES_CSV}")

    # 1) Cargar reglas
    reglas = []
    with RULES_CSV.open("r", encoding="utf-8-sig", newline="") as f:
        rr = csv.DictReader(f)
        for r in rr:
            categoria = (r.get("categoria") or "*").strip() or "*"
            min_incl = to_decimal(r["min_incl"])
            max_raw = r.get("max_incl")
            max_incl = None if is_missing(max_raw) else to_decimal(max_raw)
            tasa = to_decimal(r["tasa"])
            reglas.append((categoria, min_incl, max_incl, tasa))

    # 2) Procesar ventas
    total_rows = 0
    total_importe = Decimal("0")
    total_impuesto = Decimal("0")

    with INPUT_CSV.open("r", encoding="utf-8-sig", newline="") as f_in, \
         OUTPUT_CSV.open("w", encoding="utf-8", newline="") as f_out, \
         EXCEPTIONS_CSV.open("w", encoding="utf-8", newline="") as f_exc:

        ventas = csv.DictReader(f_in)
        fieldnames = list(ventas.fieldnames or []) + ["impuesto_tasa", "impuesto"]

        out = csv.DictWriter(f_out, fieldnames=fieldnames)
        exc = csv.DictWriter(f_exc, fieldnames=["motivo", "row_number", *fieldnames])
        out.writeheader()
        exc.writeheader()

        for row_number, row in enumerate(ventas, start=2):
            total_rows += 1

            categoria = str(row.get("categoria") or "").strip()
            imp_raw = row.get("importe")

            # Manejo simple de vacíos / inválidos
            if is_missing(imp_raw):
                row["impuesto_tasa"] = ""
                row["impuesto"] = ""
                out.writerow(row)
                exc.writerow({"motivo": "importe_vacio", "row_number": row_number, **row})
                continue

            try:
                importe = to_decimal(imp_raw)
            except Exception:
                row["impuesto_tasa"] = ""
                row["impuesto"] = ""
                out.writerow(row)
                exc.writerow({"motivo": "importe_invalido", "row_number": row_number, **row})
                continue

            # 3) Encontrar la primera regla aplicable (prioriza categoría específica, luego '*')
            regla_encontrada = None
            for cat, min_incl, max_incl, tasa in reglas:
                cat_ok = (cat == "*") or (cat.lower() == categoria.lower())
                if not cat_ok:
                    continue
                if importe < min_incl:
                    continue
                if max_incl is not None and importe > max_incl:
                    continue
                regla_encontrada = (cat, tasa)
                break

            if regla_encontrada is None:
                row["impuesto_tasa"] = ""
                row["impuesto"] = ""
                out.writerow(row)
                exc.writerow({"motivo": "sin_regla", "row_number": row_number, **row})
                continue

            _, tasa = regla_encontrada
            impuesto = (importe * tasa).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

            row["impuesto_tasa"] = str(tasa)
            row["impuesto"] = str(impuesto)
            out.writerow(row)

            total_importe += importe
            total_impuesto += impuesto

    print(f"OK: {OUTPUT_CSV}")
    print(f"OK: {EXCEPTIONS_CSV}")
    print(f"Filas: {total_rows}")
    print(f"Suma importe: {total_importe.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)}")
    print(f"Suma impuesto: {total_impuesto.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)}")


if __name__ == "__main__":
    main()
