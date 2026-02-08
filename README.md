# Proyecto SAAD ESENCIAL: Dashboard de Análisis de Rendimiento Estudiantil

## Descripción General del Proyecto

**SAAD ESENCIAL** (Sistema de Alerta y Análisis de Datos) es un proyecto enfocado en modelar y analizar sistemas de información. En esta iteración, el escenario elegido es el **Análisis de Notas Académicas** de estudiantes.

Este repositorio contiene el código y la documentación de la Fase IV del proyecto, que comprende el Análisis Exploratorio de Datos (EDA) y la implementación de un dashboard interactivo utilizando Streamlit. El objetivo principal es visualizar y analizar el rendimiento estudiantil, identificando patrones y factores influyentes en los resultados académicos.

## Características Principales del Dashboard

El dashboard interactivo permite:

*   **Introducción:** Visión general del proyecto y su propósito.
*   **Análisis Exploratorio de Datos (EDA):** Muestra estadísticas descriptivas, información del dataset y los primeros registros de datos.
*   **Análisis de Puntuaciones Académicas:** Visualiza la distribución de las puntuaciones de matemáticas, lectura y escritura, así como la correlación entre ellas mediante un mapa de calor.
*   **Análisis por Características:** Permite explorar interactivamente la relación entre las puntuaciones académicas y diversas características demográficas o de hábitos (género, etnia, nivel educativo de los padres, tipo de almuerzo, curso de preparación, etc.) a través de gráficos de caja.
*   **Conclusiones Clave:** Resume los principales hallazgos e insights obtenidos del análisis de datos.
*   **Próximos Pasos Sugeridos:** Propone la continuación del proyecto hacia la modelización predictiva y la implementación de un sistema de alerta temprana.

## Estructura del Proyecto

```
.
├── .venv/                         # Entorno virtual de Python (no subir a GitHub)
├── dashboard_plan.md              # Plan de desarrollo del dashboard
├── dashboard.py                   # Código fuente de la aplicación Streamlit
├── eda.py                         # Script de Análisis Exploratorio de Datos (EDA)
├── eda_plots/                     # Carpeta con gráficos generados por eda.py (para usar en dashboard.py)
│   ├── correlation_matrix.png
│   ├── distribution_math_score.png
│   ├── ... (otros gráficos de distribución y box plots)
├── requirements.txt               # Lista de dependencias de Python
└── ProyectoSAAD_NotasAcademicas/
    ├── bitacora.md                # Bitácora de seguimiento del proyecto
    ├── README.md                  # (Si existe) README específico de esa sección
    ├── Fase_I_Requerimientos/
    │   └── DFD_y_Diccionario_de_Datos.md
    ├── Fase_II_DisenoLogico/
    │   └── Diseno_Logico_Fase_II.md
    ├── Fase_III_ModeladoPOO/
    │   └── Diagrama_de_Clases_UML.md
    └── Fase_IV_AnalisisDatos_Streamlit/
        └── student_performance_data.csv # Dataset utilizado
```

## Cómo Ejecutar el Dashboard Localmente

Para ejecutar la aplicación Streamlit en tu máquina local, sigue estos pasos:

1.  **Clonar el Repositorio (si no lo has hecho ya):**
    ```bash
    git clone [URL_DEL_TU_REPOSITORIO]
    cd proyecto-saad-dashboard
    ```

2.  **Crear y Activar el Entorno Virtual:**
    Si el `.venv` no está presente (normalmente se excluye de GitHub), debes crearlo:
    ```bash
    python -m venv .venv
    ```
    Activa el entorno virtual:
    *   **Windows (PowerShell):**
        ```bash
        .venv\Scripts\Activate
        ```
    *   **Windows (CMD):**
        ```bash
        .venv\Scripts\activate.bat
        ```
    *   **macOS/Linux:**
        ```bash
        source .venv/bin/activate
        ```

3.  **Instalar Dependencias:**
    Con el entorno virtual activado, instala todas las librerías necesarias:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Ejecutar la Aplicación Streamlit:**
    Asegúrate de estar en la raíz del proyecto y ejecuta:
    ```bash
    streamlit run dashboard.py
    ```
    Esto abrirá automáticamente el dashboard en tu navegador web.

## Despliegue en Streamlit Community Cloud

Para compartir tu dashboard con otras personas, la forma más sencilla es desplegarlo en [Streamlit Community Cloud](https://share.streamlit.io/).

1.  Asegúrate de que todos los archivos relevantes (`dashboard.py`, `requirements.txt`, `eda_plots/`, `ProyectoSAAD_NotasAcademicas/`) estén subidos a tu repositorio **público** de GitHub.
2.  Ve a [share.streamlit.io](https://share.streamlit.io/) e inicia sesión con tu cuenta de GitHub.
3.  Haz clic en **"New app"** y selecciona tu repositorio.
4.  Asegúrate de que la "Main file path" sea `dashboard.py`.
5.  Haz clic en **"Deploy!"**.
    Streamlit Community Cloud instalará automáticamente las dependencias listadas en `requirements.txt` y te proporcionará una URL pública para tu aplicación.

## Contacto

Para cualquier pregunta o sugerencia sobre este proyecto, por favor contacta a [Tu Nombre/Contacto].

---
_Este README fue generado automáticamente como parte del desarrollo del proyecto._
