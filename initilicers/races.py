import csv
import random
import numpy as np
from datetime import datetime, timedelta

# Función para generar una fecha aleatoria entre 2010 y 2023
def random_date():
    start_date = datetime(2010, 1, 1)
    end_date = datetime(2023, 12, 31)
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    return start_date + timedelta(days=random_number_of_days)

# Listas de valores posibles
drivers = ["Hamilton", "Verstappen", "Leclerc", "Alonso", "Vettel", "Ricciardo", "Bottas", "Perez", "Sainz", "Norris"]
teams = ["Mercedes", "Red Bull", "Ferrari", "McLaren", "Aston Martin", "Alpine", "AlphaTauri", "Alfa Romeo", "Haas", "Williams"]
circuits = ["Monaco", "Silverstone", "Monza", "Spa", "Suzuka", "Melbourne", "Singapore", "Montreal", "Interlagos", "Abu Dhabi"]

# Generar datos
data = []
for _ in range(500):
    driver = random.choice(drivers)
    team = random.choice(teams)
    circuit = random.choice(circuits)
    
    # Edad del conductor (distribución normal)
    age = int(np.random.normal(28, 5))
    
    # Tiempo de pit stop (distribución normal)
    pit_stop_time = max(1.5, np.random.normal(3, 0.5))
    
    # Tiempo de reacción (distribución exponencial)
    reaction_time = np.random.exponential(0.2)
    
    # Posición final (distribución uniforme)
    final_position = random.randint(1, 20)
    
    # DNF (Did Not Finish) - distribución de Bernoulli
    dnf = np.random.binomial(1, 0.15)  # 15% de probabilidad de DNF
    
    # Puntos (basados en la posición final y DNF)
    points = 0 if dnf else max(0, 26 - final_position) if final_position <= 10 else 0
    
    # Velocidad máxima (distribución normal)
    max_speed = np.random.normal(330, 10)
    
    # Número de adelantamientos (distribución de Poisson)
    overtakes = np.random.poisson(5)
    
    # Fecha de la carrera
    race_date = random_date()
    
    data.append([
        race_date.strftime("%Y-%m-%d"),
        driver,
        age,
        team,
        circuit,
        round(pit_stop_time, 3),
        round(reaction_time, 3),
        final_position,
        dnf,
        points,
        round(max_speed, 1),
        overtakes
    ])

# Escribir en CSV
filename = './formula1/formula1_race_data.csv'
header = ['Date', 'Driver', 'Age', 'Team', 'Circuit', 'PitStopTime', 'ReactionTime', 'FinalPosition', 'DNF', 'Points', 'MaxSpeed', 'Overtakes']

with open(filename, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(header)
    writer.writerows(data)

print(f"CSV file '{filename}' has been generated with {len(data)} records.")

# Mostrar las primeras 5 líneas del archivo
print("\nPreview of the first 5 lines:")
with open(filename, 'r') as file:
    for i, line in enumerate(file):
        if i < 5:
            print(line.strip())
        else:
            break