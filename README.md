# **Programming and Scripting Project**

## **Table of Contents**

1. Introduction to Dataset
2. Project Outline
3. Software Used
4. Analysis


## **Introduction to Dataset**

The Fischers Iris dataset was made by famous by statistician Ronald Fischer when he used it in his 1936 paper ["The use of multiple measurements in taxonomic problems"](https://onlinelibrary.wiley.com/doi/10.1111/j.1469-1809.1936.tb02137.x). However it was actually compiled before this by Edgar Anderson, a botanist who was examining the variation within the Iris flower. 

The 1936 paper was proposing 'Fishers linear discriminant' which today is known as linear discrimanent analysis. This is a [method](https://www.geeksforgeeks.org/ml-linear-discriminant-analysis/) used in statistics to find a combination of features that can best seperate the data into distinct classes.

The dataset is hosted on the [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/iris). It consists of 3 classes of iris; 

<img src="https://github.com/Kevin002023/pands-project/blob/main/images/Setosa.jpg" width="250" height="250" title="Iris-setosa">
-Iris-Setosa
<img src="https://github.com/Kevin002023/pands-project/blob/main/images/Veriscolor.jpg" width="250" height="250" title="Iris-veriscolor">
-Iris-veriscolor
<img src="https://github.com/Kevin002023/pands-project/blob/main/images/Virginica.jpg" width="250" height="250" title="Iris-virginica">
-Iris-virginica


It is a multivariate dataset containing information on 150 specimens of iris. There are 5 attributes recorded for each specimen. [These are as follows](https://archive.ics.uci.edu/ml/datasets/iris) :

1. sepal length in cm
2. sepal width in cm
3. petal length in cm
4. petal width in cm
5. class:
- Iris Setosa
- Iris Versicolour
- Iris Virginica

Fischer used this information to identify a method of distinguishing between the classes of iris's. It has since been used as a benchmark dataset for machine learning algorithims.

## **Project Outline**

The purpose of the project was to research the Iris dataset, import it to python and write a program called 'analysis.py' that would be used to analyse the dataset. We were to produce plots of this analysis and output the results fo any commands to a text file called 'project.txt'.

The purpose of the analysis done by Fisher on this dataset was to see if he could distinguish the class of iris based on the metrics it contains or a combination thereof.  I would like to try and replicate this. 

In order to acheive this, a univariate analysis was carried out, where a singular variable was looked at. This was done by producing plots to show the ditribution and variance for Sepal and petal lenghts and widths. The [Pandas documnetation](https://pandas.pydata.org/pandas-docs/version/0.13.1/visualization.html#targeting-different-subplots) was a great source of information on generating plots.

After this a multivariate analysis was performed, where the relationship between certain variables was looked at.


## **Software Used**

This project was done using python on Visual Studio Code. It was used to produce both the code and this README.md file.

The dataset is availble from the machine learning repository of UCI(http://archive.ics.uci.edu/ml/datasets/Iris). 

The packages I used are as follows:

````
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

````

Pandas allows you to manipulate the dataset as a dataframe. It was used to import the dataset, set up a dataframe, valdidate the valeus and then for aggregation and grouping of specific variables. I made extensive use of the Pandas documentation which can be found [here](https://pandas.pydata.org/pandas-docs/stable/getting_started/index.html)

NumPy was used for mathematical operations adn when working with arrays/matrices. Its documentation can be found [here](https://numpy.org/doc/stable/)

Matplotlib is an extension of NumPy and was used to present the data in plots. Its documentation is [here](https://matplotlib.org/stable/index.html)

Seaborn was also used in the visualistation of the data. It has some extended functionality on Matplotlib when making plots. Seaborn documentation is [here](https://seaborn.pydata.org/)


## **Analysis**

I chose to import the dataset using the url and the pandas read_csv() function. I did this so the code would work even with the dataset unattached to the repository. The dataset is called 'data' in my code hereafter. 

````
data_url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
col_headings = ['Sepal Length', 'Sepal Width', 'Petal Length', 'Petal Width', 'Class']
data= pd.read_csv(data_url, sep=",",  names = col_headings,)

````
The next step was to look at the data and run some checks to make sure it looks as expected. However as I wanted all commands to be outputted to my textfile ['project.txt'](https://github.com/Kevin002023/pands-project/blob/main/project.txt), I first created it, using the methods [here](https://www.geeksforgeeks.org/reading-writing-text-files-python/). 

``
with open('project.txt', 'w') as f:
    f.write("This is the text file where the outputs of my commands will be recorded \n")
``

I first wanted to ensure the dataset was as expected. I used the function data.shape, which presented the below

``
The below command confirms there are 150 samples with 5 pieces of information like we are expecting. 
(150, 5)
``

This is as expected. As stated in the summary, there are 150 samples with 5 variables.  Next I wanted to view the actual data to ensure it was presenting correctly. I used the functions head(), tail() in order to view the first and last 5 rows of the dataset.  This appeared as below;

````
The below is the first 5 lines of the dataset
   Sepal Length  Sepal Width  Petal Length  Petal Width        Class
0           5.1          3.5           1.4          0.2  Iris-setosa
1           4.9          3.0           1.4          0.2  Iris-setosa
2           4.7          3.2           1.3          0.2  Iris-setosa
3           4.6          3.1           1.5          0.2  Iris-setosa
4           5.0          3.6           1.4          0.2  Iris-setosa
````

````
The below is the last 5 lines of dataset
'     Sepal Length  Sepal Width  Petal Length  Petal Width           Class
145           6.7          3.0           5.2          2.3  Iris-virginica
146           6.3          2.5           5.0          1.9  Iris-virginica
147           6.5          3.0           5.2          2.0  Iris-virginica
148           6.2          3.4           5.4          2.3  Iris-virginica
149           5.9          3.0           5.1          1.8  Iris-virginica
````

The dataset is presenting as expected. The next step was to get some preliminary statistics regarding each variable. The Pandas function describe() does this for us. 

````
Below is a list of statistics regarding this dataset 

       Sepal Length  Sepal Width  Petal Length  Petal Width
count    150.000000   150.000000    150.000000   150.000000
mean       5.843333     3.054000      3.758667     1.198667
std        0.828066     0.433594      1.764420     0.763161
min        4.300000     2.000000      1.000000     0.100000
25%        5.100000     2.800000      1.600000     0.300000
50%        5.800000     3.000000      4.350000     1.300000
75%        6.400000     3.300000      5.100000     1.800000
max        7.900000     4.400000      6.900000     2.500000

````

The above commands were all added to 'project.txt' using the write() command. However this command expects any input to be a string, wheras the head(), tail(), info() and describe() funcitons all generate dataframes. To counteract this they were converted to strings in the write command.  


##Univariate Analysis

Univariate Analysis where only one variable is looked at, at a time. This was done for Sepal Length, Sepal Width, Petal Length and Petal Width.

#Histogram

A Histogram is a visual representation of the distribution of values. The range of values are grouped into a series of intervals called 'bins' and the frequency of each value inside these bins is then plotted on the graph. The number of bins can greatly impact the effectiveness of the histogram. If we have too few, there will be a lack of detail making it difficult to identify any pattern, too many and the distribution will look rough and there will be too much "noise". ["Sturges Rule"](https://www.statology.org/sturges-rule/) is a method of identifying the optimal number of bins to use. 

``
Optimal Bins = ⌈log2n + 1⌉
``
 
As each histogram will be for one data metric, there is 150 datapoints in each histogram. This means the optimal number of bins is 9. 


In this case each variable was plotted on its own seperate histogram. To do this a series was created for each variable and then used to create a plot. 

By creating an array called ``axs``, each variable could have its own subplot on the one image. 

![Iris histogram](https://github.com/Kevin002023/pands-project/blob/main/images/hist_iris.png)

A ['normal distribution'](https://www.techtarget.com/whatis/definition/normal-distribution#:~:text=What%20is%20normal%20distribution%3F,the%20mean%20of%20the%20distribution.) of values will have a bell curve. 

-Sepal length: Has a unimodal distribution (ie, a singular peak). while it isnt strictly symmetrical, it can be considered normal distribution wiht a slight skew to the right.

-Sepal Width: This also has a unimodal distribution and the classical bell shape you would expect from a normal distribution.

-Petal Length: This has a bimodal (two peaks) distribution and skews towards the right.

-Petal Width: Again this has a bimodal distribution and skews to the right. 


###uninvariate analysis looks at one variable of a data set. i will do this for each of sepal length, sepal width, petal length and petal width
- histograms
- boxplots



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