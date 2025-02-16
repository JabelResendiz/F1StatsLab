import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import statsmodels.api as sm

# Cargar el dataset
data = pd.read_csv("formula1_interlagos_data_final.csv")

# Imprimir nombres de columnas
print("Available columns:")
print(data.columns.tolist())

circuit_name = 'Interlagos'
    
circuit_data = data[data['Circuit'] == circuit_name].copy()  

if circuit_data.empty:
    print(f"No data found for circuit {circuit_name}")
    print("Available circuits:")
    print(data['Circuit'])  
else:
    print(f"Data for circuit {circuit_name}:")
    # print(circuit_data.head()) 

print(f"\nAnalyzing data for circuit: {circuit_name}")
print(f"Number of races: {len(circuit_data)}")

# Seleccionar las características relevantes
features = ['MaxSpeed', 'DriverSkill', 'Experience', 'TyreWear', 'TyreCompounds']
target = 'FinalRaceTime'

# Verificar si las columnas existen y eliminar aquellas que no
features = [f for f in features if f in data.columns]
if target not in data.columns:
    raise ValueError(f"Target column '{target}' not found in the dataset")

print(f"\nUsing features: {features}")
print(f"Number of features : {len(features)}")
print(f"Target: {target}")

# Convertir las características a numéricas (si es necesario)
for feature in features:
    circuit_data[feature] = pd.to_numeric(circuit_data[feature], errors='coerce')
circuit_data = circuit_data.dropna(subset=features + [target])

# Crear variables dummies para 'TyreCompounds'
if 'TyreCompounds' in features:
    tyre_compounds_dummies = pd.get_dummies(circuit_data['TyreCompounds'], prefix='TyreCompounds', drop_first=True)
    circuit_data = pd.concat([circuit_data, tyre_compounds_dummies], axis=1)
    features.remove('TyreCompounds')  # Eliminar la columna original 'TyreCompounds'

# Separar las características (X) y la variable objetivo (y)
X = circuit_data[features + tyre_compounds_dummies.columns.tolist()]
y = circuit_data[target]

# Dividir los datos en conjunto de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Escalar las características
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Crear y entrenar el modelo
model = LinearRegression()
model.fit(X_train_scaled, y_train)

# Imprimir la ecuación del plano
coefficients = model.coef_
intercept = model.intercept_

print("\nEquation of the hyperplane:")
equation = f"FinalRiceTime = {intercept:.2f}"
for feature, coef in zip(features + tyre_compounds_dummies.columns.tolist(), coefficients):
    equation += f" + ({coef:.2f} * {feature})"
print(equation)

# Calcular R-squared
r_squared = model.score(X_test_scaled, y_test)
print(f"\nR-squared: {r_squared:.4f}")

# Agregar constante para la intersección en statsmodels
X_train_const = sm.add_constant(X_train_scaled)

# Ajustar el modelo de regresión con statsmodels
model_sm = sm.OLS(y_train, X_train_const).fit()

# Mostrar los p-values de cada coeficiente
print(model_sm.summary())
