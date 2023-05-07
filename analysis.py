# analysis.py
# Author: Kevin O'Leary
# Project analysing Fischer's Iris dataset

# First reading in the data set to VScode. also daved in folder

import pandas as pd # pandas will be used to manipulate the data
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


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

#uninvariate analysis looks at one variable of a data set. i will do this for each 
#of sepal length, sepal width, petal length and petal width for histogrmas and boxplots

sep_len = data["Sepal Length"]
#plt.hist(sep_len)
#plt.show()
sep_wit = data["Sepal Width"]
#plt.hist(sep_wit)
#plt.show()
pet_len= data["Petal Length"]
pet_wit = data["Petal Width"]

figure, axs = plt.subplots(2, 2, figsize=(8, 8))

axs[0, 0].set_title("Sepal Length (cm)", weight='bold')
axs[0, 1].set_title("Sepal Width (cm)", weight='bold')
axs[1, 0].set_title("Petal Length (cm)", weight='bold')
axs[1, 1].set_title("Petal Width (cm)", weight='bold')

axs[0, 0].hist(sep_len, bins=9, edgecolor ='black')
axs[0, 1].hist(sep_wit, bins=9, edgecolor ='black')
axs[1, 0].hist(pet_len, bins=9, edgecolor ='black')
axs[1, 1].hist(pet_wit, bins=9, edgecolor ='black')
#plt.show()
plt.savefig('graphs/hist_iris.png')


#uninvariate analysis looks at one variable of a data set. i will do this for each 
# of sepal length, sepal width, petal length and petal width


#in order select for a subset of data. In this case all setosa classes

#setosa = data[data["Class"] == "Iris-setosa"]
#veriscolour = data[data["Class"] == "Iris-versicolor"]
#virginica = data[data["Class"] == "Iris-virginica"]

print(data.groupby('Class').agg([np.mean, np.median])) #np.mean and np.medians are functions wihtin numPy.

figure, ax = plt.subplots(2, 2, figsize=(8, 8))

sns.boxplot(x =data['Class'], y= data['Sepal Length'], ax=ax[0,0]);
ax[0, 0].set_title("Sepal Length (cm)", weight='bold' )
ax[0, 0].set_xlabel("Class of Iris", weight='bold')
sns.boxplot(x =data['Class'], y= data['Sepal Width'], ax=ax[0,1]);
ax[0, 1].set_title("Sepal Width (cm)", weight='bold')
ax[0, 1].set_xlabel("Class of Iris", weight='bold')
sns.boxplot(x =data['Class'], y= data['Petal Length'], ax=ax[1,0]);
ax[1, 0].set_title("Petal Length (cm)", weight='bold')
ax[1, 0].set_xlabel("Class of Iris", weight='bold')
sns.boxplot(x =data['Class'], y= data['Petal Width'], ax=ax[1,1]);
ax[1, 1].set_title("Petal Width (cm)", weight='bold')
ax[1, 1].set_xlabel("Class of Iris", weight='bold')
figure.subplots_adjust(hspace=.5)
figure.suptitle('Boxplots of Sepal and Petal Dimensions by Class', weight='bold')
#plt.show()
plt.savefig('graphs/Boxplots.png')


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