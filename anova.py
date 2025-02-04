import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm

# Load the data
data = pd.read_csv("formula1/formula1_enhanced_data_final.csv")

# Prepare the data for ANOVA
# We'll use 'Team' as the independent variable and 'ReactionTime' as the dependent variable
data['ReactionTime'] = pd.to_numeric(data['ReactionTime'], errors='coerce')
data = data.dropna(subset=['Team', 'ReactionTime'])

# Perform one-way ANOVA
model = ols('ReactionTime ~ C(Team)', data=data).fit()
anova_table = anova_lm(model, typ=2)

print("One-way ANOVA results:")
print(anova_table)

# Calculate mean reaction times for each team
team_means = data.groupby('Team')['ReactionTime'].mean().sort_values()

# Visualize the results
plt.figure(figsize=(12, 6))
sns.boxplot(x='Team', y='ReactionTime', data=data)
plt.title('Reaction Time by Team')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Post-hoc test (Tukey's HSD)
from statsmodels.stats.multicomp import pairwise_tukeyhsd
tukey_results = pairwise_tukeyhsd(data['ReactionTime'], data['Team'])

print("\nTukey's HSD Test results:")
print(tukey_results)

# Visualize Tukey's test results
plt.figure(figsize=(12, 8))
tukey_results.plot_simultaneous()
plt.title("Tukey's HSD Test for Team Differences in Reaction Time")
plt.tight_layout()
plt.show()

print("\nTop 5 teams with fastest mean reaction times:")
print(team_means.head())

print("\nBottom 5 teams with slowest mean reaction times:")
print(team_means.tail())