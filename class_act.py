import pandas as pd

df = pd.read_csv("big-mac-full-index.csv")
# the row that has the minimum value of bigmac

index_of_min_value = df['dollar_price'].idxmin()

print(index_of_min_value)

# print(df.loc[index_of_min_value]) #returns a series, returns date,country,and min price in data 

# print(df['dollar_price'].min()) #returns the cheapest big mac, but not country or date etc. 





#query from 2000-01-01 and end 2000-12-31
year = '2000'
country_code = "ARG"
new_query = f"(date >= '{year}-01-01' and date <= '{year}-12-31' and iso_a3 == '{country_code}')"

# new_query = f"(date >= '2000-01-01' and date <= '2000-12-31')"

df_by_date =df.query(new_query)
# print(df_by_date)

# ---------------------------------------------------------------------------------

query = f"(iso_a3 =='NZL' or iso_a3 =='DNK')" #OR returns both. AND returns if both exist aat same time(theydont)

df_result = df.query(query)

mean_dollar_price = df_result['dollar_price'].mean()

mean_dollar_price_two_deciamls = round(mean_dollar_price,2)

# print(mean_dollar_price)
# print(mean_dollar_price_two_deciamls)

# print(df_result.min())
# print(df_result['dollar_price'].min())
# print(df_result['dollar_price'].max())
# print(round(df_result['dollar_price'].mean()),3)
# print(df_result['dollar_price'].median())

