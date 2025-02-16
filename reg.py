import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import statsmodels.api as sm

data = pd.read_csv("formula1_interlagos_data_final.csv")

# Print column names
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

    # Select relevant features
# features = ['MaxSpeed','DriverSkill','Age','PitStopTime','ReactionTime',
#            'FinalPosition','Experience','DNF','Points',
#             'Overtakes','TyreWear','Experience','DriverSkill','CarPerformance',
#             'TrackFamiliarity','EngineMode','FuelConsumption','DownforceLevel','TrackTemperature',
#             'WeatherCondition_Mixed','WeatherCondition_Wet','TyreCompound_Medium','TyreCompound_Soft','TrackGrip_Low','TrackGrip_Medium']

# features = ['MaxSpeed','PitStopTime','ReactionTime',
#            'FinalPosition','Experience','DNF','Points',
#             'Overtakes','TyreWear','Experience','CarPerformance',
#             'DownforceLevel',
#             'WeatherCondition_Mixed','TyreCompound_Medium']

# features = ['MaxSpeed','PitStopTime','ReactionTime',
#            'FinalPosition','DNF','Points',
#             'Overtakes','TyreWear',
#             'DownforceLevel',
#             'TyreCompound_Medium']

features = ['MaxSpeed','ReactionTime',
           'FinalPosition','DNF','Points',
            'Overtakes','TyreWear',
            'DownforceLevel',
            'TyreCompound_Medium']

target = 'FinalRaceTime'

    # Check if columns exist and remove those that don't
features = [f for f in features if f in data.columns]
if target not in data.columns:
        raise ValueError(f"Target column '{target}' not found in the dataset")

print(f"\nUsing features: {features}")
print(f"Number of features : {len(features)}")
print(f"Target: {target}")

for feature in features:
        circuit_data[feature] = pd.to_numeric(circuit_data[feature], errors='coerce')
circuit_data = circuit_data.dropna(subset=features + [target])


    # Split the data for the selected driver (only Hamilton's data)
X = circuit_data[features]
y = circuit_data[target]


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

print("\nEquation of the hyperplane:")
equation = f"FinalRiceTime = {intercept:.2f}"
for feature, coef in zip(features, coefficients):
        equation += f" + ({coef:.2f} * {feature})"
print(equation)

    # Calculate R-squared
r_squared = model.score(X_test_scaled, y_test)
print(f"\nR-squared: {r_squared:.4f}")
    
   
# Agregar constante para la intersección
X_train_const = sm.add_constant(X_train_scaled)

# Ajustar el modelo de regresión con statsmodels
model_sm = sm.OLS(y_train, X_train_const).fit()

# Mostrar los p-values de cada coeficiente
print(model_sm.summary())

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
print("\nSorted Coefficients and P-values (from highest to lowest p-value):")
print(summary_df)




