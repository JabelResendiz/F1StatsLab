import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Cargar los datos
df = pd.read_csv('formula1_race_data.csv')

# Configuración de la visualización
plt.figure(figsize=(15, 20))
sns.set()

# 1. Distribución normal: Edad de los pilotos
plt.subplot(3, 2, 1)
sns.histplot(df['Age'], kde=True)
plt.title('Distribución de la edad de los pilotos')
plt.xlabel('Edad')
plt.show()
# 2. Distribución normal: Tiempo de pit stop
plt.subplot(3, 2, 2)
sns.histplot(df['PitStopTime'], kde=True)
plt.title('Distribución del tiempo de pit stop')
plt.xlabel('Tiempo (segundos)')
plt.show()
# 3. Distribución exponencial: Tiempo de reacción
plt.subplot(3, 2, 3)
sns.histplot(df['ReactionTime'], kde=True)
plt.title('Distribución del tiempo de reacción')
plt.xlabel('Tiempo (segundos)')

# 4. Distribución uniforme: Posición final
plt.subplot(3, 2, 4)
sns.histplot(df['FinalPosition'], kde=True, discrete=True)
plt.title('Distribución de la posición final')
plt.xlabel('Posición')

# 5. Distribución de Bernoulli: DNF
plt.subplot(3, 2, 5)
sns.countplot(x='DNF', data=df)
plt.title('Distribución de DNF (Did Not Finish)')
plt.xlabel('DNF')

# 6. Distribución de Poisson: Número de adelantamientos
plt.subplot(3, 2, 6)
sns.histplot(df['Overtakes'], kde=True, discrete=True)
plt.title('Distribución del número de adelantamientos')
plt.xlabel('Número de adelantamientos')

plt.tight_layout()
plt.savefig('f1_distributions.png')


print("Se ha generado el gráfico 'f1_distributions.png' con las distribuciones de las variables.")

# Pruebas estadísticas para confirmar las distribuciones
print("\nPruebas estadísticas para confirmar las distribuciones:")

# Test de normalidad para la edad
_, p_value = stats.normaltest(df['Age'])
print(f"Test de normalidad para la edad: p-value = {p_value:.4f}")

# Test de exponencialidad para el tiempo de reacción
_, p_value = stats.kstest(df['ReactionTime'], 'expon')
print(f"Test de exponencialidad para el tiempo de reacción: p-value = {p_value:.4f}")

# Test de uniformidad para la posición final
_, p_value = stats.kstest(df['FinalPosition'], 'uniform', args=(1, 20))
print(f"Test de uniformidad para la posición final: p-value = {p_value:.4f}")

# Test de Poisson para el número de adelantamientos
_, p_value = stats.kstest(df['Overtakes'], 'poisson', args=(df['Overtakes'].mean(),))
print(f"Test de Poisson para el número de adelantamientos: p-value = {p_value:.4f}")