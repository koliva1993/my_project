import pandas as pd
import numpy as np

msft=pd.read_csv("arduino.csv",index_col=0)
print(msft.head())

print(msft.dtypes)