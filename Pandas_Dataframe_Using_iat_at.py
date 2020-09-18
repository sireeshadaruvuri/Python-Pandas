import pandas as pd
f = pd.read_excel('c:\\Siri F1 assignments\\SEC 6050\\week3\\data_visualization.xlsx')
print(f)
print(f.head())
#.iat works with integer numbers
print(f.iat[2,2])
print(f.iat[1,5])
#.at works with strings
#f = f.reset_index()
#f.reset_index(inplace = True)
print(f.at[4,'Season'])
print(f.at[3,'Humiditityin%']) #.at looks for labels, it doesn't care about indexing .iat checks for index
#create a subset of 10
n = f[::10] #it prints every 10th record
print(n)
#n.reset_index(inplace = True)
print(n.iat[1,2])
print(n.at[10,'State']) #use n.reset_index function to reset the subset index then both will return the same values
#print(n.iat[])
