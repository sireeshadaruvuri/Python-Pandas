import pandas as pd
f = pd.read_excel('c:\\Siri F1 assignments\\SEC 6050\\week3\\data_visualization.xlsx')
f.columns = ['Year', 'State', 'AvrgMax', 'AvrgMin', 'Season', 'Humiditityin%', 'UVIndex']
print(f)
# filter UVIndex values greater than 3
#to resolve error '>' not supported between instances of 'str' and 'int'
f['UVIndex'] = pd.to_numeric(f['UVIndex'], errors='coerce') #it converts string values to numeric
print(f[f.UVIndex > 3])#use f[f] to get numeric values else f.UVIndex >3 will return bool values true or false
f['AvrgMax'] = pd.to_numeric(f['AvrgMax'], errors='coerce')
print(f[f.AvrgMax > 70])
f['AvrgMin'] = pd.to_numeric(f['AvrgMin'],errors='coerce')
print(f[f.AvrgMin > 60])
c = f.AvrgMax * f.AvrgMin
print(c)
f['Multiply']=f.AvrgMax * f.AvrgMin
print(f)
#filtering two values at a time AvrgMax > 80 and AvrgMin > 60
#usually and operator can be used in R
#but in python & should be used
'''
f1 = f.AvrgMax > 80
f2 = f.AvrgMin > 60
f = f1 & f2
'''
#print(f[f])
print(f[(f.AvrgMax > 70) & (f.AvrgMin < 60)]) #& is a bitwise operator
#filter values that has UVIndex as zero
print(f)
print(f[f.UVIndex == 0])
print(f.Season.unique())
print(f[(f.Season == 'Summer') & (f.AvrgMax > 70)])
