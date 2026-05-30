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

#Getting the highest and lowest transaction
max_transaction = sample_data['amount'].max()
max_merchant = sample_data[sample_data['amount'] == max_transaction]['merchant'].item()
min_transaction = sample_data['amount'].min()
min_merchant = sample_data[sample_data['amount'] == min_transaction]['merchant'].item()
#Printing out the row with the max transaction
print("The maximum transaction of {} is attributed to the merchant {}".format(max_transaction, max_merchant))
print("The minimum transaction of {} is attributed to the merchant {}".format(min_transaction, min_merchant))