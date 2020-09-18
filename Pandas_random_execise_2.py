import pandas as pd
import numpy as np
#How to create a series from a list, numpy array and dict?
l = ['a','b','c','d']
li = list('abcd') #both ways of creating list r same #list can be created with list keyword or square brackets
print('li series is', +pd.Series(li))
array = np.array([1,2,3,4,5])
mydict = {'a':1, 'b':2, 'c':3,'d':4}
#Create a pandas series from each of the items below: a list, numpy and a dictionary
print(pd.Series(l))
print(pd.Series(array))
print(pd.Series(mydict))
#---------------------
#How to convert the index of a series into a column of a dataframe?
c = pd.Series(l)
d = pd.DataFrame(c)
print('data frame is', +d)
myli = list('abcdefghijklmno')
arr = np.arange(0,15)
dicti = dict(zip(myli,arr))
#the zip() function takes iterables (can be zero or more), aggregates them in a tuple, and return it.
ser = pd.Series(dicti)
print(ser)
df = pd.DataFrame(ser)
print(df)
print(df.reset_index())
# using pandas to_frame()
df = ser.to_frame().reset_index()
print(df)
#---------------------------------
#How to combine many series to form a dataframe
list1 = list('abcdefgh')
array1 = np.arange(0,8)
dict1 = dict(zip(list1,array1))
series1 = pd.Series(dict1)
print('series1 is', +series1)
list2 = list('hgfdfiop')
array2 = np.arange(8)
dict2 = dict(zip(list2,array2))
series2 = pd.Series(dict2)
print('series2 is', +series2)
'''
datafr = pd.DataFrame(series1)
print(datafr)
datafr2 = pd.DataFrame(series2)
print(datafr2)
'''
dataframe = pd.DataFrame({'col1':series1,'col2':series2})
print(dataframe)
#they can be combined using concatenation function
df = pd.concat([series1,series2],axis = 1)
print(df)
#----------------------
#How to assign name to the series’ index?
#it can be done using rename method
ser = pd.Series(list('abcdef'))
ser.rename('alphabets')
print(ser)
ser.name = 'ser index'
print(ser)
#How to get the items of series A not present in series B?
se1 = pd.Series(list('abcdef'))
ser2 = pd.Series(list('kjhgfe'))
print(se1[se1.isin(ser2)]) #this is for common values present in ser2
#to get values not present ~ this symbol
print(se1[~se1.isin(ser2)])
#How to get the items not common to both series A and series B?
a = se1[~se1.isin(ser2)]
b = ser2[~se1.isin(ser2)]
#to combine a and b use append function
f = a.append(b, ignore_index=True) #here it is taking separate indexes for se1 and ser2, to get common indexes use ignore_index = true
print(f)
#in numpy above can be done using union and intersection
ser_u = pd.Series(np.union1d(se1, ser2))
print('union values r', +ser_u)
ser_i = pd.Series(np.intersect1d(se1, ser2))
print('intersection values are', +ser_i)
l = ser_u[~ser_u.isin(ser_i)]
print(l)
#How to get the minimum, 25th percentile, median, 75th, and max of a numeric series?
#take random values
state = np.random.RandomState(100)
print(state)
ser = pd.Series(state.normal(10, 5, 25))
print(ser)
#using decscribe function in pandas
print(ser.describe())
#in numpy
print(np.percentile(ser, q = [0, 25, 50, 75, 100]))
#How to get frequency counts of unique items of a series?
#Calculate the frequency counts of each unique value ser.
#it can be done using value_counts function
ser = pd.Series(np.take(list('abcdefgh'), np.random.randint(8, size=30)))
a= np.random.randint(8, size=30)
print('values in a r', +a)
print(ser)
print(ser.value_counts())
#How to keep only top 2 most frequent values as it is and replace everything else as ‘Other’?
v = pd.Series(np.random.randint(1,6,[20]))
print(v)
print(v.value_counts())
v[~v.isin(v.value_counts().index[:2])] = 'other'
print(v)
#how to bin a numeric series to 10 groups of equal size?
a = pd.Series(np.random.random(20))
print(a)
print(pd.qcut(a, q=10)) #using qcut function
#we can also pass labels
#print(pd.qcut(ser, q = [0, .10, .20, .30, .40, .50, .60, .70, .80, .90, 1], labels=['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th', '10th']))
#____________________________
#How to convert a numpy array to a dataframe of given shape? (L1)
