# Python for data analysis

> Authors Alix PETITCOL - Marine SUBLET 

*This project is made within the python course in Year 4 (Data science and artificial intelligence major) at [ESILV](https://www.esilv.fr/) - Engineering school*

> Packages required
>
> - For the visualization : Pandas, Seaborn, Matplotlib, Pygal, Wordcloud, Plotly
> - For the Prediction : Sklearn
> - For the API : Flask 


Instruction :

To run the project with git bash: 
1) go into Facebook_Comments_Project folder  
2) activate the virtual environment with $ cd Scripts then $ . activate
3) return into Facebook_Comments_Project folder (cd ..)
4) verify that all the packages were installed (if not: install flask, pandas, seaborn, matplotlib and the other modules with pip install command)

Then you can run the Flask App by using git bash command: $ python MyFlaskApp.py in the terminal. 

## Content of work delivered

The project is composed by :
- a Jupyter notebook and its HTML for more convenience. 
*To see the HTML file correctly please go on https://htmlpreview.github.io  and enter the HTML URL of Facebook_Python_Project.html > raw*
- You will find a flask application  name under MyFlaskApp.py
- The project report under PDF format

## Project Description

The intent of this project is to practice visualization and machine learning with python through a given dataset. 

For this project, we have chosen to work on the Facebook Comment Volume Dataset.

Due to the frequency of use of social networks today, it is interesting to study the behavior of consumers concerning these services. This work aims to study and model user activity from Facebook.

The main purpose here is to estimate the number of comments that a message should receive in the hours following its post. The analysis will be done first by studying through different graphs the user behaviors and trends that stand out the most. Secondly, we will implement some prediction algorithms using regression techniques.

Instances in this dataset contain 30 features directly extracted from Facebook posts, and 24 derived features that are aggregated by page, by calculating min, max, average, median, and standard deviation of essential features. 

The dataset contains 5 variants of data, however, for our complete study we have used only one of its datasets, due to its sufficient size.

## Visualization Study

*For some reasons, Most of our graphics were not displayed when you visualize the jupyter notebook on the git hub, so we put instead pictures of the expected graphics. An Alternative to interact with graphics is to used the HTML file provide **see section "Content of work delivered"**. However don’t hesitate to download the notebook and execute cells if you want to be able to interact with the graphs*

In the second part of the jupyter notebook, you will find the visualization study of the dataset. 
This section is delimitated into two main parts, the first one contains general visualizations of the dataset and the second focuses on some specific features.


## Machine Learning Part

In the third section of the jupyter notebook, you will find the machine learning work. It consits in a principal component analysis part *[Due to a large number of features in the datasets, we chose to compute a PCA]* and a prediction part. 


The intent was to reduce the dimension of the datasets, increase their interpretability while minimizing the information loss.


## Result

thanks to our visualization study, we got to understand our dataset and the way its features impacted the target variable. 

This helped us to make better predictions with our models and interpret the results in a more accurate way.
We managed to get an accuracy of  70% on the test set with the Random Forest Regression, which is a good result given the target variable we had to predict.
