# Used Car Sales Analysis
**OVERVIEW**

In this repo we provide an exploration and in-depth analyis of a 'used cars' dataset from kaggle. The original dataset contained information on 3 million used cars. The provided dataset contains information on 426K cars. The smaller dataset ensures speed of processing.

**Goal of Analysis**

The goal is to understand what factors make a car more or less expensive. As a result of your analysis, you should provide clear recommendations to your client -- a used car dealership -- as to what consumers value in a used car.

To frame the task, throughout our practical applications we will refer back to a standard process in industry for data projects called CRISP-DM. This process provides a framework for working through a data problem.


# Context
The goal of this project was to understand, prepare and model the used cars data to describe the factors that make a car more or less expensive and valuable to customers. The result of the analysis provide recommendations of possible value to our hypothetical customer -- a used car dealership. 


# How this directory is structured 

| Item Name     | Description   |
| ------------- | ------------- |
| data/         | Directory containing the data set in .csv format. |
| env/          | Directory housing a yaml file with all needed requirements to create a conda dev environment to run the Juypter notebook in you laptop. |
| [used-cars-analysis.ipynb](https://github.com/leonyi/zero-to-mlai-mastery/blob/main/practical-application-5-1-coupon-acceptace-analysis/used-cars-analysis.ipynb)       | Jupyter Notebook with the in-depth analysis. |
| README.md     | This file. |

# Analysis Summary
This section describes the decisions/observations made in each phase of the analysis cycle.

## Data Exploration
The goal here was to find out more about the patterns in the data to answer a key question, **what makes used cars valuable to used car buyers?** among the following:

* What features have strong correlation with the prices?
* Are there any features with missing values?
* What data types does the dataset have available?
* Do we have categorical features? Do any of them need to be encoded?
* How do we make projections on profits based on the base purchase price of the car (i.e. the price the Agency paid for the car)?

After thinking through the questions, we started by understanding the shape of the dataset, which houses 426880 records and 18 features. No obvious numerical correlations were observed but the ouput of the pairwise correlation of columns did show an interesting positive correlation between accepting coupons and temperature. The output of this initial correlation can be accessed under the [Exploration Section](http://localhost:8888/notebooks/Customers_and_Coupons_Acceptance_Analysis.ipynb#Data-Exploration) of the included Jupyter notebook.

## Data Sanitation
Null values were detected on a handful of columns:
```
size            306361
cylinders       177678
condition       174104
VIN             161042
drive           130567
paint_color     130203
type             92858
manufacturer     17646
title_status      8242
model             5277
odometer          4400
fuel              3013
transmission      2556
year              1205
```
The car size missing data was calculated to be ~72% missing of the total dataset records and keeping it was definitely not going to be appropriate. For the others we will have to do more analysis and decide what we will do with them. Another interesting observation was with the title_status, which predominantly shows a clean status at ~98% of the total data, we may consider dropping that column since the other statuses may not offer much value to the analysis. For the curious, other title_status were broken down as follows:

```
lien          1422
missing        814
parts only     198
rebuilt       7219
salvage       3868
```

A summary of the decisons is listed on the following sections.

### The Decisions
To facilitate analysis of the data the following decisions were made to deal with the missing data:

1. Possibly drop the size data from the dataframe. At approximately ~72% is a relatively high missing data.
2. For the title_status column the most predominant entry is 'clean'. Keeping it may may not add much value to the analysis, so the column will be dropped.
3. Categorical features like the case of 'fuel' will be hot encoded. Others, like 'condition' will be transformed into ordinal values.
4. Categorical features that hold multiple values will be handled in a case by case basis. 

The implementation of each decision can be accessed on the [implementing decisions section](http://localhost:8888/notebooks/Customers_and_Coupons_Acceptance_Analysis.ipynb#Implementing-the-decisions) of the Jupiter Notebook included on this directory.

### Data 
Once the data was sanitized we started the analysis and had the following observations:

[General Obserations]
* 
*


### Next Steps
* Continue exploring the "Coffee House" and the "Restaurant(<20)" as they reported the highest **total** counts for acceptance rates. We may be able to uncover good insights on what influenced the drivers who received those coupons to accept them.
* Create other visualizations to summarize the observations for each of the aforementioned features.


## Sources 
The data for this analysis came from [uci.edu machine learning archive](https://archive.ics.uci.edu/ml/datasets/in-vehicle+coupon+recommendation#).

