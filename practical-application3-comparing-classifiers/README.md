# Comparing Classifiers Performance 
**OVERVIEW**

In this repo you will find a comparisson in performance of a handful of classifiers. To perform the analysis we utilized a dataset related to marketing bank products over the telephone from the [UCI Machine Learning](https://archive.ics.uci.edu/ml/datasets/bank+marketing) repository.

**Goal of Analysis**

The goal is to apply the knowledge acquired and compare the performace of several classifiers: K Nearest Neighbor, Logistic Regression, Decision Trees, and Support Vector Machines.


# Context
The dataset, used for the analysis, comes from the [UCI Machine Learning repository](https://archive.ics.uci.edu/ml/datasets/bank+marketing). The data is from a Portugese banking institution and is a collection of the results of multiple marketing campaigns. The dataset collected is related to 17 campaings that occurred between May 2008 and November 2010, corresponding to a total of 79354 contacts. You can gather more context on this by reading this [this document](http://localhost:8888/notebooks/module_17_practical_application3/practical-application3-comparing-classifiers/CRISP-DM-BANK.pdf).


# How this directory is structured 

| Item Name     | Description   |
| ------------- | ------------- |
| data/         | Directory containing the data set in .csv format. |
| env/          | Directory housing a yaml file with all needed requirements to create a conda dev environment to run the Juypter notebook in you laptop. |
| [comparing-classifiers.ipynb](https://github.com/leonyi/zero-to-mlai-mastery/blob/main/practical-application3-comparing-classifiers/comparing-classifiers.ipynb)       | Jupyter Notebook with the in-depth analysis. |
| README.md     | This file. |

# Analysis Summary
This section describes the decisions/observations made in each phase of the analysis cycle. Throughout this README, I use the words column and feature interchangeably.

## Data Exploration
The goal here was to find out more about the patterns in the data to answer a key question, **which clients are likely to subscribe to a term deposit?** among the following:

* Are there any features with missing values?
* What data types does the dataset have available?
* Do we have categorical features? Do any of them need to be encoded?
* What features have strong statistical importance to influence the prediction?
* How do we use the data to predict what the outcome of the Bank's campaign would be with regards to increasing clients' term deposits?

After thinking through the questions, we started by understanding the shape of the dataset, which houses 41188 records and 21 features. The output of this initial correlation can be accessed under the [Data Exploration](https://github.com/leonyi/zero-to-mlai-mastery/blob/main/practical-application3-comparing-classifiers/comparing-classifiers.ipynb) section of the included Jupyter notebook.

## Features Understanding and Selection
* No missing data found
* Heatmap revealed that the euribor3m feature strongly correlated (almost perfectly colinearly) with emp.var.rate (97) and nr.employed (.95). 
* We noticed that the dataset had both categorical and numeric features:
    * The categorical features consisted of 11 features (including the target)
    * The numerical features totalled 10.

### The Decisions
To facilitate analysis of the data the following decisions were made:
* Cleaning the data in the different columns:
    * Decided to delete euribor3m because of its strong correlation with both em.var.rate and nr.employed. Highly correlated attributes in the dataset can lead to poor performance in LogisticRegression models.
    * Decided to remove the variable *yes* from the default column since it only held 3 observations. The majority belonged to *no* and *unknown*. Didn't seem to hold much statistical importance.
    * The *age* feature trends uncovered three bins in which the observations could be grouped: young (<= 30), middle (> 30) and senior (>60). Per the data we also uncovered that this data set had a min age of 17, an average age of 40 and a max age of 98. This feature was transformed into a category.
    * For the *job* feature we removed observations with "unknown" entries. The same was done for the *marital* variable.
    * Decided to remove the *personal loan* column
    * The *duration* feature is discarded (as suggested in the data description). It had a strong positive skew - highly impacting the target.

* Transform all the categorical features into numerical values:
    * The day_of_week feature was convereted to integer
    * The age column category was transformed to an int value via label encoding
    * The job, marital, education, contact and poutcome features were transformed using one hot encoding
 

The implementation of each decision can be accessed on the [implementing decisions section](http://localhost:8888/notebooks/Customers_and_Coupons_Acceptance_Analysis.ipynb#Implementing-the-decisions) of the Jupiter Notebook included on this directory.

### Summary
The data revealed the following:
* People over 60 years old and younger relative to their population grups at 83% and 17%, respectively are more likely to take a deposit than middle age people at 10%.
* Married people are less likely to subscribe to a term deposit.
* High likelyhood that success in a previous campaign could result in clients signing up for a term deposit

The models tested on a local laptop environment resulted in the following accuracy scores:

| Model Name    | Training Time   |  Training Accuracy Score   | Test Accuracy Score    | 
| ------------- | --------------- |--------------------------- | ---------------------- |
| Logistic Regression | 2.13 ms   |  0.8962363330529857   | 0.8998364677023712    | 
| K-NN    | 10.7 ms   |  0.912636669470143   | 0.8973017170891251    | 
| Decision Tree    | 85.6 ms   | 0.9460681244743482 | 0.8842191332788226    | 
| SVM    | 10.7 s   | 0.8865643397813289 | 0.8893704006541292    | 

### Conclusion 
For this particular analysis logistic regression did the best job with balanced accuracy.  Results of the SVM model also looked adequate (although its training time took longer than the other algoritms) followed by KNN. The Decision tree performed the poorest on this particular analysis. It seems like the Bank could benefit from using the LogisticRegression model to predict if a client would subscribe to a term deposit given the current results of this analysis.

### Next Steps
* Analyze the skews closer to see how we can re-prepare the data to work on improving accuracy of the models.
* Continue improving the model
    - Run more tests to determine accuracy for each model on TP, TN, FP & FN.
    - Do more exploration on hyperparameters tuning for each model
    - Get more in depth results for model sensitivity & specificity.
    - With a more robust system we could also try Random Forest, Gradient Boosting or more intense computations of SVM to try to achieve the best possible predictions.

## Sources 
* Information Value function code from [Kaggle](https://www.kaggle.com/code/podsyp/information-value-iv-weight-of-evidence-woe/notebook).
* What is [information value (IV)](https://www.listendata.com/2015/03/weight-of-evidence-woe-and-information.html)?
* [Understanding chi-squared test](https://machinelearningmastery.com/chi-squared-test-for-machine-learning/)
* [machinelearningmastery.com](https://machinelearningmastery.com/how-to-study-machine-learning-algorithms/)

