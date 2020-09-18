import pandas as pd
stats = pd.read_csv('C:\Siri F1 assignments\data science training\pandas exercise\Automobile_data.csv')
print(stats)
#1. From given data set print first and last five rows
print(stats.head())
print(stats.tail())
#2. Clean data and update the CSV file
stats = pd.read_csv('C:\Siri F1 assignments\data science training\pandas exercise\Automobile_data.csv',na_values = \
    {'price':["?","n.a"],'stroke':['?','n.a'],'horsepower':["?","n.a"],'peak-rpm':["?","n.a"],'average-mileage':["?","n.a"]})
print(stats[22:24])
#b = stats.to_csv('C:\Siri F1 assignments\data science training\pandas exercise\Automobile_data.csv')
#print(b)
#Find the most expensive car company name
print(stats[['company','price']][stats.price == stats['price'].max()])
#print(stats['price'].max())
print(stats[stats.price == stats['price'].max()])
print(stats[['company','price']][stats.price == stats['price'].max()])
#Print All Toyota Cars details
#print(stats.head())
print(stats[stats.company == 'toyota'])
#Count total cars per company
print(stats['company'].value_counts()) #value_counts() counts for each value
#Find each company’s Higesht price car
#print(stats[['company']][stats['price'].max()])
a = stats.groupby('company')
print(a[['company','price']].max())
#Find the average mileage of each car making company
print(stats.info())
print(stats.describe())
print(stats[['company','average-mileage']])
a = stats.groupby('company')
print(a[['company','average-mileage']].mean())
#Sort all cars by Price column
print(stats.sort_values(by=['price','horsepower'],ascending=False))
#Concatenate two data frames using the following conditions
GermanCars = {'Company': ['Ford', 'Mercedes', 'BMV', 'Audi'], 'Price': [23845, 171995, 135925 , 71400]}
japaneseCars = {'Company': ['Toyota', 'Honda', 'Nissan', 'Mitsubishi '], 'Price': [29995, 23600, 61500 , 58900]}
b = pd.DataFrame.from_dict(GermanCars) #DataFrame.from_dict converts dictionary into dataframe
print(b)
c = pd.DataFrame.from_dict(japaneseCars)
print(c)
print(pd.concat([b,c], keys=['Germany', 'Japan']))
#Merge two data frames using the following condition
Car_Price = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'Price': [23845, 17995, 135925 , 71400]}
car_Horsepower = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'horsepower': [141, 80, 182 , 160]}
a = pd.DataFrame.from_dict(Car_Price)
print(a)
b = pd.DataFrame.from_dict(car_Horsepower)
print(b)
print(pd.merge(a,b,on='Company'))