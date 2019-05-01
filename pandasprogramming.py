import pandas as pd

excel_file = "Momentum Cohort Analysis Jan 1-7 (1).xlsx"

cohort = pd.read_excel(excel_file, sheet_name = 0, index_col = 3)
excel_file = "Subscriptions0726.xlsx"

cohort2 = pd.read_excel(excel_file, sheet_name = 0, index_col = 2)

cohort2_subset_columns = pd.read_excel(excel_file, usecols = [2,17,20])

print(cohort2_subset_columns.head())
print(cohort.head())
