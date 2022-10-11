# Driver Coupon Acceptance Analysis
The analysis was conducted using the in-vehicle coupon recommendations dataset from the UCI machine learning archive and was collected via a survey on Amazon Mechanical Turk. The survey describes different driving scenarios including the destination, current time, weather, passenger, etc., and then ask the person whether he will accept the coupon if he is the driver. Answers that the user will drive there ‘right away’ or ‘later before the coupon expires’ are labeled as ‘Y = 1’ and answers ‘no, I do not want the coupon’ are labeled as ‘Y = 0’. There are five different types of coupons -- less expensive restaurants (under $20), coffee houses, carry out & take away, bar, and more expensive restaurants ($20 - $50). The data set contains various attributes that describe a driver/user, coupons, an other contextual attributes, whose description can aslo be foudn [here](https://archive.ics.uci.edu/ml/datasets/in-vehicle+coupon+recommendation#)


# Context
The goal of this project was to use visualizations and probability distributions to distinguish between customers who accepted a driving coupon versus those that did not based on different criteria.


# How this directory is structured 

| Item Name     | Description   |
| ------------- | ------------- |
| data/         | Directory containing the data set in .csv format. |
| env/          | Directory housing a yaml file with all needed requirements to create a conda dev environment to run the Juypter notebook on you laptop. |
| Customers_and_Coupons_Acceptance_Analysis.ipynb       | Jupyter Notebook with the in-depth analysis. |
| README.md     | This file. |

# Analysis Summary
This section describes the decisions/observations made in each phase of the analysis cycle.

## Data Exploration
The process started by setting a goal before getting familiar with the data. Our goal was to answer the main question on this dataset, **will the customer accept the coupon?** taking into account different criteria and the following questions as we cleaned and queried the data:

* How would you determine whether a driver is likely to accept the coupon?
* What factors would determine whether a driver accepts the coupon once it is delivered to them?
    * Would the driver accept the coupon and take a short detour to the restaurant?
    * Would the driver accept the coupon but use it on a subsequent trip?
    * Would the driver ignore the coupon entirely?
        * What if the coupon was for a bar instead of a restaurant?
        * What about a coffee house?
    * Would the driver accept a bar coupon with a minor passenger in the car?
        * What about if it was just you and your partner in the car?
    * Would weather impact the rate of acceptance?
    * What about the time of day?

After thinking through the questions, we started by understanding the shape of the dataset, which houses 12684 records and 26 features. No obvious numerical correlations were observed but the ouput of the pairwise correlation of columns did show an interesting positive correlation between accepting coupons and temperature. The output of this initial correlation can be accessed under the [Exploration Section](http://localhost:8888/notebooks/Customers_and_Coupons_Acceptance_Analysis.ipynb#Data-Exploration) of the included Jupyter notebook.

## Data Sanitation
No null values were detected but we did have missing/problematic data brokend down as follows:
```
car                     12576
Bar                       107
CoffeeHouse               217
CarryAway                 151
RestaurantLessThan20      130
Restaurant20To50          189
```
The car missing data was calculated to be ~99% missing of the total dataset records and keeping it was definitely not going to be appropriate. Also, the non Nan records for the car feature were less than 1% (approximately .85%) of the total records. At that small %, the car feature data was determined to be a good candidate for deletion. A summary of the decisons is listed on the following sections.

### The Decisions
To facilitate analysis of the data the following decisions were made to deal with the missing data:

1. Drop the car data from the dataframe. At approximately 99.15% it's too much data missing.
2. For the Bar coupon use the most common value to fill-in the NaN entries. The most common value per the modal is 'never'. At ~.84% missing data percent this didn't seem to make much of a difference in the analysis.
3. For the CoffeHouse there was a balanced distribution for frequency of visits per month. Decided to use use the modal output to replace the missing results. The modal output for this one is 'less1'.
4. For Restaurant20To50, CarryAway, RestaurantLessThan20 decided to not replace the missing values but consider labeling as "no_visit_frequency_specified" if it assists the analysis as we proceed.
5. Rename Y column to "CouponAccepted" using the same boolean values: 1 (accepted) and 0 (not accepted).
6. Lowercase column names since we have a mixture of camelCase, snake_case, PascalCase naming convention.

The implementation of each decision can be accessed on the [implementing decisions section](http://localhost:8888/notebooks/Customers_and_Coupons_Acceptance_Analysis.ipynb#Implementing-the-decisions) of the Jupiter Notebook included on this directory.

### Data Analysis and Observations
Once the data was sanitized we started the analysis and had the following observations:

[General Obserations]
* The proportion of the total observations that choose to accept the coupon was calculated to be ~56.84%. 
* We used a Seaborn barplot to see a distribution of the total counts per coupon type. The "Coffee House" coupons reported the highest total count at 3996, 1995 of which was calculated to have been accepted.
* A Seaborn countplot was also utilized to get the total acceptance counts by coupon type and we could see that both the "Coffee House" and "Restaurant(<20)" had the highest coupon acceptance counts.
* We used a bar plot to understand the proportion of coupons accepted in relation to the temperature and discovered that at high temperatures (i.e. 80s) we see higher acceptace coupon rates. An acceptance rate of ~51.47%.

[Bar Coupon Observations]
* Generated a new dataframe to analyze the "Bar Coupons" feature and uncovered that ~41.0% of the bar coupons were accepted, while ~51% were not.
* Grouping the frequent vs infrequent bar visitors revealed the expected. The percentage of coupon acceptance, for the coupons "Bar" feature is higher for frequent bar visitors than non-frequent visitors who have also accepted the coupon.
*  Using a bar plot we can also see that that drivers who never or rarely go to a bar don't accept the coupon. Interestingly enough the people who go 3 or less times a month tend to accept the coupons at higher proportions when comparing them to the other frequent bar visitors (those who go >= 4 times a week). 
* Trends and calculations revealed that the acceptance in drivers who go to a bar more than once a month and are older than 25 years of age is higher at ~69.5% compared to the not older than 25 not going to bars as frequently, whose acceptance rate is at ~39.3%.
* The acceptance rate for drivers who go to bars once a month, have no kids as passangers and don't hold a "farming, fishing or forestry" occupation is calcuated at ~71%.
* The data also revealed that the acceptance rate for drivers under 30 years of age, with no kids and who frequent the bar once a month have the highest acceptance rates at ~72%.


### Next Steps
* Continue exploring the "Coffee House" and the "Restaurant(<20)" as they reported the highest **total** counts for acceptance rates. We may be able to uncover good insights on what influenced the drivers who received those coupons to accept them.
* Create other visualizations to summary the observations for each of the aforementioned features.



## Sources 
The data for this analysis came from [uci.edu machine learning archive](https://archive.ics.uci.edu/ml/datasets/in-vehicle+coupon+recommendation#).

