import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import glob
import re

# Load the data from states0.csv into a pandas DataFrame
data = pd.read_csv('states0.csv')

# Display the first few rows of the DataFrame to understand its structure
print(data.head())

# Extract the necessary columns: State, Income, and GenderPop
income_gender = data[['State', 'Income', 'GenderPop']]

# Display the first few rows of the extracted data
print(income_gender.head())

# Load the data from states1.csv into a pandas DataFrame
data1 = pd.read_csv('states1.csv')

# Extract the necessary columns: State, Income, and GenderPop
income_gender1 = data1[['State', 'Income', 'GenderPop']]

# Display the first few rows of the extracted data
print(income_gender1.head())

# Load the data from states2.csv into a pandas DataFrame
data2 = pd.read_csv('states2.csv')

# Extract the necessary columns: State, Income, and GenderPop
income_gender2 = data2[['State', 'Income', 'GenderPop']]

# Display the first few rows of the extracted data
print(income_gender2.head())

# Load the data from states3.csv into a pandas DataFrame
data3 = pd.read_csv('states3.csv')

# Extract the necessary columns: State, Income, and GenderPop
income_gender3 = data3[['State', 'Income', 'GenderPop']]

# Display the first few rows of the extracted data
print(income_gender3.head())

# Load the data from states4.csv into a pandas DataFrame
data4 = pd.read_csv('states4.csv')

# Extract the necessary columns: State, Income, and GenderPop
income_gender4 = data4[['State', 'Income', 'GenderPop']]

# Display the first few rows of the extracted data
print(income_gender4.head())

# Load the data from states5.csv into a pandas DataFrame
data5 = pd.read_csv('states5.csv')

# Extract the necessary columns: State, Income, and GenderPop
income_gender5 = data5[['State', 'Income', 'GenderPop']]

# Display the first few rows of the extracted data
print(income_gender5.head())

# Load the data from states6.csv into a pandas DataFrame
data6 = pd.read_csv('states6.csv')

# Extract the necessary columns: State, Income, and GenderPop
income_gender6 = data6[['State', 'Income', 'GenderPop']]

# Display the first few rows of the extracted data
print(income_gender6.head())

# Load the data from states7.csv into a pandas DataFrame
data7 = pd.read_csv('states7.csv')

# Extract the necessary columns: State, Income, and GenderPop
income_gender7 = data7[['State', 'Income', 'GenderPop']]

# Display the first few rows of the extracted data
print(income_gender7.head())

# Load the data from states8.csv into a pandas DataFrame
data8 = pd.read_csv('states8.csv')

# Extract the necessary columns: State, Income, and GenderPop
income_gender8 = data8[['State', 'Income', 'GenderPop']]

# Display the first few rows of the extracted data
print(income_gender8.head())

# Load the data from states9.csv into a pandas DataFrame
data9 = pd.read_csv('states9.csv')

# Extract the necessary columns: State, Income, and GenderPop
income_gender9 = data9[['State', 'Income', 'GenderPop']]

# Display the first few rows of the extracted data
print(income_gender9.head())

# Get a list of all census files available
census_files = glob.glob("states*.csv")

# Initialize an empty list to store individual DataFrames
dfs = []

# Loop through each file, load it into a DataFrame, and append it to the list
for file in census_files:
    df = pd.read_csv(file)
    dfs.append(df)

# Concatenate all DataFrames in the list into one DataFrame
us_census = pd.concat(dfs, ignore_index=True)

# Display the first few rows of the concatenated DataFrame
print(us_census.head())

# Display the columns and data types of the us_census DataFrame
print(us_census.columns)
print(us_census.dtypes)

# Display the first few rows of the us_census DataFrame
print(us_census.head())

# Remove dollar signs from the Income column using regex
us_census['Income'] = us_census['Income'].replace('[\$,]', '', regex=True)

# Display the updated Income column
print(us_census['Income'])

# Split the GenderPop column into separate columns for men and women
us_census[['Men', 'Women']] = us_census['GenderPop'].str.split('_', expand=True)

# Display the updated DataFrame with the new Men and Women columns
print(us_census.head())

# Remove 'M' and 'F' characters from Men and Women columns
us_census['Men'] = us_census['Men'].replace('[M]', '', regex=True)
us_census['Women'] = us_census['Women'].replace('[F]', '', regex=True)

# Convert Men and Women columns to numerical data types
us_census['Men'] = pd.to_numeric(us_census['Men'])
us_census['Women'] = pd.to_numeric(us_census['Women'])

# Display the updated DataFrame with numerical Men and Women columns
print(us_census.head())

# Create a scatterplot
plt.scatter(us_census['Women'], us_census['Income'])

# Add labels and title
plt.xlabel('Women Population')
plt.ylabel('Income')
plt.title('Income vs Women Population')

# Display the plot
plt.show()

# Print the Women column to check for NaN values
print("Women column before filling NaN values:\n", us_census['Women'])

# Fill NaN values in Women column using TotalPop - Men
us_census['Women'] = us_census['Women'].fillna(us_census['TotalPop'] - us_census['Men'])

# Print the Women column after filling NaN values
print("\nWomen column after filling NaN values:\n", us_census['Women'])

# Check for duplicate rows in the census DataFrame
duplicates = us_census.duplicated()

# Drop duplicate rows from the census DataFrame
us_census = us_census.drop_duplicates()

# Verify that duplicates have been dropped
print("Duplicate rows after dropping:\n", us_census[us_census.duplicated()])

# Scatterplot of proportion of women vs. average income
plt.scatter(us_census['Women'], us_census['Income'], color='blue', alpha=0.5)
plt.title('Proportion of Women vs. Average Income')
plt.xlabel('Proportion of Women')
plt.ylabel('Average Income')
plt.grid(True)
plt.show()

# Display the columns of the DataFrame
print(us_census.columns)

# Remove percentage signs and convert columns to numeric
us_census['Hispanic'] = us_census['Hispanic'].replace({'%':''}, regex=True).astype(float)
us_census['White'] = us_census['White'].replace({'%':''}, regex=True).astype(float)
us_census['Black'] = us_census['Black'].replace({'%':''}, regex=True).astype(float)
us_census['Native'] = us_census['Native'].replace({'%':''}, regex=True).astype(float)
us_census['Asian'] = us_census['Asian'].replace({'%':''}, regex=True).astype(float)
us_census['Pacific'] = us_census['Pacific'].replace({'%':''}, regex=True).astype(float)

# Fill NaN values with mean of respective column
us_census = us_census.fillna(value={
    'Hispanic': us_census['Hispanic'].mean(),
    'White': us_census['White'].mean(),
    'Black': us_census['Black'].mean(),
    'Native': us_census['Native'].mean(),
    'Asian': us_census['Asian'].mean(),
    'Pacific': us_census['Pacific'].mean()
})

# Check for duplicates
print("Duplicates:", us_census.duplicated().sum())

# Drop duplicates
us_census.drop_duplicates(inplace=True)

# Create histograms for each race category
plt.figure(figsize=(12, 8))

plt.subplot(2, 3, 1)
plt.hist(us_census['Hispanic'], bins=20, color='blue', alpha=0.7)
plt.title('Hispanic Population')

plt.subplot(2, 3, 2)
plt.hist(us_census['White'], bins=20, color='green', alpha=0.7)
plt.title('White Population')

plt.subplot(2, 3, 3)
plt.hist(us_census['Black'], bins=20, color='red', alpha=0.7)
plt.title('Black Population')

plt.subplot(2, 3, 4)
plt.hist(us_census['Native'], bins=20, color='orange', alpha=0.7)
plt.title('Native Population')

plt.subplot(2, 3, 5)
plt.hist(us_census['Asian'], bins=20, color='purple', alpha=0.7)
plt.title('Asian Population')

plt.subplot(2, 3, 6)
plt.hist(us_census['Pacific'], bins=20, color='brown', alpha=0.7)
plt.title('Pacific Population')

plt.tight_layout()
plt.show()

