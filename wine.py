

import numpy as np
import pandas as pd
import scipy.stats as st
import matplotlib.pyplot as plt

heart = pd.read_csv("winequality-red.csv")

cols = heart.columns[:-1]

fig, axs = plt.subplots(2, 4, figsize=(10, 6))
axs = axs.flatten()

for i, ax in enumerate(axs):
    col_name = cols[i]
    
    ax.hist(heart[col_name], bins=30, alpha=0.5, label=col_name)
    ax.set_title(f'Distribution for {col_name}')
    ax.legend()

for i in range(8, len(axs)):
    fig.delaxes(axs[i])

plt.tight_layout()
plt.show()