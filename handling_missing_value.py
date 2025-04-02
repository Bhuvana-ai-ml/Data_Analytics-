import pandas as pd
df = pd.read_csv(r"C:\Users\Bhuvana P\Downloads\winequality-red.csv")
# why r? cause in python '\' means escape character.so, we use r to avoid misinterpret
df.head