from __future__ import annotations

import csv
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP
from pathlib import Path


NA_TOKENS = {"", "nan", "na", "n/a", "null", "none"}


def is_missing(value: object) -> bool:
    if value is None:
        return True
    text = str(value).strip().lower()
    return text in NA_TOKENS


def parse_decimal(value: str) -> Decimal:
    """Convierte texto a Decimal.

    Acepta formatos comunes como: 1500.00 o 1,500.00 o 1500,00.
    """
    if value is None:
        raise ValueError("importe vacío")

    text = str(value).strip()
    if text == "":
        raise ValueError("importe vacío")

    # Quitar separador de miles y normalizar separador decimal
    # Ejemplos:
    #  "1,500.00" -> "1500.00"
    #  "1500,00"  -> "1500.00"
    if "," in text and "." in text:
        text = text.replace(",", "")
    else:
        text = text.replace(",", ".")

    try:
        return Decimal(text)
    except InvalidOperation as exc:
        raise ValueError(f"importe inválido: {value!r}") from exc


def impuesto_tasa(importe: Decimal) -> Decimal:
    """Regla escalonada: <=1000 => 5%, <=5000 => 8%, >5000 => 12%."""
    if importe <= Decimal("1000"):
        return Decimal("0.05")
    if importe <= Decimal("5000"):
        return Decimal("0.08")
    return Decimal("0.12")


def main() -> None:
    base_dir = Path(__file__).resolve().parent
    input_path = base_dir / "ejercicios" / "ventas.csv"
    output_path = base_dir / "ejercicios" / "ventas_con_impuesto.csv"

    if not input_path.exists():
        raise SystemExit(f"No encontré el archivo: {input_path}")

    total_importe = Decimal("0")
    total_rows = 0
    missing_counts: dict[str, int] = {}

    with input_path.open("r", encoding="utf-8-sig", newline="") as f_in:
        reader = csv.DictReader(f_in)
        if reader.fieldnames is None:
            raise SystemExit("El CSV no tiene encabezados.")

        required = {"id_cliente", "fecha", "importe", "categoria"}
        missing = required - set(reader.fieldnames)
        if missing:
            raise SystemExit(f"Faltan columnas en ventas.csv: {sorted(missing)}")

        for col in required:
            missing_counts[col] = 0

        fieldnames = list(reader.fieldnames) + ["impuesto_tasa", "impuesto"]

        with output_path.open("w", encoding="utf-8", newline="") as f_out:
            writer = csv.DictWriter(f_out, fieldnames=fieldnames)
            writer.writeheader()

            for row_number, row in enumerate(reader, start=2):
                total_rows += 1

                for col in required:
                    if is_missing(row.get(col)):
                        missing_counts[col] += 1

                if is_missing(row.get("importe")):
                    row["impuesto_tasa"] = ""
                    row["impuesto"] = ""
                    writer.writerow(row)
                    continue

                try:
                    importe = parse_decimal(row["importe"])
                except ValueError as e:
                    raise SystemExit(f"Error en fila {row_number} (columna 'importe'): {e}")

                total_importe += importe

                tasa = impuesto_tasa(importe)
                impuesto = (importe * tasa).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

                row["impuesto_tasa"] = str(tasa)
                row["impuesto"] = str(impuesto)
                writer.writerow(row)

    total_importe_2d = total_importe.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    print(f"OK: generado {output_path}")
    print(f"Suma de importes: {total_importe_2d}")
    if total_rows > 0:
        for col in ("importe", "fecha", "categoria", "id_cliente"):
            if col in missing_counts:
                count = missing_counts[col]
                pct = (Decimal(count) * Decimal("100") / Decimal(total_rows)).quantize(
                    Decimal("0.01"), rounding=ROUND_HALF_UP
                )
                print(f"NaNs en '{col}': {count} ({pct}%)")


if __name__ == "__main__":
    main()
