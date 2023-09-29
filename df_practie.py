import pandas as pd

filename = "big-mac-full-index.csv"

df = pd.read_csv(filename)

# print(df.columns)# gives coulumn names to make a proper search
# print(df['dollar_price']) #gives dollar price on ever column labeled 'dollar_price
# print(df['name'])
query_text = f"(iso_a3 == 'ARG')"

df_arg = df.query(query_text)

# print(df_arg)

# df_arg.to_csv('argentina_report.csv')

print(df_arg['dollar_price'].median())
print(df_arg['dollar_price'].max())
print(df_arg['dollar_price'].min())
print(df_arg['dollar_price'].mean())



