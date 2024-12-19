
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as st
from scipy.stats import shapiro

df = pd.read_csv('./formula1/formula1_race_data.csv')

filtred = df[df['Pit']>30]
filtred2=  df[df['Age']<=30]
pit_stop_times = filtred['MaxSpeed']
pit_stop_times_2 = filtred2['MaxSpeed']

print(len(filtred))
print(len(filtred2))
print(pit_stop_times)
print(pit_stop_times_2)


stat, p_value = st.normaltest(pit_stop_times)

print(f"Stat = {stat}, p_value = {p_value}")

if p_value > 0.05:
    print("El tiempo de los pits stops parece estar normalmente distribuidos (no se rechaza H0)")

else:
    print("El tiempo de los pits stops no parece estar normalmente distribuidos (se rechaza H0)\n")


# menor de 30 
stat, p_value = shapiro(pit_stop_times_2)

print(f"Stat = {stat}, p_value = {p_value}")

if p_value > 0.05:
    print("El tiempo de los pits stops parece estar normalmente distribuidos (no se rechaza H0)")

else:
    print("El tiempo de los pits stops no parece estar normalmente distribuidos (se rechaza H0)\n")

plt.figure(figsize=(10, 6))
plt.hist(pit_stop_times_2, bins=20, edgecolor='black')
plt.title('Distribución de Pit Stop Times para Edad Mayor de 30')
plt.xlabel('Pit Stop Time')
plt.ylabel('Frecuencia')
plt.grid(True)
plt.show()
