import pandas as pd

#First, the data will be loaded into a pandas dataframe
sample_data = pd.read_csv("startingData.csv")

#Getting exploratory data
#Getting the number of transactions - the number of total rows
rows = len(sample_data)
print(sample_data)
print("The number of transactions is {}".format(rows))
#Calculating the total amount spent in these transactions
total_expense = round(sample_data['amount'].sum(), 2)
print("Across {} expenses, the individual spent {}".format(rows, total_expense))