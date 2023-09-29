import csv
import pandas as pd
# pd.read_csv('./big-mac-full-index.csv')
df = pd.read_csv('./big-mac-full-index.csv')
# lower = df.lower() 

def get_big_mac_price_by_year(year,country_code):

    query = f"(date >= '{year}-01-01'and date <= '{year}-12-31' and iso_a3 == '{country_code.upper()}')"
    df_result = df.query(query)
    mean_dollar_price = (round(df_result['dollar_price'].mean(),2))
   
    return mean_dollar_price
 
def get_big_mac_price_by_country(country_code):
     
     query = f"(iso_a3 == '{country_code.upper()}')"
     df_result = df.query(query)
     mean_dollar_price = (round(df_result['dollar_price'].mean(),2))
     
     return mean_dollar_price


def get_the_cheapest_big_mac_price_by_year(year):
    # name_query = f"('name')"
    query = f"(date >= '{year}-01-01' and date <= '{year}-12-31')"
    year_query = df.query(query)
    index_of_min_value = year_query['dollar_price'].idxmin()
    cheapest = round(year_query.loc[index_of_min_value]['dollar_price'],2)
    row = year_query.loc[index_of_min_value]
    iso_a3 = row['iso_a3']
    # rows = year_query.loc[index_of_min_value]
    name = row['name']
    # cheap_with_name = f"the output for {year} will be: {name}({iso_a3}): ${cheapest}"
    cheap_with_name = f"{name}({iso_a3}): ${cheapest}"


    return cheap_with_name
    

def get_the_most_expensive_big_mac_price_by_year(year):
    query = f"(date >= '{year}-01-01' and date <= '{year}-12-31')"
    year_query = df.query(query)
    index_of_max_value = year_query['dollar_price'].idxmax()
    expensive = round(year_query.loc[index_of_max_value]['dollar_price'],2)
    row = year_query.loc[index_of_max_value]
    iso_a3 = row['iso_a3']
    # rows = year_query.loc[index_of_min_value]
    name = row['name']
    # most_with_name = f"the output for {year} will be: {name}({iso_a3}): ${expensive}"
    most_with_name = f"{name}({iso_a3}): ${expensive}"

    return most_with_name

if __name__ == "__main__":
    result_a = get_big_mac_price_by_year(2010,"arg")
    print(result_a)
    result_b = get_big_mac_price_by_country("mex")
    print(result_b)
    result_c = get_the_cheapest_big_mac_price_by_year(2011)
    print(result_c)
    result_d = get_the_most_expensive_big_mac_price_by_year(2008)
    print(result_d)