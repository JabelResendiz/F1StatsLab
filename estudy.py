

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Cargar los datos
df = pd.read_csv('./formula1/formula1_race_data.csv')


driver= df[df["Driver"]=='Hamilton']

# Asegurarse de que RaceDate sea de tipo fecha
df["Date"] = pd.to_datetime(df["Date"])

# Crear una columna de año
df["Year"] = df["Date"].dt.year

# Agrupar por año y sumar los adelantamientos
overtakes_per_year = df.groupby("Year")["Overtakes"].sum()

# Mostrar los adelantamientos por año
print(overtakes_per_year)
