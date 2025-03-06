import pandas as pd
import numpy as np
import statsmodels.api as sm
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.feature_selection import SequentialFeatureSelector

def load_data(filepath, circuit_name):
    data = pd.read_csv(filepath)
    circuit_data = data[data['Circuit'] == circuit_name].copy()
    if circuit_data.empty:
        raise ValueError(f"No data found for circuit {circuit_name}")
    return circuit_data

def select_features(data, target, initial_features):
    features = [f for f in initial_features if f in data.columns]
    if target not in data.columns:
        raise ValueError(f"Target column '{target}' not found in the dataset")
    return features

def preprocess_data(data, features, target):
    for feature in features:
        data[feature] = pd.to_numeric(data[feature], errors='coerce')
    data = data.dropna(subset=features + [target])
    return data

def train_model(X, y):
    
    # Split into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Scale the features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)


    # Create and train the model
    model = LinearRegression()
    model.fit(X_train_scaled, y_train)

    # Print the equation of the hyperplane
    coefficients = model.coef_
    intercept = model.intercept_

    #print("\nEquation of the hyperplane:")
    equation = f"FinalRiceTime = {intercept:.2f}"
    for feature, coef in zip(features, coefficients):
        equation += f" + ({coef:.2f} * {feature})"
    #print(equation)

    # Calculate R-squared
    r_squared = model.score(X_test_scaled, y_test)
    
   
# Agregar constante para la intersección
    X_train_const = sm.add_constant(X_train_scaled)


# Ajustar el modelo de regresión con statsmodels
    model_sm = sm.OLS(y_train, X_train_const).fit()

# Mostrar los p-values de cada coeficiente
    #print(model_sm.summary())

# Create a DataFrame for coefficients and p-values
    summary_df = pd.DataFrame({
    'Feature': model_sm.params.index,
    'Coefficient': model_sm.params.values,
    'P-value': model_sm.pvalues.values
    })

# Filter to keep only p-values greater than 0.05
    summary_df = summary_df[summary_df['P-value'] > 0.05]

# Sort the DataFrame by p-value in descending order
    summary_df = summary_df.sort_values(by='P-value', ascending=False)


# Print the sorted DataFrame
    # print("\nSorted Coefficients and P-values (from highest to lowest p-value):")
    # print(summary_df)
    return summary_df



# Ejecutar el pipeline
data = load_data("formula1_interlagos_df_final.csv", "Melbourne")
features = ['MaxSpeed', 'DriverSkill', 'Age', 'PitStopTime', 'ReactionTime',
                    'FinalPosition', 'Experience', 'DNF', 'Overtakes', 'TyreWear',
                    'CarPerformance', 'TrackFamiliarity', 'FuelConsumption', 'DownforceLevel',
                    'TrackTemperature', 'WeatherCondition_Mixed', 'WeatherCondition_Wet',
                    'TyreCompound_Medium', 'TyreCompound_Soft', 'TrackGrip_Low', 'TrackGrip_Medium']

target = 'FinalRaceTime'
features = select_features(data, target, features)
data = preprocess_data(data, features, target)
X, y = data[features], data[target]

summary_df = train_model(X, y)

while len(summary_df)>0:
    top_feature = str(summary_df.iloc[0]['Feature']) # Primer variable (con mayor p-valor)
    
    #print(top_feature[1:])
    
    del features[int(top_feature[1:])-1]
    #print(f"Variable {top_feature} eliminada de 'features'.")
    #print(f"Lista de variables restantes: {features}")
    
    features = select_features(data, target, features)
    data = preprocess_data(data, features, target)
    X, y = data[features], data[target]
    summary_df = train_model(X, y)
    
print(features)





def train_model2(X, y):
    
    # Split into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Scale the features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)


    # Create and train the model
    model = LinearRegression()
    model.fit(X_train_scaled, y_train)

    # Print the equation of the hyperplane
    coefficients = model.coef_
    intercept = model.intercept_

    #print("\nEquation of the hyperplane:")
    equation = f"FinalRaceTime = {intercept:.2f}"
    for feature, coef in zip(features, coefficients):
        equation += f" + ({coef:.2f} * {feature})"
    print(equation)

    # Calculate R-squared
    r_squared = model.score(X_test_scaled, y_test)
    
   
# Agregar constante para la intersección
    X_train_const = sm.add_constant(X_train_scaled)

# Ajustar el modelo de regresión con statsmodels
    model_sm = sm.OLS(y_train, X_train_const).fit()

# Mostrar los p-values de cada coeficiente
    print(model_sm.summary())


print(features)
data = data = pd.read_csv("formula1_interlagos_df_final.csv")
circuit_data = data[data['Circuit'] == "Melbourne"].copy()
X, y = circuit_data[features], circuit_data[target]
summary_df = train_model2(X, y)
