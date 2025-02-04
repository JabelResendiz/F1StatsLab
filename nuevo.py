import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar el dataset
df = pd.read_csv('formula1_enhanced_data.csv')

# Definir coeficientes basados en relaciones esperadas
coeff_experience = -0.3  # Menos tiempo con más experiencia
coeff_max_speed = -0.1  # Menos tiempo con mayor velocidad
coeff_weather = {'Dry': 0, 'Mixed': 5, 'Wet': 12}  # Penalización por clima
coeff_tyre = {'Soft': -2, 'Medium': 0, 'Hard': 3}  # Dureza del neumático afecta el tiempo

# Generar la variable FinalRaceTime
base_time = 300  # Base en segundos para una carrera típica

df['FinalRaceTime'] = (
    base_time +
    df['Experience'] * coeff_experience +
    df['MaxSpeed'] * coeff_max_speed +
    df['WeatherCondition'].map(coeff_weather) +
    df['TyreCompound'].map(coeff_tyre) +
    np.random.normal(0, 5, len(df))  # Agregar algo de variabilidad
)

# Asegurar que los tiempos sean positivos y lógicos
df['FinalRaceTime'] = df['FinalRaceTime'].clip(150, 400)

# Visualizar la nueva variable con un histograma
plt.figure(figsize=(8,5))
sns.histplot(df['FinalRaceTime'], bins=30, kde=True, color="blue")
plt.xlabel('Tiempo Final de Carrera (segundos)')
plt.title('Distribución de Tiempos Finales de Carrera')
plt.show()

# Guardar el dataset con la nueva columna
df.to_csv('formula1_enhanced_data_final.csv', index=False)
print("Datos guardados en 'formula1_enhanced_data_final.csv'")
