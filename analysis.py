# analysis.py
# Author: Kevin O'Leary
# Project analysing Fischer's Iris dataset

# First reading in the data set to VScode. also daved in folder

import pandas as pd # pandas will be used to manipulate the data
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


data_url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
col_headings = ['Sepal Length', 'Sepal Width', 'Petal Length', 'Petal Width', 'Class']
data= pd.read_csv(data_url, sep=",",  names = col_headings,)

with open('project.txt', 'w') as f: #creating the text file for outputs
    f.write("This is the text file where the outputs of my commands will be recorded \n\n")

#Initial look at the dataset
with open('project.txt', 'a') as f:
    f.write(" The below command confirms there are 150 samples with 5 pieces of information like we are expecting. \n")
    f.writelines(str(data.shape) + "\n\n")
    f.write('The below is the first 5 lines of the dataset:\n')
    f.writelines(str(data.head(5)) + "\n\n")
    f.write("The below is the last 5 lines of dataset:\n'")
    f.writelines(str(data.tail(5)) + "\n\n")

with open('project.txt', 'a') as f:  
    f.write("Below is a technical summary of the dataframe: \n\n")
    f.writelines(str(data.info) + "\n\n")
    f.write("Below is a statistical summary of each variable: \n\n")
    f.writelines(str(data.describe()) + "\n\n")


#univariate analysis 
#Histograms

sep_len = data["Sepal Length"]
sep_wit = data["Sepal Width"]
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
figure.suptitle('Multiclass Histogram', weight='bold')
plt.show()
plt.savefig('images/hist_iris.png')

#histograms that have been seperated by class

#Setosa Histogram
setosa = data[data["Class"] == "Iris-setosa"]
set_sl = setosa["Sepal Length"] #Setosa Sepal Lenght
set_sw = setosa["Sepal Width"] #Setosa Sepal width
set_pl = setosa["Petal Length"] #Petal Length
set_pw = setosa["Petal Width"] # Petal Width

figure, axs = plt.subplots(2, 2, figsize=(8, 8))

axs[0, 0].set_title("Sepal Length (cm)", weight='bold')
axs[0, 1].set_title("Sepal Width (cm)", weight='bold')
axs[1, 0].set_title("Petal Length (cm)", weight='bold')
axs[1, 1].set_title("Petal Width (cm)", weight='bold')

axs[0, 0].hist(set_sl, bins=9, edgecolor ='black')
axs[0, 1].hist(set_sw, bins=9, edgecolor ='black')
axs[1, 0].hist(set_pl, bins=9, edgecolor ='black')
axs[1, 1].hist(set_pw, bins=9, edgecolor ='black')
figure.suptitle('Setosa Histogram', weight='bold')
plt.show()
plt.savefig('images/Setosa_hist.png')

#Versicolor Histogram

versi = data[data["Class"] == "Iris-versicolor"]
ver_sl = versi["Sepal Length"] #Setosa Sepal Lenght
ver_sw = versi["Sepal Width"] #Setosa Sepal width
ver_pl = versi["Petal Length"] #Petal Length
ver_pw = versi["Petal Width"] # Petal Width

figure, axs = plt.subplots(2, 2, figsize=(8, 8))

axs[0, 0].set_title("Sepal Length (cm)", weight='bold')
axs[0, 1].set_title("Sepal Width (cm)", weight='bold')
axs[1, 0].set_title("Petal Length (cm)", weight='bold')
axs[1, 1].set_title("Petal Width (cm)", weight='bold')

axs[0, 0].hist(ver_sl, bins=7, edgecolor ='black')
axs[0, 1].hist(ver_sw, bins=7, edgecolor ='black')
axs[1, 0].hist(ver_pl, bins=7, edgecolor ='black')
axs[1, 1].hist(ver_pw, bins=7, edgecolor ='black')
figure.suptitle('Versicolor Histogram', weight='bold')
plt.show()
plt.savefig('images/Versicolor_hist.png')

#Virginica Histogram
virgin = data[data["Class"] == "Iris-virginica"]
vg_sl = virgin["Sepal Length"] #Setosa Sepal Lenght
vg_sw = virgin["Sepal Width"] #Setosa Sepal width
vg_pl = virgin["Petal Length"] #Petal Length
vg_pw = virgin["Petal Width"] # Petal Width

figure, axs = plt.subplots(2, 2, figsize=(8, 8))

axs[0, 0].set_title("Sepal Length (cm)", weight='bold')
axs[0, 1].set_title("Sepal Width (cm)", weight='bold')
axs[1, 0].set_title("Petal Length (cm)", weight='bold')
axs[1, 1].set_title("Petal Width (cm)", weight='bold')

axs[0, 0].hist(vg_sl, bins=7, edgecolor ='black')
axs[0, 1].hist(vg_sw, bins=7, edgecolor ='black')
axs[1, 0].hist(vg_pl, bins=7, edgecolor ='black')
axs[1, 1].hist(vg_pw, bins=7, edgecolor ='black')
figure.suptitle('Virginica Histogram', weight='bold')
plt.show()
plt.savefig('images/Virginica_hist.png')

#Boxplots

figure, ax = plt.subplots(2, 2, figsize=(8, 8))

sns.boxplot(x =data['Class'], y= data['Sepal Length'], ax=ax[0,0]); #Boxplot for Sepal Length
ax[0, 0].set_title("Sepal Length (cm)", weight='bold' )
ax[0, 0].set_xlabel("Class of Iris", weight='bold')

sns.boxplot(x =data['Class'], y= data['Sepal Width'], ax=ax[0,1]); #Boxplot for Sepal Width
ax[0, 1].set_title("Sepal Width (cm)", weight='bold')
ax[0, 1].set_xlabel("Class of Iris", weight='bold')

sns.boxplot(x =data['Class'], y= data['Petal Length'], ax=ax[1,0]); #Boxplot for Petal Length
ax[1, 0].set_title("Petal Length (cm)", weight='bold')
ax[1, 0].set_xlabel("Class of Iris", weight='bold')

sns.boxplot(x =data['Class'], y= data['Petal Width'], ax=ax[1,1]); #Boxplot for Petal Width
ax[1, 1].set_title("Petal Width (cm)", weight='bold')
ax[1, 1].set_xlabel("Class of Iris", weight='bold')

figure.subplots_adjust(hspace=.5)
figure.suptitle('Boxplots of Sepal and Petal Dimensions by Class', weight='bold')
plt.show()
plt.savefig('images/Boxplots.png')

#sepal_scatter = data[['Sepal Length', 'Sepal Width', 'Class']]
iris_s = data[data['Class'] == 'Iris-setosa']
iris_ver = data[data['Class'] == 'Iris-versicolor']
iris_vir = data[data['Class'] == 'Iris-virginica']

ax = iris_s.plot(x= 'Sepal Length', y ='Sepal Width', kind= 'scatter', c ='green', s=30, label= 'Iris-setosa')
iris_ver.plot(x= 'Sepal Length', y ='Sepal Width', kind= 'scatter', ax= ax, c ='red', s=30, label= 'Iris-versicolor')
iris_vir.plot(x= 'Sepal Length', y ='Sepal Width', kind= 'scatter', ax= ax, c ='blue', s=30, label= 'Iris-virginica ')
plt.title('Sepal Length vs Width', weight='bold')
plt.xlabel('Sepal Length (cm)', weight='bold')
plt.show()
plt.savefig('images/sepal_scatter.png')

ax = iris_s.plot(x= 'Petal Length', y ='Petal Width', kind= 'scatter', c ='green', s=30, label= 'Iris-setosa')
iris_ver.plot(x= 'Petal Length', y ='Petal Width', kind= 'scatter', ax= ax, c ='red', s=30, label= 'Iris-versicolor')
iris_vir.plot(x= 'Petal Length', y ='Petal Width', kind= 'scatter', ax= ax, c ='blue', s=30, label= 'Iris-virginica ')
plt.title('Petal Length vs Width', weight='bold')
plt.xlabel('Petal Length (cm)', weight='bold')
plt.show()
plt.savefig('images/petal_scatter.png')


#sns.scatterplot(x='Sepal Length', y='Sepal Width', hue= 'class')
#plt.show()
#ax= data.plot.scatter(x="Sepal Length", y= "Sepal Width", colour =)
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



'''