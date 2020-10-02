import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats


global_temp_df = pd.read_csv('global_temp_co2_nasa.csv', skipinitialspace=True)
gt_df = global_temp_df.replace('', np.nan)
print(gt_df)
print(gt_df.dtypes)