import pandas as pd
#method1 to import data: specify full path
#for windows
stats = pd.read_excel('C:\\Siri F1 assignments\\Dinesh anna\\Journalist Deaths (1).xlsx')
print(stats)
#method2: using working directory
"""
import os
print(os.getcwd())
#change the work diectory so that u can access the complete folder instead of just file
os.chdir('c:\\Users\\arunk\\PycharmProjects')
print(os.getcwd())
stats2 = pd.read_excel('Journalist Deaths (1).xlsx')
print(stats2)
"""
#2. see the length of dataframe
print(len(stats))
#3. see the columns
print(stats.columns)
#4. to see no of columns
print(len(stats.columns))
#5. to see top rows
#head() gives top 5 rows
print(stats.head())
print(stats.head(6)) #it gives 6 rows
#6 . bottom rows
print(stats.tail())
print(stats.tail(6))
#7. to get information on the columns
print(stats.info())
#get stats on the columns
print(stats.describe())
#transpose function organizes rows n columns
print(stats.describe().transpose())
#rename columns
print(stats.columns)
#slicing in dataframes (to retrieve rows)
#by default it considers rows
print(stats[20:27])
print(stats[:10])
print(stats[1:])
print(stats[100:150])
print(stats[::-1]) #reverse the dataframe
print(stats[125:110:-1])
#to get 20th row
print(stats[::20])
#to extract columns we can give column name to dataset
print(stats['Year'])
#top 5 rows
print(stats['Year'].head())
#to extract two coulms
#print(stats['Year','Name'])
#make a list of year n name first like ['year','Name'] then pass this list into the dataframe
#we should give two square braces to extract multiple columns
print(stats[['Year','Name']]) #columns order can be interchangeble
print(stats[['Year','Name']].head())
#to quickly access one column
print(stats.Year.head(10))
#subsetting in pandas
#extract required rows n columns using above syntax
print(stats[10:15][['Year','Name']]) #subset of columns in rows #two subsets one after another
print(stats[['Year','Name']] [10:15])
print('extract two columns')
print(stats[['Year','Name']][15:25].head(5))
#mathematical operations
f = pd.read_excel('c:\\Siri F1 assignments\\SEC 6050\\week3\\data_visualization.xlsx')
print(len(f))
print(f.columns)
print(f[5:10])
print(f.head(5))
print(f.tail(6))
print(f.describe())
f.columns = ['Year','State','AvrgMax','AvrgMin','Season','Humiditityin%','UVIndex']
print(f.columns)
print(f['Year'])
print(f[['AvrgMax','AvrgMin']][1:6])
#AvrgMax = int(AvrgMax)
#AvrgMin = int(AvrgMin)
#r = f.AvrgMax * f.AvrgMin
#print(r)
#-----------------
#add a new column
f['new'] = [2,3,4,5,6,6,2,3,4,5,1,2,3,4,5,6,1,2,3,1,2,3]
print(f.head())
#delete column
print(f.drop('new',1)) #1 is position of column which is axis here
print(f.head()) #though we have deleted new column it is still present here
#it is just returning new object here, not actually deleting new column
#override it to delete it
f = f.drop('new',1)
print(f)
print(f.head())

