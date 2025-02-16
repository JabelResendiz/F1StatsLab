import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar el dataset
df = pd.read_csv('formula1/formula1_enhanced_data_final.csv')

# Definir coeficientes basados en relaciones esperadas
coeff_experience = -0.3  # Más experiencia reduce el tiempo
coeff_max_speed = -0.1  # Más velocidad reduce el tiempo
coeff_weather = {'Dry': 0, 'Mixed': 5, 'Wet': 12}  # Clima afecta el tiempo
coeff_tyre = {'Soft': -2, 'Medium': 0, 'Hard': 3}  # Tipo de neumático afecta el tiempo

# 🔹 Nuevo: Coeficientes para Temperatura y Track Grip en Interlagos
coeff_temperature = -0.15  # Mayor temperatura, mayor degradación, pero más grip
coeff_track_grip = {'Low': 5, 'Medium': 0, 'High': -3}  # Bajo grip aumenta el tiempo

# 🔹 Generar datos para temperatura y track grip en Interlagos
np.random.seed(42)
df['TrackTemperature'] = np.random.uniform(20, 45, len(df))  # Temperaturas entre 20°C y 45°C
df['TrackGrip'] = np.random.choice(['Low', 'Medium', 'High'], size=len(df), p=[0.3, 0.5, 0.2])  # Más probabilidad de Medium

# 🔹 Calcular la variable FinalRaceTime con los nuevos factores
base_time = 300  # Base en segundos para una carrera típica

df['FinalRaceTime'] = (
    base_time +
    df['Experience'] * coeff_experience +
    df['MaxSpeed'] * coeff_max_speed +
    df['WeatherCondition'].map(coeff_weather) +
    df['TyreCompound'].map(coeff_tyre) +
    df['TrackTemperature'] * coeff_temperature +  # 🔹 Impacto de la temperatura
    df['TrackGrip'].map(coeff_track_grip) +  # 🔹 Impacto del grip
    np.random.normal(0, 5, len(df))  # Agregar ruido aleatorio
)

# Asegurar valores lógicos
df['FinalRaceTime'] = df['FinalRaceTime'].clip(150, 400)

# 🔹 Visualizar la distribución de tiempos de carrera en Interlagos
plt.figure(figsize=(8,5))
sns.histplot(df['FinalRaceTime'], bins=30, kde=True, color="blue")
plt.xlabel('Tiempo Final de Carrera (segundos)')
plt.title('Distribución de Tiempos Finales de Carrera en Interlagos')
plt.show()

df = pd.get_dummies(df, columns=['WeatherCondition', 'TyreCompound', 'TrackGrip'], drop_first=True)

# Guardar el dataset con la nueva columna
df.to_csv('formula1_interlagos_data_final.csv', index=False)
print("Datos guardados en 'formula1_interlagos_data_final.csv'")

df = pd.get_dummies(df, columns=['TrackGrip'], drop_first=True)
