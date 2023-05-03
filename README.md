# pands-project

The Fischers Iris data set was put together in 1936 by Ronald Alymer Fisher. it was compuled for his paper "The use of multiple measurements in taxonomic problems" There are five cateogries of data. 4 of them relate to the measurements of the sepal adn petals and the fifth is the class or speices of iris. There are 50 plants of each spieces totalling 150 organisms in total. 

https://www.angela1c.com/projects/iris/ *
https://archive.ics.uci.edu/ml/datasets/iris

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

data.info() provides a technical summary of the data frame. # https://pandas.pydata.org/pandas-docs/stable/getting_started/intro_tutorials/02_read_write.html#min-tut-02-read-write
This confimrs it is a dataframe, how many rows and columns there are, how many non-null values there are and the 'type' in each column.