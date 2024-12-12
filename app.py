print("Hello World")
import pandas as pd
data_frame = pd.read_csv(".learn/assets/pokemon_data.csv")
print(data_frame)
# Series
s = pd.Series([23,45,7,34,6,63,36,78,54,34])
print(s)
# Data Range
dr = pd.date_range("2021-05-01","2021-05-12")
print(dr)
# Series Apply
my_series = pd.Series([2, 4, 6, 8, 10])
def divide(input):
    return input/2
divided = my_series.apply(divide)
print(divided)
# DataFrames
data =  [["Toyota", "Corolla", "Blue"], ["Ford", "K", "Yellow"], ["Porsche", "Cayenne", "White"]]
df = pd.DataFrame(data, columns=['Brand', 'Model', 'Color'])
print(df)
# DataFrame Dict
data = [
    { 
        "brand": "Toyota", 
        "model": "Corolla",
        "color": "Blue"
    },
    {
        "brand": "Ford", 
        "model": "K",
        "color": "Yellow"
    },
    {
        "brand": "Porsche", 
        "model": "Cayenne",
        "color": "White"
    }
]
df = pd.DataFrame(data)
df.loc[len(df)] = ["Tesla", "Model S", "Red"] # añade una fila al dataframe
print(df)
# DataFrame iLoc
df_pokemon = pd.read_csv(".learn/assets/pokemon_data.csv")
print(df_pokemon.iloc[133,6])
# DataFrame Head
print(df_pokemon.head(3))
# DataFrame Tail
print(df_pokemon.tail(3))
# Print Columns
print(df_pokemon[["Name", "Type 1"]].head(10))
# Loc Function
print(df_pokemon.loc[df_pokemon['Attack'] > 80])
# Filter and Count
print(len(df_pokemon.loc[df_pokemon['Legendary'] == True]))
# Clean Datasets
df_names = pd.read_csv(".learn/assets/us_baby_names_right.csv")
print(df_names.head(5))
# Remove Column
df_names.drop('Unnamed: 0', axis=1, inplace=True) # axis=1 columns, inplace=True, el DataFrame se modifica directamente y no necesitas asignar el resultado de drop a df_names nuevamente
print(df_names.head(5))
# Value Counts
print(df_names.value_counts('Gender'))
# Group By
result = df_names.groupby('Name').sum()
print(len(result))