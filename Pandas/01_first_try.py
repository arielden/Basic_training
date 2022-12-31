
import pandas as pd
dataset = pd.read_excel(r'Pandas\dataset.xlsx', header=0)  # This skips the first row, used as a header.
print(dataset.values)
