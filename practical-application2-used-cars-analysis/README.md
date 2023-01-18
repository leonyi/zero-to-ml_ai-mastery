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
This section describes the decisions/observations made in each phase of the analysis cycle. We start the section with a brief summary on the business understanding.

## Business Understanding
The used car market is huge. Some poeple prefer to buy used or certified pre-owned vehicles due to depreciation. Studies show that a brand new car looses ~ 9 - 11% of their value the moment its driven off the lot. It is also predicted that by the year 2030 it will be a 2.75 Trillion USD market. With this context in mind is important for a used car agency to have reliable data and trained models that can generate accurate predictions (and market analysis) on what type of car inventory (with key features) is to be built to increase sales and possibly profits.

## Data Understanding and Exploration
The goal here was to find out more about the patterns in the data to answer a key question, **what makes used cars valuable to used car buyers?** among the following:

* What features have strong correlation with the prices?
* Are there any features with missing values?
* What data types does the dataset have available?
* Do we have categorical features? Do any of them need to be encoded?
* How do we make projections on profits based on the base purchase price of the car (i.e. the price the Agency paid for the car)?

After thinking through the questions, we started by understanding the shape of the dataset, which houses 426880 records and 18 features for ~426K cars. We run a correlation check and found that we had only a handful of numerical values (i.e. id, price, year and odometer). The price correlation output showed the strongest correlation with the odometer and year. The data showed that there is a positive  The output of this initial correlation can be accessed under the [Data Exploration Section](bhttps://github.com/leonyi/zero-to-mlai-mastery/blob/main/practical-application2-used-cars-analysis/used-cars-analysis.ipynb) of the included Jupyter notebook. 

## Data Preparation
Null values were detected on a handful of columns. The percentages of missing values by feature are listed below:
```
size            71.77
cylinders       41.62
condition       40.79
VIN             37.73
drive           30.59
paint_color     30.50
type            21.75
manufacturer     4.13
title_status     1.93
model            1.24
odometer         1.03
fuel             0.71
transmission     0.60
year             0.28
```
The car size missing data was calculated to be ~72% missing of the total dataset records and may not keep it. For the others we will have to do more analysis and decide what we will do with them. Another interesting observation was with the title_status, which predominantly shows a clean status at ~98% of the total data, we may consider dropping that column since the other statuses may not offer much value to the analysis. For the curious, other title_status were broken down as follows:

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

1. Possibly drop the 'size' feature from the dataframe. At approximately ~72% is a relatively high missing data.
2. For the title_status column the most predominant entry is 'clean'. Keeping it may may not add much value to the analysis, so the column will be dropped.
3. Categorical features like the case of 'fuel' will be hot encoded. Others, like 'condition' will be transformed into ordinal values. 
4. Categorical feature, 'cylinders' will be converted to numerical value.
5. Categorical features that hold multiple values will be handled in a case by case basis. 

The implementation of each decision can be accessed on the [implementing decisions section](https://github.com/leonyi/zero-to-mlai-mastery/blob/main/practical-application2-used-cars-analysis/used-cars-analysis.ipynb) of the Jupiter Notebook included on this directory.

## Data Evaluation
Once the data was sanitized we started the analysis and had the following observations:

[General Obserations]
* Features with strongest impact on price resulted in year, odometer reading, number of cylinders, 
* We also see Electric vehicles with positive correlation with price.
* At this time, we can recommend that inventory includes vehicles with lower odometer readings, more cylinders and ideally not too old. However, with the current data we can't make predictions on sales/profit details.
* The data analyzed didn't provide sufficient context to determine precisely what type of cars would result in higher sales, possibly increasing profits. Without this data, the analysis would be incomplete if we bring it back to our client.


## Data Deployment
The data analysis revealed that used car buyers are willing to pay more for cars with lower odometer readings, that are newer and with automatic transmissions.  Other features that directly impact the used car appeal are electric or hybrid transmissions. Hence, keeping these types of cars in the inventory has a high potential of increasing sales. The analyzed dataset didn't cotain sufficient data on other features like fuel efficency, horsepower and other details that could also play a role in the car prices. The recommendation is to gather more data on the missing features and also use previous years sales details to correlate features and train a model to perform projections on how to increase profits based on the type of inventory the dealership must keep.


### Next Steps
* Collect more data to determine what other features can have a stronger impact on used car prices, that will increase their appeal to used car buyers, which could translate to better sales/profits.
* Some features that could positively impact price are horsepower, fuel efficiency, which were not included on the provided dataset.
* Richer data may help train a model that can better predict profits for a given used car agency based on their inventory and previous sales data.

## Sources 
* The data for this analysis came from [Kaggle](https://www.kaggle.com/datasets).
* Used car market size data from [Globe Newswire](https://www.globenewswire.com/en/news-release/2022/09/22/2521333/0/en/Used-Car-Market-Size-is-projected-to-reach-USD-2-75-trillion-by-2030-growing-at-a-CAGR-of-6-17-Straits-Research.html).

