# Paso 1: Hacer la Pregunta

## Pregunta
¿Qué características de una URL o sitio web predicen mejor si un sitio es phishing o legítimo?

## Beneficio
Un analista SOC o de seguridad se beneficia al identificar qué indicadores técnicos son más confiables para priorizar alertas de phishing y automatizar reglas de detección, reduciendo el tiempo de triage y los falsos positivos.

## Tipo de análisis
**Diagnóstico** — buscamos entender *por qué* ciertos sitios son clasificados como phishing (qué variables se correlacionan con esa etiqueta).

## Hipótesis inicial
Se espera que los sitios de phishing tiendan a presentar URLs más largas, mayor cantidad de caracteres especiales, ausencia de HTTPS, uso de direcciones IP en vez de dominios, y mayor cantidad de subdominios en comparación con sitios legítimos.

---

# Paso 2: Determinar los Datos Necesarios

## Elementos de datos identificados
- Longitud de la URL
- Presencia de caracteres especiales (@, -, %, =, ~, etc.)
- Uso de dirección IP en vez de nombre de dominio
- Uso de HTTPS
- Cantidad de subdominios (número de puntos en el dominio)
- Palabras sospechosas dentro de la URL
- Cantidad de dígitos en la URL
- Entropía de la URL (aleatoriedad de caracteres)

## Fuentes investigadas
- Kaggle — "Phishing URLs Dataset with Extracted Features" (victusadi)
- Kaggle — "Phishing Websites Dataset" (basado en UCI Machine Learning Repository)

---

# Preguntas de reflexión

**1. ¿Por qué es importante identificar la pregunta que debe responderse con el análisis antes de comenzar el proyecto?**

Porque la pregunta determina qué datos hay que recolectar, qué tipo de análisis aplicar y qué herramientas usar. Sin una pregunta clara, se corre el riesgo de recolectar datos irrelevantes o de perder tiempo analizando información que no responde a ninguna necesidad real. En seguridad, esto equivale a investigar sin saber qué se está buscando.

**2. Nombre algunas fuentes de datos abiertos para el análisis que encontró al buscar sus elementos de datos.**

Kaggle (datasets "Phishing URLs Dataset with Extracted Features" y "Phishing Websites Dataset"), ambos basados en investigación académica sobre detección de phishing (UCI Machine Learning Repository).
