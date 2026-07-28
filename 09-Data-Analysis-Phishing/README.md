# Análisis de Datos: Detección de Phishing por Características de URL

## Resumen
Proyecto de análisis de datos enfocado en identificar qué características técnicas de una URL o sitio web son más útiles para predecir si se trata de un sitio de phishing o de un sitio legítimo.

## Contexto
Proyecto desarrollado como parte del curso **"Fundamentos de Análisis de Datos"**, cursado a través de la beca **MICITT / PROCOMER (Talent Up)** vía **Cisco Networking Academy**.

## Pregunta de investigación
¿Qué características de una URL o sitio web (longitud de la URL, uso de dirección IP en vez de dominio, presencia de HTTPS, edad del dominio, símbolos especiales, etc.) predicen mejor si un sitio es phishing o legítimo?

## Motivación / Beneficio
Un analista SOC o de seguridad se beneficia al identificar qué indicadores técnicos son más confiables para priorizar alertas de phishing y automatizar reglas de detección (por ejemplo, en un SIEM o filtro de correo), reduciendo el tiempo de triage y los falsos positivos.

## Metodología
- **Tipo de análisis:** Diagnóstico (con componente descriptivo)
- **Fuente de datos:** _pendiente — ver `data/README.md`_
- **Herramientas:** _se actualizará conforme avance el curso (Excel / SQL / Tableau)_

## Hallazgos principales
_Se completará al finalizar el análisis (Módulos 4-8 del curso)._

## Habilidades demostradas
- Definición de preguntas analíticas
- Recolección e investigación de datos
- Limpieza y preparación de datos
- Análisis estadístico descriptivo
- Consultas SQL
- Visualización de datos (Tableau)
- Relevancia directa para ciberseguridad: identificación de indicadores de phishing

## Estructura del proyecto
- `01-question-and-hypothesis.md` — Pregunta, beneficio, tipo de análisis e hipótesis inicial
- `02-data-sources.md` — Fuentes de datos identificadas
- `03-cleaning-and-prep.md` — Limpieza y preparación de datos
- `04-analysis.md` — Análisis estadístico y hallazgos
- `05-visualization/` — Dashboards y gráficos (Tableau)
- `06-sql-queries.sql` — Consultas SQL utilizadas
- `data/` — Referencia al dataset utilizado
