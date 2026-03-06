# POC Thinking con Microsoft 365 Copilot

> Programa de 3 sesiones diseñado para **Project Managers** y **profesionales financieros**.

## 🎯 Objetivo

Capacitar a PMs y financieros para crear **Pruebas de Concepto (POCs)** usando **Microsoft 365 Copilot** y **GitHub Copilot** como copilotos integrales — desde análisis sin código hasta automatización con Python.

## 🛠️ Herramientas

| Herramienta | Sesión | Uso principal |
|-------------|--------|---------------|
| Excel + Copilot | 1 | Análisis de datos, fórmulas con IA, tablas dinámicas |
| Power BI + Copilot | 1 | Dashboards interactivos |
| Copilot Chat | 2 | Generación de HTMLs interactivos (reportes, dashboards, presentaciones) |
| VS Code + GitHub Copilot | 3 | Automatización Python: consolidación multi-fuente, formato global |
| pandas + openpyxl | 3 | Lectura, transformación y escritura de Excel/CSV |

## 📁 Estructura del proyecto

```
POC_THINKING_SCOTIA/
├── intro.html                          # Brochure principal del programa
├── sesion1.html                        # Sesión 1 — Excel + Power BI + Copilot 365
├── sesion2.html                        # Sesión 2 — HTMLs interactivos con Copilot Chat
├── sesion3.html                        # Sesión 3 — Python multi-fuente con GitHub Copilot
├── prompts_cheatsheet.html             # Cheatsheet de prompts (Sesión 2)
├── README.md                           # Este archivo
├── ejercicios_sesion_1/
│   ├── ejercicios_instrucciones.md     # Instrucciones de ejercicios
│   ├── prompts_cheatsheet.md           # Guía rápida de prompts
│   ├── guion_instructor_sesion1.md     # Guión del instructor
│   ├── generate_datasets_sesion1.py    # Generador de datasets
│   └── *.xlsx                          # Datasets de ejemplo
├── ejercicios_sesion_2/
│   ├── ejemplo_dashboard.html          # Ejemplo de dashboard HTML
│   ├── ejemplo_presentacion.html       # Ejemplo de presentación HTML
│   ├── ejemplo_reporte.html            # Ejemplo de reporte HTML
│   └── guia_iconos_svg.html            # Guía de íconos SVG
└── ejercicios_sesion_3/
    ├── ejercicios_instrucciones.md     # Instrucciones (6 ejercicios)
    ├── prompts_cheatsheet.md           # Prompts para GitHub Copilot
    ├── guion_instructor_sesion3.md     # Guión del instructor
    ├── generate_datasets_sesion3.py    # Generador de 12 datasets
    ├── consolidar_solucion.py          # Script solución completo
    ├── datos_entrada/                  # 10 xlsx + 2 csv de ejemplo
    └── datos_salida/                   # Outputs generados por la solución
```

## 📅 Programa de 3 Sesiones

| Sesión | Tema | Herramientas | Enfoque |
|--------|------|-------------|---------|
| **1** | Datos y Análisis | Excel + Power BI + Copilot 365 | Análisis sin código, dashboards |
| **2** | Documentación Interactiva | Copilot Chat | HTMLs: reportes, dashboards, presentaciones |
| **3** | Automatización Python | VS Code + GitHub Copilot + pandas | Consolidar 12 fuentes → 3 Excels → Formato Global |

## ✅ Requisitos previos

### Sesiones 1 y 2
- Licencia de Microsoft 365 con Copilot habilitado
- Acceso a Excel, Word, PowerPoint y Teams
- Laptop con conexión a internet
- **No se requiere experiencia en programación**

### Sesión 3
- Todo lo anterior, más:
- VS Code con extensión GitHub Copilot
- Python 3.9+ con `pandas`, `openpyxl`, `xlsxwriter`
- Familiaridad básica con conceptos de datos (columnas, filas, filtros)

## 📌 Enfoque progresivo

| Sesión | Sin código | Código asistido |
|--------|:----------:|:---------------:|
| 1 | ✅ | — |
| 2 | ✅ | — |
| 3 | — | ✅ (Python + GitHub Copilot) |

Las sesiones 1 y 2 son **100% sin código** usando prompts en Microsoft 365. La sesión 3 introduce **Python asistido por GitHub Copilot** para automatizar procesos de consolidación financiera que manualmente tomarían horas.
