# Stock Market Prediction 
This project focuses on utilizing concepts of Financial Engineering and Artificial Intelligence to train models that can predict stock for a given company and ideally configure the setup to do algorithmic trading. We use the Cross-Industry Standard Process for Data Mining (CRISP-DM) framework to organize the project.


## Problem Definition
In a statement,

> Given the characteristics and historical data trends for a given company stock, can we reliably predict the value of their stock?

In addition, we want to understand how to predict the return on investment as well as answer other questions such as the following:

* What features make a stock option a potentially high positive investment even when the selling company may be showing periods of downturn?
* What returns are more convenient for modeling the movement of stock prices?
* What constant return would one have to get everyday in order to achieve the same final price?
* Why does the stock price go up and down?

## Executive summary

### Rationale
The main motivation behind this project was to understand how to utilize the concepts learned during the course (Machine Learning and Artificial Intelligence) and apply them in conjunction with Financial Engineering concepts to do stock prediction and apply the learnings to build strategies for algorithmic trading. For context, the trend in the stock market is leaning heavily towards algorithmic trading. According to a [2020 report](https://www.sec.gov/files/Algo_Trading_Report_2020.pdf) from the U.S. Securities and Exchange Commission more than 70% of trades in the US alone are being done by bots. It’s important to understand how this is done and use the knowledge as something to add to my current investment strategy.

## The Data
The data is retreived from Yahoo for the SP500 companies. The  list of companies came from [Kaggle](https://www.kaggle.com/camnugent/sandp500) and the dataset from the same location was utilized to understand the data. The dataset from Kaggle is outdated but is a good initial step to understand the financial data we will be dealing with. Later, we can recreate the dataset downloading recent financial data for all sp500 companies and filter just a handful (100 or so), which always includes those ones we may be interested to keep an eye on (e.g. NFLX, AAPL, TSLA, etc.).

#### Data Sources
* [Kaggle Stock Market Datasets](https://www.kaggle.com/datasets/aaron7sun/stocknews)
* [Historical Stock Market Dataset](https://www.kaggle.com/borismarjanovic/price-volume-data-for-all-us-stocks-etfs): Containing the daily prices and volume information surrounding US stocks and ETFs on the NASDAQ, NYSE, and NYSE MKT 
* [Stock Market Turnover Ratio](https://fred.stlouisfed.org/series/DDEM01USA156NWDB)
* [Yahoo Finance](finance.yahoo.com) to get updated historical data for all the SP500 companies.

## Methodology
The methods being used to answer our questions are:
* Linear Regression (baseline model)
    * Time series analysis
* Recurrent Neural Networks (RNN)
    * The shape of the input will be transformed to work with the RNN.
* Long Short Term Memory (LSTM) Neural Network 

## Results
We started by understanding the data we would be using to do the analysis. We then converted our time series data into 'datasets' and moved into the analysis & model evaluation. The results revealed that more complex models kine RNNs are not a proper approach to do stock predictions; in fact, they were completely inadequate at this task. Applying LSTM for this type of prediction was very deceptive. In trends, when the predictions seemed extremely accurate the models were just copying the most recent value. This discovery raised a huge flag with regards to online claims in blogs and courses, which state that neural networks perform almost accurately when doing stock predictions. LinearRegression (auto regressive models) did better at stock prediction but were outperfomed by the baseline model. Overall, the task of stock prediction (i.e. trends going up or down) is very, very challenging, especially when all we could gather from the data sources is the closing price. The stock price prediction is even harder especially when all we could gather from the sources is the closing price. Market trends are affected by a myriad other factors including emotions, social media, news, world-wide events and just general perceptions about a given company or their leadership; so it is very difficult to have all of this represented in datasets. In summary, stock price prediction is a very complex task.  Not attainable by just analysing the closing price from stock market sources (i.e. timeseries data) as was done with this exercise.

## Outline of project

- [Stock Prediction - DEA](https://colab.research.google.com/drive/16DvzTrbjleZcIR70-Z6vzkXosIVRKewc?usp=sharing)
- [Stock Prediction - Modeling ](https://colab.research.google.com/drive/1I9D8TwYrNFwBTMEhWkgF-5WprRPFQYxn?usp=sharing)

### More context on structure of this project
Before moving to the problem definition, this section provides details on the contents of this git repository.

| Item Name     | Description   |
| ------------- | ------------- |
| data/         | Directory containing the data set in .csv format. This data is also loaded in a google drive used by Colab, which are used by the Jupyter/Colab notebooks listed above.|
| README.md     | This file. |


## Next Steps
- Explore other techniques in Financial Engineering using AI to do algorithmic trading to evaluate a company's stock value for investment and be able to answer the following questions:
    * What returns are more convenient for modeling the movement of stock prices?
    * What constant return would one have to get everyday in order to achieve the same final price?
- Work on porfolio optimization, using algorithmic trading, as I learn new techniques
