import pandas as pd
#method1 to import data: specify full path
#for windows
stats = pd.read_excel('C:\\Siri F1 assignments\\Dinesh anna\\Journalist Deaths (1).xlsx')
print(stats)
#method2: using working directory
import os
print(os.getcwd())
#change the work diectory so that u can access the complete folder instead of just file
os.chdir('C:\\Siri F1 assignments\\Dinesh anna')
print(os.getcwd())
stats2 = pd.read_excel('Journalist Deaths (1).xlsx')
print(stats2)