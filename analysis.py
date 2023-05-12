# analysis.py
# Author: Kevin O'Leary
# Project analysing Fischer's Iris dataset

# First reading in the data set to VScode. also daved in folder

import pandas as pd # pandas will be used to manipulate the data
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statistics as stat



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
plt.savefig('images/hist_iris.png')
plt.show()

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
plt.savefig('images/Class Specific Histograms/Setosa_hist.png')
plt.show()


#Versicolor Histogram

versi = data[data["Class"] == "Iris-versicolor"]
ver_sl = versi["Sepal Length"] # Sepal Lenght
ver_sw = versi["Sepal Width"] # Sepal width
ver_pl = versi["Petal Length"] # Petal Length
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
plt.savefig('images/Class Specific Histograms/Versicolor_hist.png')
plt.show()

#Virginica Histogram
virg = data[data["Class"] == "Iris-virginica"]
vg_sl = virg["Sepal Length"] # Sepal Lenght
vg_sw = virg["Sepal Width"] # Sepal width
vg_pl = virg["Petal Length"] # Petal Length
vg_pw = virg["Petal Width"] # Petal Width

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
plt.savefig('images/Class Specific Histograms/Virginica_hist.png')
plt.show()

#Printing averages to txt.file

set_s_l_avg = (stat.mean(set_sl))   #setosa sep length average
set_s_w_avg = (stat.mean(set_sw))   #setosa sep width average
set_p_l_avg = (stat.mean(set_pl))   #setosa pet length average
set_p_l_avg = (stat.mean(set_pw))    #setosa pet width average

ver_s_l_avg = (stat.mean(ver_sl))   #versicolor sep length average
ver_s_w_avg = (stat.mean(ver_sw))   #versicolor sep width average
ver_p_l_avg = (stat.mean(ver_pl))   #versicolor pet length average
ver_p_w_avg = (stat.mean(ver_pw))   #versicolor pet width average

virg_s_l_avg = (stat.mean(vg_sl))   #virginica sep length average
virg_s_w_avg = (stat.mean(vg_sw))   #virginica sep width average
virg_p_l_avg = (stat.mean(vg_pl))   #virginica pet length average
virg_p_w_avg = (stat.mean(vg_pw))    #virginica pet width average


with open('project.txt', 'a') as f:  
    f.write(f'The average Sepal length of the Setosa iris is  {set_s_l_avg}cm\n')
    f.write(f'The average Sepal width of the Setosa iris is {set_s_w_avg}cm\n')
    f.write(f'The average Petal length of the Setosa iris is {set_p_l_avg}cm\n')
    f.write(f'The average Petal width of the Setosa iris is {set_p_l_avg}cm\n\n')
    f.write(f'The average Sepal length of the Versicolor iris is  {ver_s_l_avg}cm\n')
    f.write(f'The average Sepal width of the Versicolor iris is {ver_s_w_avg}cm\n')
    f.write(f'The average Petal length of the Versicolor iris is {ver_p_l_avg}cm\n')
    f.write(f'The average Petal width of the Versicolor iris is {ver_p_w_avg}cm\n\n')
    f.write(f'The average Sepal length of the Virginica iris is  {virg_s_l_avg}cm\n')
    f.write(f'The average Sepal width of the Virginica iris is {virg_s_w_avg}cm\n')
    f.write(f'The average Petal length of the Virginica iris is {virg_p_l_avg}cm\n')
    f.write(f'The average Petal width of the Virginica iris is {virg_p_l_avg}cm\n\n')


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
plt.savefig('images/Boxplots.png')
plt.show()

#Multivariate Analysis 
#Scatter plots

ax = setosa.plot(x= 'Sepal Length', y ='Sepal Width', kind= 'scatter', c ='green', s=30, label= 'Iris-setosa')
versi.plot(x= 'Sepal Length', y ='Sepal Width', kind= 'scatter', ax= ax, c ='red', s=30, label= 'Iris-versicolor')
virg.plot(x= 'Sepal Length', y ='Sepal Width', kind= 'scatter', ax= ax, c ='blue', s=30, label= 'Iris-virginica ')
plt.title('Sepal Length vs Width', weight='bold')
plt.ylabel('Sepal Width (cm)', weight='bold')
plt.xlabel('Sepal Length (cm)', weight='bold')
plt.savefig('images/sepal_scatter.png')
plt.show()

ax = setosa.plot(x= 'Petal Length', y ='Petal Width', kind= 'scatter', c ='green', s=30, label= 'Iris-setosa')
versi.plot(x= 'Petal Length', y ='Petal Width', kind= 'scatter', ax= ax, c ='red', s=30, label= 'Iris-versicolor')
virg.plot(x= 'Petal Length', y ='Petal Width', kind= 'scatter', ax= ax, c ='blue', s=30, label= 'Iris-virginica ')
plt.title('Petal Length vs Width', weight='bold')
plt.ylabel('Petal Width (cm)', weight='bold')
plt.xlabel('Petal Length (cm)', weight='bold')
plt.savefig('images/petal_scatter.png')
plt.show()


# Pairplots comparing each variable to all others. 

pair = sns.pairplot(data, hue ='Class')
pair.map_diag(sns.histplot)
pair.map_offdiag(sns.scatterplot)
plt.savefig('images/Pairplot.png')
plt.show