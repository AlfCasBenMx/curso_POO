from __future__ import annotations

import csv
import random
from dataclasses import dataclass
from datetime import date, timedelta
from decimal import Decimal
from pathlib import Path


@dataclass(frozen=True)
class Venta:
    id_cliente: int
    fecha: date
    importe: str
    categoria: str


def daterange(start: date, end: date) -> list[date]:
    days = (end - start).days
    return [start + timedelta(days=i) for i in range(days + 1)]


def money(rng: random.Random, *, low: int, high: int) -> Decimal:
    # Importes con 2 decimales, pero variados
    cents = rng.randint(low * 100, high * 100)
    return (Decimal(cents) / Decimal(100)).quantize(Decimal("0.01"))


def write_csv(path: Path, rows: list[dict[str, str]], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(rows)


def build_clientes(*, n: int) -> list[dict[str, str]]:
    # Mantiene el formato de ejercicios/clientes.csv: id,nombre
    base = [
        "ACME SA",
        "Consultores del Norte",
        "Servicios Globales SA",
        "Industrial Delta",
        "Comercial Orion",
        "Logística Sierra",
        "Fintech Aurora",
        "Retail Andrómeda",
        "Energía Horizonte",
        "Agro Nova",
    ]

    rows: list[dict[str, str]] = []
    for i in range(1, n + 1):
        nombre = base[(i - 1) % len(base)]
        # Hacerlos únicos sin complicar
        if i > len(base):
            nombre = f"{nombre} {i}"  # ok para demo
        rows.append({"id": str(i), "nombre": nombre})
    return rows


def build_ventas(*, rng: random.Random, n: int, start: date, end: date, n_clientes: int) -> list[Venta]:
    fechas = daterange(start, end)
    categorias = ["Servicios", "Software", "Retenciones", "Honorarios", "Gastos"]
    weights = [0.35, 0.25, 0.10, 0.20, 0.10]

    ventas: list[Venta] = []
    for _ in range(n):
        id_cliente = rng.randint(1, n_clientes)
        fecha = rng.choice(fechas)
        categoria = rng.choices(categorias, weights=weights, k=1)[0]

        if categoria == "Retenciones":
            imp = money(rng, low=50, high=900)
        elif categoria == "Gastos":
            imp = money(rng, low=100, high=2500)
        else:
            imp = money(rng, low=200, high=12000)

        ventas.append(
            Venta(
                id_cliente=id_cliente,
                fecha=fecha,
                importe=f"{imp}",
                categoria=categoria,
            )
        )

    return ventas


def to_rows(ventas: list[Venta]) -> list[dict[str, str]]:
    return [
        {
            "id_cliente": str(v.id_cliente),
            "fecha": v.fecha.isoformat(),
            "importe": v.importe,
            "categoria": v.categoria,
        }
        for v in ventas
    ]


def build_ventas_sucio(*, rng: random.Random, base: list[Venta], take: int) -> list[dict[str, str]]:
    # Copia un subconjunto y mete errores típicos (NaN, texto, separadores)
    sample = base[:take]
    rows = to_rows(sample)

    if len(rows) >= 5:
        rows[1]["importe"] = ""  # vacío
        rows[2]["importe"] = "NaN"  # token
        rows[3]["importe"] = "1,500.00"  # miles
        rows[4]["importe"] = "abc"  # inválido

    # También mete una categoría “nueva” para probar reglas
    if len(rows) >= 8:
        rows[7]["categoria"] = "Servicios Especiales"

    return rows


def main() -> None:
    base_dir = Path(__file__).resolve().parent
    out_dir = base_dir

    rng = random.Random(42)

    clientes = build_clientes(n=50)
    write_csv(out_dir / "clientes_large.csv", clientes, ["id", "nombre"])

    ventas = build_ventas(rng=rng, n=200, start=date(2025, 1, 1), end=date(2025, 3, 31), n_clientes=50)
    write_csv(out_dir / "ventas_large.csv", to_rows(ventas), ["id_cliente", "fecha", "importe", "categoria"])

    ventas_sucio = build_ventas_sucio(rng=rng, base=ventas, take=30)
    write_csv(out_dir / "ventas_sucio.csv", ventas_sucio, ["id_cliente", "fecha", "importe", "categoria"])

    print("OK: generados clientes_large.csv, ventas_large.csv, ventas_sucio.csv")


if __name__ == "__main__":
    main()
