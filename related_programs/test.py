import pandas as pd
import numpy as np

df = pd.read_csv('fort99', sep = '\s+')
print(df.index)
print(df.columns)
