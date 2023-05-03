# analysis.py
# Author: Kevin O'Leary
# Project analysing Fischer's Iris dataset

# First reading in the data set to VScode. also daved in folder

import pandas as pd # pandas will be used to manipulate the data
import numpy as np
import matplotlib.pyplot as plt


# dataset can be either saved locally or read in directly from the url 

data_url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
col_headings = ['Sepal Length', 'Sepal Width', 'Petal Length', 'Petal Width', 'Class']
data= pd.read_csv(data_url, sep=",",  names = col_headings)
#data = data.set_index('Sepal Length')

# here is the second method of reading in the data set
'''
filename = "iris.data"
data = pd.read_csv(filename, sep="," names =col_headings) # check format was correct
'''

'''
#Initial look at the dataset

print(data.head(10))
print(data.tail(10))
print(data.info()) # a techincal summary of the dataframe
print(data.shape) # confimrs there are 150 samples with 5 pieces of informaiton
print(data.describe())

'''
#sep_len = data["Sepal Length"]
#sep_wid = data["Sepal Width"]
#print(sep_len.head())
#print(sep_wid.head())

#create histogram for Sepal length, wideth and petal lenght width. 

#in order select for a subset of data. In this case all setosa classes

setosa = data[data["Class"] == "Iris-setosa"]
veriscolour = data[data["Class"] == "Iris-versicolor"]
virginica = data[data["Class"] == "Iris-virginica"]

print(setosa.describe())
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

#print(df.describe())

'''