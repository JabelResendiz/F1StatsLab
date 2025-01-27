import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import requests
from io import StringIO

# Descargar y leer el archivo CSV

df = pd.read_csv('formula1_enhanced_data.csv')


# Convertir columnas a tipo numérico
numeric_columns = ['Age', 'PitStopTime', 'ReactionTime', 'FinalPosition', 'DNF', 'Points', 'MaxSpeed', 'Overtakes']
df[numeric_columns] = df[numeric_columns].apply(pd.to_numeric, errors='coerce')

# Modificar y añadir nuevas columnas con relaciones más fuertes
df['Experience'] = np.random.randint(1, 20, len(df))
df['DriverSkill'] = 50 + 2 * df['Experience'] + np.random.normal(0, 5, len(df))
df['CarPerformance'] = np.random.uniform(80, 100, len(df))
df['TrackFamiliarity'] = np.random.uniform(0, 10, len(df))
df['WeatherCondition'] = np.random.choice(['Dry', 'Wet', 'Mixed'], len(df))
df['TyreCompound'] = np.random.choice(['Soft', 'Medium', 'Hard'], len(df))
df['EngineMode'] = np.random.uniform(1, 10, len(df))

# Crear distribución normal para los tiempos de pit stop
mean_pit_stop = 2.5
std_pit_stop = 0.3
df['PitStopTime'] = np.random.normal(mean_pit_stop, std_pit_stop, len(df))
df['PitStopTime'] = df['PitStopTime'].clip(1.8, 4)  # Limitar valores extremos

# Ajustar los tiempos de pit stop basados en el rendimiento del coche y las condiciones
df['PitStopTime'] += (100 - df['CarPerformance']) * 0.01
df.loc[df['WeatherCondition'] == 'Wet', 'PitStopTime'] += 0.5

# Crear distribución normal para la velocidad máxima
mean_max_speed = 330
std_max_speed = 10
df['MaxSpeed'] = np.random.normal(mean_max_speed, std_max_speed, len(df))

# Ajustar la velocidad máxima basada en el rendimiento del coche y las condiciones
df['MaxSpeed'] += (df['CarPerformance'] - 90) * 0.5
df['MaxSpeed'] -= (df['DownforceLevel'] - 1000) * 0.02
df.loc[df['WeatherCondition'] == 'Wet', 'MaxSpeed'] -= 20
df['MaxSpeed'] = df['MaxSpeed'].clip(300, 360)  # Limitar valores extremos

# Resto del código para otras variables
df['QualifyingPosition'] = 20 - (df['DriverSkill'] + df['CarPerformance']) / 15 + np.random.normal(0, 1, len(df))
df['QualifyingPosition'] = df['QualifyingPosition'].clip(1, 20).round()

df['Overtakes'] = (20 - df['QualifyingPosition']) * 0.5 + (df['DriverSkill'] - 50) * 0.1 + np.random.poisson(2, len(df))
df['Overtakes'] = df['Overtakes'].clip(0, 20)

df['TyreWear'] = np.where(df['TyreCompound'] == 'Soft', np.random.uniform(60, 100, len(df)),
                          np.where(df['TyreCompound'] == 'Medium', np.random.uniform(40, 80, len(df)),
                                   np.random.uniform(20, 60, len(df))))

df['FuelConsumption'] = 1.5 + (df['MaxSpeed'] - 330) * 0.005 + (df['EngineMode'] - 5) * 0.05 + np.random.normal(0, 0.05, len(df))

df['DownforceLevel'] = 1000 - (df['MaxSpeed'] - 330) * 2 + np.random.normal(0, 20, len(df))

df['ReactionTime'] = 0.5 - (df['DriverSkill'] - 50) * 0.002 + (df['Age'] - 25) * 0.001 + np.random.normal(0, 0.02, len(df))
df['ReactionTime'] = df['ReactionTime'].clip(0.2, 0.8)

# Calcular la posición final y los puntos
df['FinalPosition'] = df['QualifyingPosition'] - df['Overtakes'] * 0.5 + np.random.normal(0, 1, len(df))
df['FinalPosition'] = df['FinalPosition'].clip(1, 20).round()

points_map = {1: 25, 2: 18, 3: 15, 4: 12, 5: 10, 6: 8, 7: 6, 8: 4, 9: 2, 10: 1}
df['Points'] = df['FinalPosition'].map(lambda x: points_map.get(x, 0))

# Ajustar DNF basado en varias condiciones
df['DNF'] = ((df['TyreWear'] > 90) | (df['FuelConsumption'] > 2.3) | (df['WeatherCondition'] == 'Wet')).astype(int)
df.loc[df['DNF'] == 1, 'Points'] = 0
df.loc[df['DNF'] == 1, 'FinalPosition'] = 20

# Calcular la matriz de correlación
corr_columns = ['Age', 'Experience', 'DriverSkill', 'CarPerformance', 'TrackFamiliarity', 'PitStopTime', 
                'ReactionTime', 'FinalPosition', 'Points', 'MaxSpeed', 'Overtakes', 'QualifyingPosition', 
                'TyreWear', 'FuelConsumption', 'DownforceLevel', 'EngineMode']
corr_matrix = df[corr_columns].corr()

# Visualizar la matriz de correlación
plt.figure(figsize=(16, 14))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1, center=0, fmt='.2f')
plt.title('Matriz de Correlación de Variables en F1')
plt.tight_layout()
plt.show()

# Visualizar las distribuciones de PitStopTime y MaxSpeed
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 5))

sns.histplot(df['PitStopTime'], kde=True, ax=ax1)
ax1.set_title('Distribución de Tiempos de Pit Stop')
ax1.set_xlabel('Tiempo (segundos)')

sns.histplot(df['MaxSpeed'], kde=True, ax=ax2)
ax2.set_title('Distribución de Velocidad Máxima')
ax2.set_xlabel('Velocidad (km/h)')

plt.tight_layout()
plt.show()

# Mostrar las primeras filas del DataFrame modificado
print(df[corr_columns].head())

# Guardar el DataFrame modificado
df.to_csv('formula1_enhanced_data_normal.csv', index=False)
print("Datos mejorados con distribuciones normales guardados en 'formula1_enhanced_data_normal.csv'")