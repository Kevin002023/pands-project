# **Programming and Scripting Project**

## **Table of Contents**

1. Introduction to Dataset
2. Project Outline
3. Software Used


## **Introduction to Dataset**

The Fischers Iris dataset was made by famous by statistician Ronald Fischer when he used it in his 1936 paper ("The use of multiple measurements in taxonomic problems")[https://onlinelibrary.wiley.com/doi/10.1111/j.1469-1809.1936.tb02137.x]. However it was actually compiled before this by Edgar Anderson, a botanist who was examining the variation within the Iris flower. 

The 1936 paper was proposing 'Fishers linear discriminant' which today is known as linear discrimanent analysis. This is a (method)[https://www.geeksforgeeks.org/ml-linear-discriminant-analysis/] used in statistics to find a combination of features that can best seperate the data into distinct classes.

The dataset is hosted on the (UCI Machine Learning Repository)[https://archive.ics.uci.edu/ml/datasets/iris]. It consists of 3 classes of iris; 

![Iris-setosa](images\Setosa.jpg "Iris Setosa")
![Iris-veriscolor](images\Veriscolor.jpg "Iris Veriscolor")
![Iris-virginica](images\Virginica.jpg "Iris Virginica")

It is a multivariate dataset containing information on 150 specimens of iris. There are 5 attributes recorded for each specimen. (These are as follows:)[https://archive.ics.uci.edu/ml/datasets/iris]

1. sepal length in cm
2. sepal width in cm
3. petal length in cm
4. petal width in cm
5. class:
-- Iris Setosa
-- Iris Versicolour
-- Iris Virginica

Fischer used this information to identify a method of distinguishing between the classes of iris's. It has since been used as a benchmark dataset for machine learning algorithims.

## **Project Outline**

The purpose of the project was to research the Iris dataset, import it to python and write a program called analysis.py that


## **Software Used**

This project was done using python on Visual Studio Code. It was used to produce both the code and this README.md file.

The dataset is availble from the machine learning repository of UCI(http://archive.ics.uci.edu/ml/datasets/Iris). I chose to import the dataset using the url and the pandas read_csv() function. I did this so the code work even outside my repository, unattached to the dataset. 

The packages I used are as follows:

'''
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

'''

Pandas allows you to manipulate the dataset as a dataframe. It was used to import the dataset, set up a dataframe, valdidate the valeus and then for aggregation and grouping of specific variables. I made extensive use of the Pandas documentation which can be found (here)[https://pandas.pydata.org/pandas-docs/stable/getting_started/index.html]

NumPy was used for mathematical operations adn when working with arrays/matrices. Its documentation can be found (here)[https://numpy.org/doc/stable/]

Matplotlib is an extension of NumPy and was used to present the data in plots. Its documentation is (here)[https://matplotlib.org/stable/index.html]

Seaborn was also used in the visualistation of the data. It has some extended functionality on Matplotlib when making plots. Seaborn documentation is (here)[https://seaborn.pydata.org/] 



Classes:
Iris Setosa
Iris Versicolour
irisVirginica

Ideas for analysis. 

Ranges of sepal size for all irises
ranges of petal size for all irises
average of sepal siz for all irises
average of petal size for all irises
ratio of sepal size to petal size for all irises


Ranges of sepal size for each class of irises
ranges of petal size for each class of irises
average of sepal siz for each class of irises
average of petal size for each class of irises

% occurance of each class # irrelevant as there is 50 of each

Graphs showing 3 classes sepal size and petal size

using this info we should be able to categorise a given organism (providing it is one of the 3 classes)

Standard deviation between the classes, possible indicate which are the most closely related

Importing DATA
I set the index as the 'Class' column by using the parameter (index_col)[https://proclusacademy.com/blog/practical/pandas-guide-for-absolute-beginners/]

###uninvariate analysis looks at one variable of a data set. i will do this for each of sepal length, sepal width, petal length and petal width
- histograms
- boxplots


data.info() provides a technical summary of the data frame. # https://pandas.pydata.org/pandas-docs/stable/getting_started/intro_tutorials/02_read_write.html#min-tut-02-read-write
This confirms it is a dataframe, how many rows and columns there are, how many non-null values there are and the 'type' in each column.


I created a histogram showing the distribution of values in each metric. When researching the number of bins to use, I came across (Sturge's Rule)[https://www.statology.org/sturges-rule/]

'''
Optimal Bins = ⌈log2n + 1⌉
'''
 
As each histogram will be for one data metric, there is 150 datapoints in each histogram. This means the optimal number of bins is 9. 

As there will be multiple graphs, I wanted to save them all to same folder "graphs". I did this by using the relative path within the 'fig.savefig' (command)[https://stackoverflow.com/questions/66583370/matplotlib-plot-image-save-path-python-vs-code]

Boxplots
https://pythonbasics.org/seaborn-boxplot/
https://proclusacademy.com/blog/quicktip/boxplot-separate-yaxis/

Making the labels bold = https://www.includehelp.com/python/bold-text-label-in-plot.aspx#:~:text=The%20command%20fontweight%3D'bold,or%20label%20in%20figure%20bold.


Multivariage analysis = looks at a number for different variables and the relationshipt betwween them.
- scatter pltos

ScatterPlot

I wanted to create a scatterplot of "Sepal Length" vs "Sepal Width", distinguishing the classes by colour and then to the same for "Petal Length vs Petal Width". I founds this (website)[https://datagy.io/pandas-scatter-plot/] a great resourse for this. 

In order to distinguish the Class by colour I created 3 different Dataframes, one for each class, assigned them a unique colour and then plotted them on the same scatterplot graph. 


###Results

The 