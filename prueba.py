import pandas as pd
import requests
from io import StringIO

# # URL del archivo CSV
# url = 'https://hebbkx1anhila5yf.public.blob.vercel-storage.com/heart-nDetRTNwILhTrr1S4gaLfAC4HDHyYB.csv'

# # Obtener el contenido del archivo CSV
# response = requests.get(url)
# csv_content = StringIO(response.text)

# Leer el CSV en un DataFrame de pandas
df = pd.read_csv("heart.csv")

# Calcular el tamaño de la muestra
sample_size = len(df)

# Contar el número de hombres y mujeres
gender_counts = df['sex'].value_counts()

# Determinar qué valor corresponde a masculino/femenino
male_value = '1' if gender_counts.index[0] == 1 else '0'
female_value = '0' if male_value == '1' else '1'

# Imprimir los resultados
print(f"Tamaño de la muestra: {sample_size}")
print(f"Sexo 1 corresponde a: {'Masculino' if male_value == '1' else 'Femenino'}")
print(f"Número de hombres: {gender_counts[int(male_value)]}")
print(f"Número de mujeres: {gender_counts[int(female_value)]}")

# Mostrar las primeras 5 filas de los datos
print("\nPrimeras 5 filas de los datos:")
print(df.head())

# Información adicional sobre el DataFrame
print("\nInformación del DataFrame:")
print(df.info())