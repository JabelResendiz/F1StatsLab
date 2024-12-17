import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import numpy as np

# Cargar los datos
#url = "https://hebbkx1anhila5yf.public.blob.vercel-storage.com/winequality-red-GI1CNwHAjMooE60inBIjaoIus8Dus3.csv"
df = pd.read_csv('winequality-red.csv')

# Convertir todas las columnas a tipo numérico
for col in df.columns:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Seleccionar pares de variables para análisis
pairs = [
    ('alcohol', 'quality'),
    ('sulphates', 'quality'),
    ('pH', 'fixed acidity'),
    ('citric acid', 'volatile acidity')
]

# Función para dibujar gráficos de dispersión y calcular correlación
def plot_scatter_and_correlation(x, y):
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, x=x, y=y)
    plt.title(f'Relación entre {x} y {y}')
    plt.xlabel(x)
    plt.ylabel(y)
    
    correlation, _ = stats.pearsonr(df[x], df[y])
    plt.text(0.05, 0.95, f'Correlación: {correlation:.2f}', transform=plt.gca().transAxes)
    
    plt.show()

# Función para calcular y mostrar estadísticas descriptivas
def show_descriptive_stats(variable):
    stats = df[variable].describe()
    print(f"\nEstadísticas descriptivas para {variable}:")
    print(stats)
    print(f"Varianza: {df[variable].var():.4f}")

# Análisis para cada par de variables
for x, y in pairs:
    print(f"\nAnálisis para {x} y {y}")
    
    # Dibujar gráfico de dispersión y calcular correlación
    plot_scatter_and_correlation(x, y)
    
    # Mostrar estadísticas descriptivas
    show_descriptive_stats(x)
    show_descriptive_stats(y)
    
    # Proponer y probar hipótesis
    print("\nHipótesis:")
    if x == 'alcohol' and y == 'quality':
        print("H0: No hay correlación entre el contenido de alcohol y la calidad del vino.")
        print("H1: Existe una correlación positiva entre el contenido de alcohol y la calidad del vino.")
        
        correlation, p_value = stats.pearsonr(df[x], df[y])
        print(f"Coeficiente de correlación: {correlation:.4f}")
        print(f"Valor p: {p_value:.4f}")
        
        if p_value < 0.05:
            print("Rechazamos H0: Hay evidencia de una correlación significativa.")
        else:
            print("No podemos rechazar H0: No hay evidencia suficiente de una correlación significativa.")
    
    elif x == 'sulphates' and y == 'quality':
        print("H0: El contenido de sulfatos no afecta la calidad del vino.")
        print("H1: El contenido de sulfatos afecta positivamente la calidad del vino.")
        
        correlation, p_value = stats.pearsonr(df[x], df[y])
        print(f"Coeficiente de correlación: {correlation:.4f}")
        print(f"Valor p: {p_value:.4f}")
        
        if p_value < 0.05:
            print("Rechazamos H0: Hay evidencia de que los sulfatos afectan la calidad del vino.")
        else:
            print("No podemos rechazar H0: No hay evidencia suficiente de que los sulfatos afecten la calidad del vino.")
    
    elif x == 'pH' and y == 'fixed acidity':
        print("H0: No hay relación entre el pH y la acidez fija.")
        print("H1: Existe una relación negativa entre el pH y la acidez fija.")
        
        correlation, p_value = stats.pearsonr(df[x], df[y])
        print(f"Coeficiente de correlación: {correlation:.4f}")
        print(f"Valor p: {p_value:.4f}")
        
        if p_value < 0.05:
            print("Rechazamos H0: Hay evidencia de una relación significativa entre pH y acidez fija.")
        else:
            print("No podemos rechazar H0: No hay evidencia suficiente de una relación entre pH y acidez fija.")
    
    elif x == 'citric acid' and y == 'volatile acidity':
        print("H0: No hay relación entre el ácido cítrico y la acidez volátil.")
        print("H1: Existe una relación negativa entre el ácido cítrico y la acidez volátil.")
        
        correlation, p_value = stats.pearsonr(df[x], df[y])
        print(f"Coeficiente de correlación: {correlation:.4f}")
        print(f"Valor p: {p_value:.4f}")
        
        if p_value < 0.05:
            print("Rechazamos H0: Hay evidencia de una relación significativa entre ácido cítrico y acidez volátil.")
        else:
            print("No podemos rechazar H0: No hay evidencia suficiente de una relación entre ácido cítrico y acidez volátil.")

# Calcular y mostrar la matriz de correlación
plt.figure(figsize=(12, 10))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Matriz de Correlación de Variables del Vino')
plt.show()

# Análisis adicional: Distribución de la calidad del vino
plt.figure(figsize=(10, 6))
sns.histplot(data=df, x='quality', kde=True)
plt.title('Distribución de la Calidad del Vino')
plt.xlabel('Calidad')
plt.ylabel('Frecuencia')
plt.show()

# Estimadores para la calidad del vino
quality_mean = df['quality'].mean()
quality_median = df['quality'].median()
quality_mode = df['quality'].mode().values[0]

print("\nEstimadores para la calidad del vino:")
print(f"Media: {quality_mean:.2f}")
print(f"Mediana: {quality_median:.2f}")
print(f"Moda: {quality_mode}")

# Intervalo de confianza para la media de la calidad del vino
confidence_interval = stats.t.interval(alpha=0.95, df=len(df)-1, loc=quality_mean, scale=stats.sem(df['quality']))
print(f"\nIntervalo de confianza del 95% para la media de la calidad: ({confidence_interval[0]:.2f}, {confidence_interval[1]:.2f})")