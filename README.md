# **Programming and Scripting Project**

## **Table of Contents**

1. [Introduction to Dataset](#introduction-to-dataset)
2. [Project Outline](#project-outline)
3. [Software Used](#software-used)
4. [Analysis](#analysis)
    1. [Univariate](#univariate)
    2. [Multivariate](#multivariate)
5. [Conclusion](#conclusion)
6. [References](#references\)



## **Introduction to Dataset**

The Fischers Iris dataset was made by famous by statistician Ronald Fischer when he used it in his 1936 paper ["The use of multiple measurements in taxonomic problems"](https://onlinelibrary.wiley.com/doi/10.1111/j.1469-1809.1936.tb02137.x). However, it was actually compiled before this by Edgar Anderson, a botanist who was examining the variation within the Iris flower. 

The 1936 paper was proposing 'Fishers linear discriminant' which today is known as linear discriminant analysis. This is a [method](https://www.geeksforgeeks.org/ml-linear-discriminant-analysis/) used in statistics to find a combination of features that can best seperate the data into distinct classes.

The dataset is hosted on the [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/iris). It consists of 3 classes of iris; 

<img src="https://github.com/Kevin002023/pands-project/blob/main/images/iris-image.png">
- The image above shows the 3 classes of iris in this data set.


It is a multivariate dataset containing information on 150 specimens of iris. There are 5 attributes recorded for each specimen. [These are as follows](https://archive.ics.uci.edu/ml/datasets/iris) :

1. sepal length in cm
2. sepal width in cm
3. petal length in cm
4. petal width in cm
5. class:
- Iris Setosa
- Iris Versicolour
- Iris Virginica

Fischer used this information to identify a method of distinguishing between the classes of iris's. It has since been used as a benchmark dataset for machine learning algorithms.

## **Project Outline**

The purpose of the project was to research the Iris dataset, import it to python and write a program called 'analysis.py' that would be used to analyse the dataset. We were to produce plots of this analysis and output the results of any commands to a text file called 'project.txt'.

The purpose of the analysis done by Fisher on this dataset was to see if he could distinguish the class of iris based on the metrics it contains or a combination thereof.  I would like to try and replicate this. 

In order to achieve this, a univariate analysis was carried out, where a singular variable was looked at. This was done by producing plots to show the distribution and variance for sepal and petal lengths and widths. The [Pandas documentation](https://pandas.pydata.org/pandas-docs/version/0.13.1/visualization.html#targeting-different-subplots) was a great source of information on generating plots.

After this a multivariate analysis was performed, where the relationship between certain variables was looked at. This was done using scatter-plots and a pair-plot. 


## **Software Used**

This project was done using Python 3.09.13, on the editor Visual Studio Code V 1.75.1. It was used to produce both the code and this README.md file.

The dataset is available from the machine learning repository of UCI(http://archive.ics.uci.edu/ml/datasets/Iris). 

The packages I used are as follows:

````
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

````

Pandas allows you to manipulate the dataset as a dataframe. It was used to import the dataset, set up a dataframe, validate the values and then for aggregation and grouping of specific variables. I made extensive use of the Pandas documentation which can be found [here](https://pandas.pydata.org/pandas-docs/stable/getting_started/index.html)

NumPy was used for mathematical operations and when working with arrays/matrices. Its documentation can be found [here](https://numpy.org/doc/stable/)

Matplotlib is an extension of NumPy and was used to present the data in plots. Its documentation is [here](https://matplotlib.org/stable/index.html)

Seaborn was also used in the visualization of the data. It has some extended functionality on Matplotlib when making plots. Seaborn documentation is [here](https://seaborn.pydata.org/)


## **Analysis**

The dataset was imported using the url and the pandas read_csv() function.  This was done so the code would work even with the dataset unattached to the repository. The dataset is called 'data' in my code hereafter. 

````
data_url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
col_headings = ['Sepal Length', 'Sepal Width', 'Petal Length', 'Petal Width', 'Class']
data= pd.read_csv(data_url, sep=",",  names = col_headings,)

````
The next step was to look at the data and run some checks to make sure it looks as expected. However, as I wanted all commands to be outputted to my textfile ['project.txt'](https://github.com/Kevin002023/pands-project/blob/main/project.txt), I first created it, using the methods [here](https://www.geeksforgeeks.org/reading-writing-text-files-python/). 

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

The above commands were all added to 'project.txt' using the write() command. However, this command expects any input to be a string, whereas the head(), tail(), info() and describe() functions all generate dataframes. To counteract this they were converted to strings in the write command.  


### Univariate Analysis

Univariate Analysis where only one variable is looked at, at a time. This was done for Sepal Length, Sepal Width, Petal Length and Petal Width.

**Histogram**

A Histogram is a visual representation of the distribution of values. The range of values are grouped into a series of intervals called 'bins' and the frequency of each value inside these bins is then plotted on the graph. The number of bins can greatly impact the effectiveness of the histogram. If we have too few, there will be a lack of detail making it difficult to identify any pattern, too many and the distribution will look rough and there will be too much "noise". There are multiple different ways of calculating the correct number of bins. In this case ["Sturges Rule"](https://www.statology.org/sturges-rule/) was used. 

``
Optimal Bins = ⌈log2n + 1⌉
``
 
As each histogram will be for one data metric, there are 150 datapoints in each histogram. This means the optimal number of bins is 9. 


In this case each variable was plotted on its own separate histogram. To do this a series was created for each variable and then used to create a plot. 

By creating an array called ``axs``, each variable could have its own subplot on the one image. 

![Iris histogram](https://github.com/Kevin002023/pands-project/blob/main/images/hist_iris.png)

A ['normal distribution'](https://www.techtarget.com/whatis/definition/normal-distribution#:~:text=What%20is%20normal%20distribution%3F,the%20mean%20of%20the%20distribution.) of values will have a bell curve. 

- Sepal length: Has a unimodal distribution (ie, a singular peak). While it isn't strictly symmetrical, it can be considered normal distribution with a slight skew to the right.

- Sepal Width: This also has a unimodal distribution and the classical bell shape you would expect from a normal distribution.

- Petal Length: This has a bimodal (two peaks) distribution and skews towards the right.

- Petal Width: Again this has a bimodal distribution and skews to the right. 

Histograms were also produced for each variable separated by class. 

**Boxplot**

A [boxplot](https://pandas.pydata.org/pandas-docs/version/0.25.3/reference/api/pandas.DataFrame.boxplot.html#pandas.DataFrame.boxplot) is another graphical representation of the distribution of a dataset.  They highlight important statistical measures like range, median and outliers. The boxes are drawn between the first and third Quartile. The bold line in the middle of the box represents the median. The 'whiskers' represent the range of data. Any dots above or below are outliers.

Again for ease of comparison each variant was a subplot allowing all 4 on the same image. 

![Boxplot](https://github.com/Kevin002023/pands-project/blob/main/images/Boxplots.png)

For both sepal length and width there is much overlap in the range of values for all 3 classes. It would be very difficult to identity what class an iris belonged to based on either of these two variables. However, it is immediately noticeable that this is not the case when comparing Petal length and width. While there is an overlap in the values for Iris-versicolor and Iris-virginica, the size of the petals for Iris-setosa are significantly smaller. In addition, Iris-setosa has a much narrower range of values. 


## Multivariate Analysis

Multivariate analysis is where 2 or more variable are examined at once to try and identify a relationship between them. 

**Scatter Plot**

This is a chart that shows the relationship between two variables. In this case we explored the relationship between Sepal Length and Sepal Width and then Petal Length and Petal Width. 

![Scatter Plot of Sepal Length vs Sepal Width (cm)](https://github.com/Kevin002023/pands-project/blob/main/images/Sepal_scatter.png)

From looking at this plot, we can see there is a great overlap in Sepal values for both Iris-Versicolor and Iris-Virginica. It would be very difficult to distinguish between these classes based on these variable. 

However, Iris-Setosa is grouped separately to the other two. These variables could be used in identifying a specimen from this class. Based on this (albeit limited) dataset if the sepals have a width greater than 3cm and a length less than 6cm it is likely Iris-Setosa.

![Scatter Plot of Petal Length vs Petal Width(cm)](https://github.com/Kevin002023/pands-project/blob/main/images/Petal_scatter.png)

Here, it can be seen again a division between Iris-Setosa and the other two classes. Although in this case there is more of a divergence between Iris-Versicolor and Iris-Virginica than when looking at their Sepals.  If the petal has a length of less than 3cm and a width of less than 1cm there is a strong likelihood that it belongs to the Iris-setosa class. 

## Pair Plots

A [pair-plot](https://datagy.io/seaborn-pairplot/) is another method of looking at the relationship of two variables. They compare each variable to every other variable.

![PairPlot](https://github.com/Kevin002023/pands-project/blob/main/images/Pairplot.png)

The diagonal line shows the distribution of values in each variable by using a histogram. The other plots all represent one variable plotted with another.  Each point is also coloured based on its classification. 

Using the above scatter-plots and pair plot, we can see that there is a positive linear relationship between petal length and petal width. There is a roughly straight line with a positive slope indicating a positive linear relationship. If there was a straight line with a negative slope it would indicate a negative linear relationship. 

The other variables do not seem to have any linear relationship between each other. It is notable that Iris-setosa shares little overlap between the other two classes. 

## **Conclusion**

I can already conclude that it seems that there is no relationship between the sepal length and sepal width and probably petal length and width have the strongest linear relationship.



## **References**


- “Pandas documentation — pandas 2.0.1 documentation,” Pydata.org. [Online]. Available: https://pandas.pydata.org/pandas-docs/stable/index.html. 

- “NumPy documentation — NumPy v1.24 manual,” Numpy.org. [Online]. Available: https://numpy.org/doc/stable/.

- “Matplotlib documentation — Matplotlib 3.7.1 documentation,” Matplotlib.org. [Online]. Available: https://matplotlib.org/stable/index.html. 

- “Seaborn: Statistical data visualization — seaborn 0.12.2 documentation,” Pydata.org. [Online]. Available: https://seaborn.pydata.org/. 

- Sauravdeb, “Introduction to Machine learning: Iris dataset,” Medium, 02-Oct-2021. [Online]. Available: https://medium.com/@sauravdeb98/introduction-to-machine-learning-iris-dataset-58f2f30f966e. 

- “Statistical analysis on IRIS dataset,” Kaggle.com, 22-May-2022. [Online]. Available: https://www.kaggle.com/code/neha99/statistical-analysis-on-iris-dataset. 

- “Iris-data-analysis.knit,” Amazonaws.com. [Online]. Available: https://rstudio-pubs-static.s3.amazonaws.com/848706_1fdca2c961d54f1e9909fe64e127095a.html.

- “Extended syntax,” Markdownguide.org. [Online]. Available: https://www.markdownguide.org/extended-syntax/.

- “User guide and tutorial — seaborn 0.12.2 documentation,” Pydata.org. [Online]. Available: https://seaborn.pydata.org/tutorial.html. 

- “Matplotlib tutorial,” W3schools.com. [Online]. Available: https://www.w3schools.com/python/matplotlib_intro.asp.

- Nik, “Creating Pair Plots in Seaborn with sns pairplot,” datagy, 11-Jul-2022. [Online]. Available: https://datagy.io/seaborn-pairplot/. 

- “How to add header row to a Pandas Dataframe?,” GeeksforGeeks, 25-Dec-2020. [Online]. Available: https://www.geeksforgeeks.org/how-to-add-header-row-to-a-pandas-dataframe/. 

- “Plotting with matplotlib — pandas 0.13.1 documentation,” Pydata.org. [Online]. Available: https://pandas.pydata.org/pandas-docs/version/0.13.1/visualization.html.

- “How to plot multiple dataframes in subplots,” Stack Overflow. [Online]. Available: https://stackoverflow.com/questions/22483588/how-to-plot-multiple-dataframes-in-subplots.

- M. Pradhan, “Exploratory Data Analysis on Iris Dataset,” Tutorialspoint.com. [Online]. Available: https://www.tutorialspoint.com/exploratory-data-analysis-on-iris-dataset. 

- “Matplotlib plot image save path python VS Code,” Stack Overflow. [Online]. Available: https://stackoverflow.com/questions/66583370/matplotlib-plot-image-save-path-python-vs-code. 

- “Seaborn boxplot,” Pythonbasics.org. [Online]. Available: https://pythonbasics.org/seaborn-boxplot/.

- Y. Singh, “Boxplot with separate Y-axis for each column,” Proclus Academy. [Online]. Available: https://proclusacademy.com/blog/quicktip/boxplot-separate-yaxis/. 

- “Bold Text Label in Python Plot,” Includehelp.com. [Online]. Available: https://www.includehelp.com/python/bold-text-label-in-plot.aspx. 

- [Online]. Available: http://ttps://datagy.io/pandas-scatter-plot/. 

- Zach, “What is Sturges’ Rule? (definition & example),” Statology, 11-Jan-2021. [Online]. Available: https://www.statology.org/sturges-rule/.

- Zach, “Seaborn: How to Use hue Parameter in Pairplot,” Statology, 16-Feb-2023. [Online]. Available: https://www.statology.org/seaborn-pairplot-hue/. 

- D. S. W. Shen, “Linear Regression using Iris dataset — ‘hello, world!’ of machine learning,” Analytics Vidhya, 10-Mar-2020. [Online]. Available: https://medium.com/analytics-vidhya/linear-regression-using-iris-dataset-hello-world-of-machine-learning-b0feecac9cc1. 

- “Reading and Writing to text files in Python,” GeeksforGeeks, 03-Apr-2017. [Online]. Available: https://www.geeksforgeeks.org/reading-writing-text-files-python/. 

- Y. Singh, “How to read and write excel files using Pandas,” Proclus Academy. [Online]. Available: https://proclusacademy.com/blog/practical/pandas-read-write-excel-files/. 

- N. Mukherjee, “First step to Statistics (with Iris data) - Analytics Vidhya - Medium,” Analytics Vidhya, 01-Jun-2020. [Online]. Available: https://medium.com/analytics-vidhya/first-step-to-statistics-with-iris-data-3d29c0820c5d. 

- Nik, “Pandas Scatter Plot: How to make a Scatter Plot in Pandas,” datagy, 04-Mar-2022. [Online]. Available: https://datagy.io/pandas-scatter-plot/. 
