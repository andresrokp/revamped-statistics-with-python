#  %%

from scipy import stats
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

tips_data = sns.load_dataset("tips")

# %%

sns.boxplot(x=tips_data["tip"], y=tips_data["time"])

sns.FacetGrid(data=tips_data, row="time").map(plt.hist, "tip")


# %%
