import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
from PIL import Image

# --- Configuración de la Página ---
st.set_page_config(
    page_title="SAAD - Dashboard de Rendimiento Estudiantil",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Funciones de Carga y Análisis ---

@st.cache_data
def load_data(path):
    """Carga el dataset desde la ruta especificada."""
    try:
        df = pd.read_csv(path, delimiter=';')
        # Limpiar nombres de columnas
        df.columns = [col.strip().replace(' ', '_') for col in df.columns]
        return df
    except FileNotFoundError:
        st.error(f"Error: El archivo no se encontró en la ruta: '{path}'. Asegúrate de que el archivo existe.")
        return None

def get_sanitized_filename(name):
    """Limpia un string para que sea un nombre de archivo válido."""
    return name.lower().replace(" ", "_").replace("/", "_")

# --- Carga de Datos ---
DATASET_PATH = 'ProyectoSAAD_NotasAcademicas/Fase_IV_AnalisisDatos_Streamlit/student_performance_data.csv'
PLOTS_DIR = 'eda_plots'
df = load_data(DATASET_PATH)


# --- Barra Lateral de Navegación ---
st.sidebar.title("🎓 SAAD ESENCIAL")
st.sidebar.markdown("Panel de Navegación")
page = st.sidebar.radio("Selecciona una sección:", [
    "Introducción",
    "Análisis Exploratorio (EDA)",
    "Análisis de Puntuaciones",
    "Análisis por Características",
    "Conclusiones"
])
st.sidebar.markdown("---")
st.sidebar.info(
    """**Proyecto:** SAAD ESENCIAL (Sistema de Alerta y Análisis de Datos).

**Objetivo:** Modelar y analizar un sistema de notas académicas para extraer insights."""
)


# --- Contenido de las Páginas ---

if df is not None:
    # --- Página de Introducción ---
    if page == "Introducción":
        st.title("Dashboard de Análisis de Rendimiento Estudiantil")
        st.markdown("---")
        st.markdown("""
            Bienvenido al dashboard del proyecto **SAAD ESENCIAL**. Esta aplicación interactiva presenta un análisis detallado
            del rendimiento de los estudiantes basado en el "Student Performance & Behavior Dataset".

            El objetivo de este dashboard es:
            - **Visualizar** de forma clara la distribución de las puntuaciones académicas.
            - **Analizar** la correlación entre diferentes asignaturas.
            - **Explorar** cómo diversas características demográficas y de hábitos de estudio influyen en el rendimiento académico.

            Utiliza el panel de navegación de la izquierda para moverte por las diferentes secciones del análisis.
        """)
        st.info("Este dashboard fue creado utilizando **Streamlit**, una librería de Python para construir aplicaciones de datos interactivas.", icon="💡")


    # --- Página de Análisis Exploratorio (EDA) ---
    elif page == "Análisis Exploratorio (EDA)":
        st.header("Análisis Exploratorio de Datos (EDA)")
        st.markdown("---")
        st.subheader("Vistazo a los Datos")
        if st.checkbox("Mostrar los primeros 10 registros del dataset"):
            st.dataframe(df.head(10))

        st.subheader("Estadísticas Descriptivas de las Puntuaciones")
        st.markdown("A continuación se muestran las estadísticas descriptivas para las puntuaciones numéricas:")
        st.table(df[['math_score', 'reading_score', 'writing_score']].describe())
        st.markdown("""
            **Interpretación:**
            - La **media** de las puntuaciones se sitúa alrededor de 66-69 puntos.
            - La **desviación estándar (std)** de ~15 puntos indica una dispersión considerable en las notas.
            - El **mínimo (min)** de 0 en matemáticas es un valor atípico que podría investigarse, mientras que los mínimos en lectura y escritura son más altos.
            - La diferencia entre el **75%** y el **máximo (max)** sugiere que hay un grupo de estudiantes con un rendimiento muy alto.
        """)
        
        st.subheader("Información del Dataset")
        # To get the info as a string, we capture the output
        from io import StringIO
        buffer = StringIO()
        df.info(buf=buffer)
        s = buffer.getvalue()
        st.text(s)


    # --- Página de Análisis de Puntuaciones ---
    elif page == "Análisis de Puntuaciones":
        st.header("Análisis Detallado de las Puntuaciones Académicas")
        st.markdown("---")

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Distribución de las Puntuaciones")
            dist_score = st.selectbox("Selecciona una puntuación para ver su distribución:", ['math_score', 'reading_score', 'writing_score'], key="dist")
            dist_img_path = os.path.join(PLOTS_DIR, f"distribution_{dist_score}.png")
            if os.path.exists(dist_img_path):
                image = Image.open(dist_img_path)
                st.image(image, caption=f"Distribución de {dist_score.replace('_', ' ').title()}")
            else:
                st.warning(f"No se encontró el gráfico para {dist_score}. Asegúrate de que los gráficos estén en la carpeta '{PLOTS_DIR}'.")
            
            st.markdown("""
                **Interpretación:**
                Las distribuciones de las tres puntuaciones se asemejan a una **distribución normal (curva de campana)**, lo cual es esperado en datos de rendimiento académico. La mayoría de los estudiantes se agrupan en torno a la media, con menos estudiantes en los extremos de puntuaciones muy bajas o muy altas.
            """)

        with col2:
            st.subheader("Correlación entre Puntuaciones")
            corr_img_path = os.path.join(PLOTS_DIR, "correlation_matrix.png")
            if os.path.exists(corr_img_path):
                image = Image.open(corr_img_path)
                st.image(image, caption="Mapa de Calor de la Correlación")
            else:
                st.warning(f"No se encontró el gráfico de correlación. Asegúrate de que esté en la carpeta '{PLOTS_DIR}'.")
            
            st.markdown("""
                **Interpretación:**
                Existe una **fuerte correlación positiva** entre las tres áreas de puntuación.
                - La correlación más alta se da entre **lectura y escritura (0.95)**, lo que sugiere que las habilidades en estas dos áreas están estrechamente relacionadas.
                - Las matemáticas también tienen una alta correlación con la lectura y la escritura (ambas >0.80).
                Esto indica que, en general, los estudiantes que tienen un buen rendimiento en un área, tienden a tenerlo también en las otras.
            """)


    # --- Página de Análisis por Características ---
    elif page == "Análisis por Características":
        st.header("Análisis de Puntuaciones por Características")
        st.markdown("---")
        st.markdown("Explora cómo las diferentes características demográficas y de hábitos de estudio se relacionan con las puntuaciones académicas.")

        col1, col2 = st.columns([1, 2])

        with col1:
            st.subheader("Filtros de Análisis")
            num_col_options = {'Puntuación de Matemáticas': 'math_score', 'Puntuación de Lectura': 'reading_score', 'Puntuación de Escritura': 'writing_score'}
            cat_col_options = {
                'Género': 'gender', 'Etnia': 'race/ethnicity', 'Nivel Educativo de los Padres': 'parental_level_of_education',
                'Tipo de Almuerzo': 'lunch', 'Curso de Preparación': 'test_preparation_course'
            }
            
            selected_num_col_label = st.selectbox("Selecciona la Puntuación a Analizar:", list(num_col_options.keys()))
            selected_cat_col_label = st.selectbox("Selecciona la Característica a Explorar:", list(cat_col_options.keys()))

            selected_num_col = num_col_options[selected_num_col_label]
            selected_cat_col = cat_col_options[selected_cat_col_label]

        with col2:
            st.subheader(f"Análisis de '{selected_num_col_label}' por '{selected_cat_col_label}'")
            
            # Generar el gráfico dinámicamente
            fig, ax = plt.subplots(figsize=(10, 6))
            sns.boxplot(x=selected_cat_col, y=selected_num_col, data=df, ax=ax, palette="viridis")
            plt.xticks(rotation=45, ha='right')
            plt.title(f"{selected_num_col_label} por {selected_cat_col_label}", fontsize=16)
            plt.xlabel(selected_cat_col_label, fontsize=12)
            plt.ylabel(selected_num_col_label, fontsize=12)
            plt.tight_layout()
            
            st.pyplot(fig)

            st.markdown("""
                **¿Cómo interpretar este gráfico?**
                - Cada **caja** representa el rango intercuartílico (IQR), donde se concentra el 50% central de los estudiantes para esa categoría.
                - La **línea dentro de la caja** es la mediana (el valor central).
                - Los **"bigotes"** se extienden para mostrar el rango de los datos, excluyendo valores atípicos (que se mostrarían como puntos individuales).
                - Compara las posiciones y tamaños de las cajas para identificar tendencias.
            """)
        
        st.markdown("---")
        st.subheader("Interpretaciones de las Relaciones")
        st.info("""
            - **Nivel Educativo de los Padres:** Generalmente, se observa una tendencia positiva. A mayor nivel educativo de los padres, las medianas de las puntuaciones de sus hijos tienden a ser más altas.
            - **Tipo de Almuerzo:** Los estudiantes con almuerzo "standard" tienden a obtener puntuaciones significativamente más altas que aquellos con almuerzo "free/reduced", lo que puede ser un indicador del estatus socioeconómico.
            - **Curso de Preparación:** Los estudiantes que completaron el curso de preparación para el examen muestran, en promedio, un rendimiento superior a los que no lo hicieron. Esto sugiere que el curso es efectivo.
            - **Género:** A menudo se observan ligeras diferencias, por ejemplo, las mujeres pueden tener un rendimiento ligeramente superior en lectura y escritura, mientras que los hombres pueden tenerlo en matemáticas.
        """, icon="🔍")


    # --- Página de Conclusiones ---
    elif page == "Conclusiones":
        st.header("Conclusiones Clave del Análisis")
        st.markdown("---")
        st.success("""
            **1. El Rendimiento Académico está Interconectado:**
            Las altas correlaciones entre las puntuaciones de matemáticas, lectura y escritura sugieren que las habilidades académicas son transferibles. Un estudiante con buen desempeño en un área probablemente lo tendrá en otras.
        """, icon="✅")
        st.success("""
            **2. El Contexto Familiar es un Factor Influyente:**
            El nivel educativo de los padres muestra una correlación positiva con las notas de los estudiantes. Esto destaca la importancia del entorno familiar en el éxito académico.
        """, icon="✅")
        st.success("""
            **3. El Estatus Socioeconómico (Indicado por el Almuerzo) es Clave:**
            La diferencia en el rendimiento entre estudiantes con almuerzo estándar y reducido es una de las más marcadas, señalando que las condiciones socioeconómicas son un predictor muy fuerte del rendimiento.
        """, icon="✅")
        st.success("""
            **4. La Preparación Funciona:**
            Los estudiantes que realizan un curso de preparación para el examen obtienen mejores resultados, lo que valida la eficacia de estas intervenciones.
        """, icon="✅")

        st.markdown("---")
        st.subheader("Próximos Pasos Sugeridos")
        st.markdown("""
            Basado en estos hallazgos, los siguientes pasos podrían ser:
            - **Desarrollar un Modelo Predictivo:** Utilizar las características más influyentes (como `parental_level_of_education`, `lunch`, y `test_preparation_course`) para construir un modelo de Machine Learning que pueda predecir el rendimiento de un estudiante.
            - **Identificar Estudiantes en Riesgo:** El modelo predictivo podría usarse para crear un "Sistema de Alerta Temprana" que identifique a los estudiantes con probabilidades de tener un bajo rendimiento, permitiendo intervenciones a tiempo.
            - **Análisis más Profundo:** Investigar el impacto combinado de varias características (ej. ¿El curso de preparación tiene el mismo efecto en todos los grupos socioeconómicos?).
        """)

else:
    st.error("No se pudo cargar el dataset. Por favor, revisa la ruta del archivo y los permisos.")

