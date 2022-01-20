import pandas as pd
import numpy as np
from matplotlib.colors import ListedColormap
import os
def prepare_data(df):
  X = df.drop("y", axis=1)

  y = df["y"]

  return X, y