import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar el dataset
df = pd.read_csv('formula1_interlagos_data_final.csv')

df['WeatherCondition_Mixed'] = np.where(df['WeatherCondition'] == 'Mixed', 1, 0)
df['WeatherCondition_Wet'] = np.where(df['WeatherCondition'] == 'Wet', 1, 0)
df['WeatherCondition_Dry'] = np.where(df['WeatherCondition'] == 'Dry', 1, 0)

# Convertir las columnas booleanas a enteros (True -> 1, False -> 0)
df['WeatherCondition_Mixed'] = df['WeatherCondition_Mixed'].astype(int)
df['WeatherCondition_Wet'] = df['WeatherCondition_Wet'].astype(int)


df['TyreCompound_Medium'] = df['TyreCompound_Medium'].astype(int)
df['TyreCompound_Soft']= df['TyreCompound_Soft'].astype(int)

df['TrackGrip_Low']= df['TrackGrip_Low'].astype(int)
df['TrackGrip_Medium']= df['TrackGrip_Medium'].astype(int)

# Guardar el dfset con la nueva columna
df.to_csv('formula1_interlagos_df2_final.csv', index=False)
print("Datos guardados en 'formula1_interlagos_df2_final.csv'")

