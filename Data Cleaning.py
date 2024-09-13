import pandas as pd

df = pd.read_csv('data.csv', encoding='ISO-8859-1')
print(df.head())


df = df.drop_duplicates()

print(df.isnull().sum())

df = df.dropna(subset=['CustomerID'])
df['Description'] = df['Description'].fillna('No Desscription')

df['InvoiceNo'] = df['InvoiceNo'].astype(str)
df['StockCode'] = df['StockCode'].astype(str)
df['Description'] = df['Description'].astype(str)
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'], errors='coerce')
df['CustomerID'] = pd.to_numeric(df['CustomerID'], errors='coerce')
df['CustomerID'] = df['CustomerID'].astype('Int64')
df['Country'] = df['Country'].astype(str)


print(df.dtypes)

df.to_csv('cleaned_data.csv', index=False)