# Python for data analysis

> Authors Alix PETITCOL - Marine SUBLET 

*This project is made within the python course in Year 4 (Data science and artificial intelligence major) at [ESILV](https://www.esilv.fr/) - Engineering school*

> Packages required
>
> - For the visualization : Pandas, Seaborn, Matplotlib, Pygal, Wordcloud, Plotly)
> - For the Prediction : Sklearn
> - For the API : Flask 

You can run the Flask App by using git command : python MyFlaskApp.py in a git terminal. *[In the Facebook_Comments_Project folder]*

## Content of work delivered

The project is composed by :
- a Jupyter notebook and its HTML for more convienency. 
To see the html file correctly please go on https://htmlpreview.github.io  and enter this URL  "https://raw.githubusercontent.com/Alix-debug/Python-Project-Facebook-Comments/main/Facebook_Python_Project.html?token=ASJ3CKZ7MSUEPSLBHNXS6DTB2RNUG" 
- You will find a flask application as well name under MyFlaskApp.py
- The project report under pdf format

## Project Description

The intent of this project is to practice visualization and machine learning with python through a given dataset. 

For this project, we have chosen to work on the Facebook Comment Volume Dataset.

Due to the frequency of use of social networks today, it is interesting to study the behavior of consumers concerning these services. This work aims to study and model user activity from Facebook.

The main purpose here is to estimate the number of comments that a message should receive in the hours following its post. The analysis will be done first by studying through different graphs the user behaviors and trends that stand out the most. Secondly, we will implement some prediction algorithms using regression techniques.

Instances in this dataset contain 30 features directly extracted from Facebook posts, and 24 derived features that are aggregated by page, by calculating min, max, average, median, and standard deviation of essential features. 

The dataset contains 5 variants of data, however, for our complete study we have used only one of its datasets, due to its sufficient size.

## Visualization Study

In the second part of the jupyter notebook, you will find the visualization study of the dataset. 
This section is delimitated into two main parts, the first one contains general visualizations of the dataset and the second focuses on some specific features.


## Machine Learning Part

In the third section of the jupyter notebook, you will find the machine learning work. It consits in a principal component analysis part *[Due to a large number of features in the datasets, we chose to compute a PCA]* and a prediction part. 


The intent was to reduce the dimension of the datasets, increase their interpretability while minimizing the information loss.


## Result

thanks to our visualization study, we got to understand our dataset and the way its features impacted the target variable. 

This helped us to make better predictions with our models and interpret the results in a more accurate way.
We managed to get an accuracy of  70% on the test set with the Random Forest Regression, which is a good result given the target variable we had to predict.
