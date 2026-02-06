from __future__ import annotations

import argparse
import csv
from dataclasses import dataclass
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP
from pathlib import Path


NA_TOKENS = {"", "nan", "na", "n/a", "null", "none"}


def is_missing(value: object) -> bool:
    if value is None:
        return True
    return str(value).strip().lower() in NA_TOKENS


def parse_decimal(value: object, *, field_name: str) -> Decimal:
    if is_missing(value):
        raise ValueError(f"{field_name} vacío")

    text = str(value).strip()

    # Normaliza separadores comunes: 1,500.00 o 1500,00
    if "," in text and "." in text:
        text = text.replace(",", "")
    else:
        text = text.replace(",", ".")

    try:
        return Decimal(text)
    except InvalidOperation as exc:
        raise ValueError(f"{field_name} inválido: {value!r}") from exc


@dataclass(frozen=True)
class ReglaImpuesto:
    categoria: str  # '*' significa "aplica a cualquier categoría"
    min_incl: Decimal
    max_incl: Decimal | None
    tasa: Decimal

    def aplica(self, *, categoria: str, importe: Decimal) -> bool:
        cat_ok = (self.categoria == "*") or (self.categoria.strip().lower() == categoria.strip().lower())
        if not cat_ok:
            return False
        if importe < self.min_incl:
            return False
        if self.max_incl is None:
            return True
        return importe <= self.max_incl


def load_reglas(path: Path) -> list[ReglaImpuesto]:
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        if reader.fieldnames is None:
            raise SystemExit("El CSV de reglas no tiene encabezados.")

        required = {"categoria", "min_incl", "max_incl", "tasa"}
        missing = required - set(reader.fieldnames)
        if missing:
            raise SystemExit(f"Faltan columnas en reglas_impuesto.csv: {sorted(missing)}")

        reglas: list[ReglaImpuesto] = []
        for row_number, row in enumerate(reader, start=2):
            categoria = (row.get("categoria") or "*").strip() or "*"
            try:
                min_incl = parse_decimal(row.get("min_incl"), field_name="min_incl")
                max_raw = row.get("max_incl")
                max_incl = None if is_missing(max_raw) else parse_decimal(max_raw, field_name="max_incl")
                tasa = parse_decimal(row.get("tasa"), field_name="tasa")
            except ValueError as e:
                raise SystemExit(f"Error en reglas fila {row_number}: {e}")

            reglas.append(ReglaImpuesto(categoria=categoria, min_incl=min_incl, max_incl=max_incl, tasa=tasa))

        if not reglas:
            raise SystemExit("No hay reglas en reglas_impuesto.csv")

        return reglas


def elegir_regla(reglas: list[ReglaImpuesto], *, categoria: str, importe: Decimal) -> ReglaImpuesto | None:
    # Prioridad: reglas específicas de categoría primero, luego '*'
    especificas = [r for r in reglas if r.categoria != "*"]
    generales = [r for r in reglas if r.categoria == "*"]

    for regla in especificas + generales:
        if regla.aplica(categoria=categoria, importe=importe):
            return regla
    return None


def main() -> None:
    base_dir = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser(
        description="Aplica reglas de impuesto definidas en un CSV y genera un CSV de salida + un CSV de excepciones."
    )
    parser.add_argument(
        "--input",
        default=str(base_dir / "ejercicios" / "ventas.csv"),
        help="Ruta del CSV de ventas (default: ejercicios/ventas.csv)",
    )
    parser.add_argument(
        "--rules",
        default=str(base_dir / "ejercicios" / "reglas_impuesto.csv"),
        help="Ruta del CSV de reglas (default: ejercicios/reglas_impuesto.csv)",
    )
    parser.add_argument(
        "--output",
        default=str(base_dir / "ejercicios" / "ventas_con_impuesto_motor.csv"),
        help="Ruta del CSV de salida (default: ejercicios/ventas_con_impuesto_motor.csv)",
    )
    parser.add_argument(
        "--exceptions",
        default=str(base_dir / "ejercicios" / "ventas_excepciones_motor.csv"),
        help="Ruta del CSV de excepciones (default: ejercicios/ventas_excepciones_motor.csv)",
    )
    args = parser.parse_args()

    input_path = Path(args.input)
    reglas_path = Path(args.rules)
    output_path = Path(args.output)
    exceptions_path = Path(args.exceptions)

    if not input_path.exists():
        raise SystemExit(f"No encontré el archivo: {input_path}")
    if not reglas_path.exists():
        raise SystemExit(f"No encontré el archivo de reglas: {reglas_path}")

    reglas = load_reglas(reglas_path)

    total_rows = 0
    missing_importe = 0
    invalid_importe = 0
    sin_regla = 0
    total_importe = Decimal("0")
    total_impuesto = Decimal("0")

    with input_path.open("r", encoding="utf-8-sig", newline="") as f_in:
        reader = csv.DictReader(f_in)
        if reader.fieldnames is None:
            raise SystemExit("El CSV de ventas no tiene encabezados.")

        required = {"fecha", "importe", "categoria"}
        missing = required - set(reader.fieldnames)
        if missing:
            raise SystemExit(f"Faltan columnas en ventas.csv: {sorted(missing)}")

        fieldnames = list(reader.fieldnames)
        for extra in ("impuesto_tasa", "impuesto"):
            if extra not in fieldnames:
                fieldnames.append(extra)

        output_path.parent.mkdir(parents=True, exist_ok=True)
        exceptions_path.parent.mkdir(parents=True, exist_ok=True)

        exceptions_fieldnames = [
            "motivo",
            "row_number",
            *fieldnames,
        ]

        with output_path.open("w", encoding="utf-8", newline="") as f_out, exceptions_path.open(
            "w", encoding="utf-8", newline=""
        ) as f_exc:
            writer = csv.DictWriter(f_out, fieldnames=fieldnames)
            writer_exc = csv.DictWriter(f_exc, fieldnames=exceptions_fieldnames)
            writer.writeheader()
            writer_exc.writeheader()

            for row_number, row in enumerate(reader, start=2):
                total_rows += 1

                categoria = str(row.get("categoria") or "").strip()
                if is_missing(row.get("importe")):
                    missing_importe += 1
                    row["impuesto_tasa"] = ""
                    row["impuesto"] = ""
                    writer.writerow(row)

                    exc_row = {k: row.get(k, "") for k in fieldnames}
                    exc_row["motivo"] = "importe_vacio"
                    exc_row["row_number"] = str(row_number)
                    writer_exc.writerow(exc_row)
                    continue

                try:
                    importe = parse_decimal(row.get("importe"), field_name="importe")
                except ValueError as e:
                    invalid_importe += 1
                    row["impuesto_tasa"] = ""
                    row["impuesto"] = ""
                    writer.writerow(row)
                    exc_row = {k: row.get(k, "") for k in fieldnames}
                    exc_row["motivo"] = f"importe_invalido: {e}"
                    exc_row["row_number"] = str(row_number)
                    writer_exc.writerow(exc_row)
                    continue

                regla = elegir_regla(reglas, categoria=categoria, importe=importe)
                if regla is None:
                    sin_regla += 1
                    row["impuesto_tasa"] = ""
                    row["impuesto"] = ""
                    writer.writerow(row)

                    exc_row = {k: row.get(k, "") for k in fieldnames}
                    exc_row["motivo"] = "sin_regla"
                    exc_row["row_number"] = str(row_number)
                    writer_exc.writerow(exc_row)
                    continue

                impuesto = (importe * regla.tasa).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

                total_importe += importe
                total_impuesto += impuesto

                row["impuesto_tasa"] = str(regla.tasa)
                row["impuesto"] = str(impuesto)
                writer.writerow(row)

    pct_missing_importe = (
        (Decimal(missing_importe) * Decimal("100") / Decimal(total_rows)).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        if total_rows > 0
        else Decimal("0")
    )
    pct_invalid_importe = (
        (Decimal(invalid_importe) * Decimal("100") / Decimal(total_rows)).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        if total_rows > 0
        else Decimal("0")
    )

    print(f"OK: generado {output_path}")
    print(f"OK: generado {exceptions_path}")
    print(f"Filas: {total_rows}")
    print(f"Suma importe: {total_importe.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)}")
    print(f"Suma impuesto: {total_impuesto.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)}")
    print(f"Importe vacío (NaN): {missing_importe} ({pct_missing_importe}%)")
    print(f"Importe inválido: {invalid_importe} ({pct_invalid_importe}%)")
    print(f"Filas sin regla aplicable: {sin_regla}")


if __name__ == "__main__":
    main()
