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
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    model = LinearRegression()
    model.fit(X_train_scaled, y_train)
    return model, X_train_scaled, X_test_scaled, y_train, y_test

def automated_backward_elimination(X, y):
    model = LinearRegression()
    sfs = SequentialFeatureSelector(model, direction='backward', n_features_to_select='auto')
    sfs.fit(X, y)
    selected_features = list(X.columns[sfs.get_support()])
    return selected_features

# Ejecutar el pipeline
data = load_data("formula1/formula1_interlagos_df_final.csv", "Interlagos")
initial_features = ['MaxSpeed', 'DriverSkill', 'Age', 'PitStopTime', 'ReactionTime',
                    'FinalPosition', 'Experience', 'DNF', 'Points', 'Overtakes', 'TyreWear',
                    'CarPerformance', 'TrackFamiliarity', 'FuelConsumption', 'DownforceLevel',
                    'TrackTemperature', 'WeatherCondition_Mixed', 'WeatherCondition_Wet',
                    'TyreCompound_Medium', 'TyreCompound_Soft', 'TrackGrip_Low', 'TrackGrip_Medium']

target = 'FinalRaceTime'
features = select_features(data, target, initial_features)
data = preprocess_data(data, features, target)
X, y = data[features], data[target]

model, X_train_scaled, X_test_scaled, y_train, y_test = train_model(X, y)
selected_features = automated_backward_elimination(pd.DataFrame(X_train_scaled, columns=features), y_train)
print(f"Final selected features: {selected_features}")
