import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import requests
from io import StringIO

# Descargar y leer el archivo CSV

df = pd.read_csv('formula1/formula1_race_data.csv')

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

# Crear relaciones más fuertes entre variables
df['QualifyingPosition'] = 20 - (df['DriverSkill'] + df['CarPerformance']) / 15 + np.random.normal(0, 1, len(df))
df['QualifyingPosition'] = df['QualifyingPosition'].clip(1, 20).round()

df['MaxSpeed'] = df ['MaxSpeed']
# df['MaxSpeed'] = 300 + (df['CarPerformance'] * 0.5) + (df['DriverSkill'] * 0.2) - (df['DownforceLevel'] * 0.05) + np.random.normal(0, 2, len(df))

df['Overtakes'] = (20 - df['QualifyingPosition']) * 0.5 + (df['DriverSkill'] - 50) * 0.1 + np.random.poisson(2, len(df))
df['Overtakes'] = df['Overtakes'].clip(0, 20)

# df['PitStopTime'] = 2 + (100 - df['CarPerformance']) * 0.02 + np.random.normal(0, 0.1, len(df))
# df['PitStopTime'] = df['PitStopTime'].clip(1.8, 4)
df ['PitStopTime'] = df['PitStopTime']



df['TyreWear'] = np.where(df['TyreCompound'] == 'Soft', np.random.uniform(60, 100, len(df)),
                          np.where(df['TyreCompound'] == 'Medium', np.random.uniform(40, 80, len(df)),
                                   np.random.uniform(20, 60, len(df))))

df['FuelConsumption'] = 1.5 + (df['MaxSpeed'] - 300) * 0.005 + (df['EngineMode'] - 5) * 0.05 + np.random.normal(0, 0.05, len(df))

df['DownforceLevel'] = 1000 - (df['MaxSpeed'] - 300) * 2 + np.random.normal(0, 20, len(df))

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

# Mostrar las primeras filas del DataFrame modificado
print(df[corr_columns].head())

# Guardar el DataFrame modificado
df.to_csv('formula1_enhanced_data.csv', index=False)
print("Datos mejorados guardados en 'formula1_enhanced_data.csv'")