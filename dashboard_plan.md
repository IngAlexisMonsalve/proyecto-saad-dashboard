# Plan de Desarrollo del Dashboard de Análisis de Rendimiento Estudiantil

## 1. Objetivo

Crear una aplicación web interactiva que funcione como un dashboard profesional para visualizar, analizar y presentar los hallazgos del proyecto de análisis de datos de rendimiento estudiantil (SAAD ESENCIAL).

## 2. Tecnología

*   **Framework Principal:** Streamlit
*   **Lenguaje:** Python
*   **Librerías de Datos:** Pandas, Matplotlib, Seaborn

Se eligió Streamlit por su facilidad de uso, su rápida integración con librerías de Python para ciencia de datos y su capacidad para crear dashboards interactivos y estéticamente agradables con poco código.

## 3. Estructura del Dashboard

La aplicación se organizará en una barra lateral de navegación que permitirá al usuario moverse entre diferentes secciones lógicas:

*   **Página Principal / Introducción:**
    *   Título del proyecto.
    *   Breve descripción del objetivo del dashboard.
    *   Resumen del conjunto de datos utilizado ("Student Performance & Behavior Dataset").

*   **Análisis Exploratorio de Datos (EDA):**
    *   Opción para mostrar/ocultar los primeros registros del dataset.
    *   Presentación de las estadísticas descriptivas (media, mediana, desviación estándar, etc.) de las puntuaciones.
    *   Información general del dataset (número de filas, columnas, tipos de datos).

*   **Análisis de Puntuaciones Académicas:**
    *   Visualización de las distribuciones de las puntuaciones de matemáticas, lectura y escritura mediante histogramas.
    *   Interpretación de las distribuciones.
    *   Visualización de la matriz de correlación entre las tres puntuaciones con un mapa de calor (`heatmap`).
    *   Análisis de la fuerte correlación positiva encontrada.

*   **Análisis por Características:**
    *   Sección con filtros interactivos (widgets de Streamlit) para que el usuario pueda seleccionar:
        *   La puntuación a analizar (matemáticas, lectura o escritura).
        *   La característica categórica a explorar (género, etnia, nivel educativo de los padres, etc.).
    *   Visualización dinámica de un gráfico de caja (`boxplot`) que muestre la relación entre la puntuación y la característica seleccionada.
    *   Interpretación de los hallazgos clave para cada característica.

*   **Conclusiones Clave:**
    *   Resumen de los principales insights obtenidos del análisis.
    *   Identificación de las características más influyentes en el rendimiento académico.
    *   Posibles siguientes pasos o áreas para un análisis más profundo (como la creación de un modelo predictivo).

## 4. Diseño y Experiencia de Usuario (UX)

*   **Diseño:** Se utilizará un tema limpio y profesional, aprovechando la disposición en columnas de Streamlit para organizar el contenido de forma clara.
*   **Interactividad:** El uso de filtros, selectores y la posibilidad de mostrar/ocultar información hará que la exploración de los datos sea intuitiva y atractiva para el usuario.

## 5. Pasos de Ejecución

1.  Crear el archivo `dashboard.py` para la aplicación Streamlit.
2.  Instalar Streamlit en el entorno virtual `.venv`.
3.  Implementar cada una de las secciones del dashboard de acuerdo a la estructura definida.
4.  Cargar los datos desde `ProyectoSAAD_NotasAcademicas/Fase_IV_AnalisisDatos_Streamlit/student_performance_data.csv`.
5.  Reutilizar los gráficos generados previamente y añadir la lógica para los componentes interactivos.
6.  Añadir texto interpretativo y explicaciones en cada sección.
7.  Verificar la funcionalidad completa del dashboard.
8.  Proporcionar las instrucciones finales para que el usuario pueda ejecutar la aplicación.
