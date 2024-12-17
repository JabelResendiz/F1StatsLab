import numpy as np
import pandas as pd
from scipy import stats

# Configuración de la semilla aleatoria para reproducibilidad
np.random.seed(42)

# Número de carreras a simular
n_races = 100

# Generar datos
race_id = np.arange(1, n_races + 1)
max_speed = np.random.normal(320, 10, n_races)  # Media 320 km/h, desviación estándar 10 km/h
overtakes = np.random.poisson(20, n_races)  # Media de 20 adelantamientos por carrera
pit_stop_time = np.random.exponential(2, n_races)  # Media de 2 segundos
race_completed = stats.bernoulli.rvs(0.9, size=n_races)  # 90% de probabilidad de completar la carrera
track_temp = np.random.normal(40, 5, n_races)  # Media 40°C, desviación estándar 5°C

# Lista de escuderías
teams = ['Mercedes', 'Red Bull', 'Ferrari', 'McLaren', 'Alpine', 'AlphaTauri', 'Aston Martin', 'Williams', 'Alfa Romeo', 'Haas']
winning_team = np.random.choice(teams, n_races)

# Crear DataFrame
df = pd.DataFrame({
    'RaceID': race_id,
    'MaxSpeed': max_speed,
    'Overtakes': overtakes,
    'PitStopTime': pit_stop_time,
    'RaceCompleted': race_completed,
    'WinningTeam': winning_team,
    'TrackTemp': track_temp
})

# Guardar a CSV
df.to_csv('f1_race_data_9090.csv', index=False)
print("Datos guardados en 'f1_race_data.csv'")

# Análisis de datos
print("\nAnálisis de datos:")

# 1. Cantidad de corredores por encima de cierta velocidad
speed_threshold = 330
fast_races = df[df['MaxSpeed'] > speed_threshold]
print(f"Carreras con velocidad máxima superior a {speed_threshold} km/h: {len(fast_races)}")

# 2. Escudería con la mayor cantidad de carreras ganadas
team_wins = df['WinningTeam'].value_counts()
print(f"\nEscudería con más victorias: {team_wins.index[0]} ({team_wins.iloc[0]} victorias)")

# 3. Correlación entre variables
correlation = df[['MaxSpeed', 'Overtakes', 'PitStopTime', 'TrackTemp']].corr()
print("\nMatriz de correlación:")
print(correlation)

# 4. Prueba de hipótesis: ¿La velocidad máxima es significativamente diferente de 320 km/h?
t_stat, p_value = stats.ttest_1samp(df['MaxSpeed'], 320)
print(f"\nPrueba t para velocidad máxima (H0: media = 320 km/h):")
print(f"Estadístico t: {t_stat:.4f}")
print(f"Valor p: {p_value:.4f}")

# 5. Test de independencia: ¿Hay relación entre la finalización de la carrera y la temperatura de la pista?
contingency_table = pd.crosstab(df['RaceCompleted'], df['TrackTemp'] > df['TrackTemp'].mean())
chi2, p_value, dof, expected = stats.chi2_contingency(contingency_table)
print(f"\nTest de independencia Chi-cuadrado (Finalización de carrera vs. Temperatura de pista):")
print(f"Estadístico Chi-cuadrado: {chi2:.4f}")
print(f"Valor p: {p_value:.4f}")