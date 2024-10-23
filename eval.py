from pymongo import MongoClient
import pandas as pd

client = MongoClient('mongodb://localhost:27017/')
db = client['mydb']
collection = db['mycollection']

df = pd.read_csv('medical.csv')

collection.insert_many(df.to_dict('records'))

print("Data inserted into MongoDB successfully.")

df_mongo = pd.DataFrame(list(collection.find()))

print("DataFrame created")
print(df_mongo.head())

providers_in_ca = df[df['practicestate'] == 'CA']
print(providers_in_ca[:10])

ny_providers = df[(df['practicestate'] == 'NY') & (df['specialitieslist'] == 'Medical Supply Company Other') & (df['supplieslist'] == 'OXYGEN & EQUIPMENT')]
print(ny_providers)

for row in df.iterrows():
    if row[0] == '20506619':
        row[10] = '123123123'
        print(row)

supplylist = df.groupby(df['supplieslist'])
print(list(supplylist)[:10])
