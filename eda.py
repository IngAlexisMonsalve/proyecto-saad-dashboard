import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Define the path to the dataset
dataset_path = 'ProyectoSAAD_NotasAcademicas/Fase_IV_AnalisisDatos_Streamlit/student_performance_data.csv'

# Create a directory for plots if it doesn't exist
plots_dir = 'eda_plots'
os.makedirs(plots_dir, exist_ok=True)

# Load the dataset
try:
    df = pd.read_csv(dataset_path, delimiter=';')
    print(f"Dataset '{dataset_path}' loaded successfully.")
except FileNotFoundError:
    print(f"Error: The file '{dataset_path}' was not found. Please ensure it is in the correct directory.")
    exit()

print("\n--- First 5 rows of the dataset ---")
print(df.head())

print("\n--- Dataset Info ---")
df.info()

print("\n--- Descriptive Statistics ---")
print(df.describe())

print("\n--- Missing Values ---")
print(df.isnull().sum())

print("\n--- Unique Values for Object (Categorical) Columns ---")
for column in df.select_dtypes(include='object').columns:
    print(f"\nUnique values for '{column}':")
    print(df[column].unique())

# --- Additional EDA: Correlation Analysis and Visualizations ---

print("\n--- Correlation Matrix for Numerical Scores ---")
numerical_cols = ['math score', 'reading score', 'writing score']
correlation_matrix = df[numerical_cols].corr()
print(correlation_matrix)

plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Matrix of Academic Scores')
plt.savefig(os.path.join(plots_dir, 'correlation_matrix.png'))
plt.close()
print(f"Correlation matrix plot saved to {os.path.join(plots_dir, 'correlation_matrix.png')}")

print("\n--- Visualizing Distributions of Academic Scores ---")
for col in numerical_cols:
    plt.figure(figsize=(8, 6))
    sns.histplot(df[col], kde=True, bins=20)
    plt.title(f'Distribution of {col}')
    plt.xlabel(col)
    plt.ylabel('Frequency')
    plt.savefig(os.path.join(plots_dir, f'distribution_{col.lower().replace(" ", "_")}.png'))
    plt.close()
    print(f"Distribution plot for {col} saved to {os.path.join(plots_dir, f'distribution_{col.lower().replace(' ', '_')}.png')}")

print("\n--- Visualizing Relationships between Categorical Features and Academic Scores ---")
categorical_cols = df.select_dtypes(include='object').columns.tolist()

for cat_col in categorical_cols:
    for num_col in numerical_cols:
        plt.figure(figsize=(10, 7))
        sns.boxplot(x=cat_col, y=num_col, data=df)
        plt.title(f'{num_col} by {cat_col}')
        plt.xlabel(cat_col)
        plt.ylabel(num_col)
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        sanitized_cat_col = cat_col.lower().replace(" ", "_").replace("/", "_")
        plt.savefig(os.path.join(plots_dir, f'{num_col.lower().replace(" ", "_")}_by_{sanitized_cat_col}.png'))
        plt.close()
        print(f"Box plot for {num_col} by {cat_col} saved to {os.path.join(plots_dir, f'{num_col.lower().replace(' ', '_')}_by_{cat_col.lower().replace(' ', '_')}.png')}")

print("\nExploratory Data Analysis (EDA) completed, including correlation and visualizations.")
print(f"\nAll generated plots are saved in the '{plots_dir}' directory.")
print("\nIf you encounter any errors related to 'matplotlib' or 'seaborn', please install them using:")
print("pip install matplotlib seaborn")
