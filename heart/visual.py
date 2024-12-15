import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar el dataset
df = pd.read_csv('heart_attack_dataset.csv')

# Configurar el estilo de seaborn
sns.set_style("whitegrid")
plt.figure(figsize=(20, 20))

# 1. Distribución de edad
plt.subplot(3, 3, 1)
sns.histplot(df['Edad'], kde=True)
plt.title('Distribución de Edad')

# 2. Distribución de sexo
plt.subplot(3, 3, 2)
sns.countplot(x='Sexo', data=df)
plt.title('Distribución de Sexo')

# 3. Distribución de presión arterial
plt.subplot(3, 3, 3)
sns.histplot(df['Presion_Arterial'], kde=True)
plt.title('Distribución de Presión Arterial')

# 4. Distribución de colesterol
plt.subplot(3, 3, 4)
sns.histplot(df['Colesterol'], kde=True)
plt.title('Distribución de Colesterol')

# 5. Distribución de frecuencia cardíaca
plt.subplot(3, 3, 5)
sns.histplot(df['Frecuencia_Cardiaca'], kde=True)
plt.title('Distribución de Frecuencia Cardíaca')

# 6. Distribución de diabetes
plt.subplot(3, 3, 6)
sns.countplot(x='Diabetes', data=df)
plt.title('Distribución de Diabetes')

# 7. Distribución de fumadores
plt.subplot(3, 3, 7)
sns.countplot(x='Fumador', data=df)
plt.title('Distribución de Fumadores')

# 8. Distribución de IMC
plt.subplot(3, 3, 8)
sns.histplot(df['IMC'], kde=True)
plt.title('Distribución de IMC')

# 9. Distribución de actividad física semanal
plt.subplot(3, 3, 9)
sns.histplot(df['Actividad_Fisica_Semanal'], kde=True, discrete=True)
plt.title('Distribución de Actividad Física Semanal')

plt.tight_layout()
plt.savefig('heart_attack_data_visualization.png')
plt.close()

# Crear un heatmap de correlación
plt.figure(figsize=(12, 10))
numeric_cols = ['Edad', 'Presion_Arterial', 'Colesterol', 'Frecuencia_Cardiaca', 'IMC', 'Actividad_Fisica_Semanal', 'Meses_Desde_Ultimo_Chequeo']
corr = df[numeric_cols].corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Matriz de Correlación de Variables Numéricas')
plt.savefig('heart_attack_data_correlation.png')
plt.close()

print("Visualizaciones guardadas como 'heart_attack_data_visualization.png' y 'heart_attack_data_correlation.png'")

