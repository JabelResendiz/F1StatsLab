import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar el dataset
df = pd.read_csv('f1_race_data_9090.csv')

# Configurar el estilo de seaborn
sns.set_style("whitegrid")
plt.figure(figsize=(20, 20))

# # 1. Distribución de edad
# plt.subplot(3, 3, 1)
# sns.histplot(df['Edad'], kde=True)
# plt.title('Distribución de Edad')

# # 2. Distribución de sexo
# plt.subplot(3, 3, 2)
# sns.countplot(x='Sexo', data=df)
# plt.title('Distribución de Sexo')

# 3. Distribución de presión arterial
plt.subplot(3, 3, 3)
sns.histplot(df['MaxSpeed'], kde=True)
plt.title('Distribución de la Velocidad Maxima')

# 4. Distribución de colesterol
plt.subplot(3, 3, 4)
sns.histplot(df['Overtakes'], kde=True)
plt.title('Distribución de los Overtakes')

# 5. Distribución de frecuencia cardíaca
plt.subplot(3, 3, 5)
sns.histplot(df['PitStopTime'], kde=True)
plt.title('Distribución de los PitStopTime')

# 6. Distribución de diabetes
plt.subplot(3, 3, 6)
sns.countplot(x='RaceCompleted', data=df)
plt.title('Distribución de RaceCompleted')

# 7. Distribución de fumadores
plt.subplot(3, 3, 7)
sns.countplot(x='WinningTeam', data=df)
plt.title('Distribución de Fumadores')

# 8. Distribución de IMC
plt.subplot(3, 3, 8)
sns.histplot(df['TrackTemp'], kde=True)
plt.title('Distribución de TrackTemp')

# # 9. Distribución de actividad física semanal
# plt.subplot(3, 3, 9)
# sns.histplot(df['Actividad_Fisica_Semanal'], kde=True, discrete=True)
# plt.title('Distribución de Actividad Física Semanal')

plt.tight_layout()
plt.savefig('f1_race_data_visualization.png')
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

