

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Cargar los datos
df = pd.read_csv('./formula1/formula1_race_data.csv')

print(df["Driver"].value_counts())


df.head(10).plot(kind='bar', figsize=(10, 6), color='skyblue')
plt.title('Top 10 Pilotos con Más Participaciones')
plt.ylabel('Número de Participaciones')
plt.xlabel('Piloto')
plt.show()



dnf_rate = df.groupby("Driver")["DNF"].mean()
print(dnf_rate.sort_values(ascending=False).head(10))