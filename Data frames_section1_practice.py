import pandas as pd
a = pd.read_excel('c:\\Siri F1 assignments\\SEC 6050\\week3\\data_visualization.xlsx')
print(a)
import os
print(os.getcwd())
os.chdir('c:\\Siri F1 assignments\\SEC 6050\\week3')
print(os.getcwd())
b = pd.read_excel('data_visualization.xlsx')
print(b)
print(len(a))
print(len(a.columns))
print(a.head(7))
print(a.tail(6))
print(a.info())
print("describe function")
print(a.describe().transpose())
#rename columns
print(a.columns)
a.columns = ['a','b','c','as','ad','ah','ug']
print(a.columns)