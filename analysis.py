# analysis.py
# Author: Kevin O'Leary
# Project analysing Fischer's Iris dataset

# First reading in the data set to VScode. also daved in folder

import pandas as pd # pandas will be used to manipulate the data
import numpy as np
import matplotlib.pyplot as plt

filename = "iris.data"
'''
df = pd.read_table(filename, sep=",") # check format was correct
print(df.head())
'''

pd.options.display.max_rows = 999 # 

dataset= pd.read_csv(filename, sep= ",", 
                       names=["Sepal Length", "Sepal Width", "Petal Length", "Petal Width", "Class"]) # adding headers to the dataframe 
#(https://www.geeksforgeeks.org/how-to-add-header-row-to-a-pandas-dataframe/)
dataset1 = dataset.set_index('Sepal Length') # remove the first empty column 
#https://datagy.io/pandas-drop-index-column/#:~:text=The%20most%20straightforward%20way%20to,a%20column%20in%20the%20DataFrame.

#print(dataset1.head())
#print(dataset.describe())

s_len = dataset["Sepal Length"]
avg_s_len = s_len.mean()
print(avg_s_len)

s_wid = dataset["Sepal Width"]
avg_s_wid = s_wid.mean()
print (avg_s_wid)

s_len_and_class = dataset[["Sepal Length", "Class"]]
print(s_len_and_class)

Class= dataset["Class"]

#plt.hist(s_len)
plt.plot(Class,s_len, color = 'r', marker ='D' )
plt.show()
plt.savefig("Sepal Lenght vs Class")

#from sklearn.datasets import load_iris
#data= load_iris()
    
#csv_url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

#data= pd.read_csv(csv_url)

#print(df.describe())