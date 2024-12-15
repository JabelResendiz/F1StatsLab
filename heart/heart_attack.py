import numpy as np
import pandas as pd

# Configurar la semilla aleatoria para reproducibilidad
np.random.seed(42)

# Número de muestras
n = 300

# Generar datos
edad = np.random.normal(60, 10, n).astype(int)
sexo = np.random.binomial(1, 0.6, n)  # 0: Mujer, 1: Hombre
presion_arterial = np.random.normal(130, 20, n).astype(int)
colesterol = np.random.normal(200, 40, n).astype(int)
frecuencia_cardiaca = np.random.normal(75, 10, n).astype(int)
diabetes = np.random.binomial(1, 0.2, n)
fumador = np.random.binomial(1, 0.3, n)
imc = np.random.normal(27, 5, n)
actividad_fisica = np.random.poisson(3, n)
tiempo_ultimo_chequeo = np.random.exponential(12, n).astype(int)

# Crear el DataFrame
df = pd.DataFrame({
    'Edad': edad,
    'Sexo': sexo,
    'Presion_Arterial': presion_arterial,
    'Colesterol': colesterol,
    'Frecuencia_Cardiaca': frecuencia_cardiaca,
    'Diabetes': diabetes,
    'Fumador': fumador,
    'IMC': imc.round(2),
    'Actividad_Fisica_Semanal': actividad_fisica,
    'Meses_Desde_Ultimo_Chequeo': tiempo_ultimo_chequeo
})

# Mostrar las primeras filas del dataset
print("Primeras filas del dataset:")
print(df.head())

# Mostrar un resumen estadístico
print("\nResumen estadístico:")
print(df.describe())

# Guardar el dataset en un archivo CSV
df.to_csv('heart_attack_dataset.csv', index=False)
print("\nDataset guardado como 'heart_attack_dataset.csv'")