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

#Calculating the average expense per merchant
avg_per_airline = round(sample_data[['merchant', 'amount']].groupby('merchant')['amount'].mean(), 2)
avg_per_airline = avg_per_airline.reset_index()
avg_per_airline = avg_per_airline.sort_values(by=['merchant', 'amount'], ascending=[False, True])
print(avg_per_airline)