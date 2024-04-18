

# Introduction

## Problem exposition and Business Value

Marketing Campaigns can be considered a call to action for customers and they can be of any kind. For example, they can involve giving customers a discount, giving customers something for free, collecting points on a membership card, offering free delivery, offering additional credit and so on.

Regardless of the exact nature of any campaign, what is important is that different types of customers respond differently to different types of campaigns; customers in a specific segment may respond well to one campaign and poorly to another.

By finding out in advance what customer segments are more likely to respond well to a given marketing campaign, we can target those customers. This will encourage a higher conversion percentage and, ultimately, higher profitability.

Therefore, this analysis is aimed at finding 

- different customer segments for this particular campaign
- which segments responds well and which do not
- conversion percentages and associated profitability for each customer segment, broken down by customer characteristics such as income, living arrangements, monthly amount spent on meat products and more
- clusters within this customer data so that subsequent marketing campaigns can target customers more effectively

In this case, our marketing campaign offers a discount on certain products to customers. The cost per customer of such a campaign is $3 while a successful conversion results in a per-customer revenue of $5.


## Data

**Data source**: This data is obtained from [Kaggle](https://www.kaggle.com/datasets/rodsaldanha/arketing-campaign), is provided by user [Rodolfo Saldanha](https://www.kaggle.com/rodsaldanha) and can be found in the Git repository

**Observations**: It contains 2216 observations where each observation represents a customer who converted or did not convert

**Features**: There are 35 features in total with a mix of interval and categorical data types. A few examples are:

- Complain - 1 if customer complained in the last 2 years

- DtCustomer - date of customer’s enrolment with the company

- Education - customer’s level of education

- Marital - customer’s marital status

- Kidhome - number of small children in customer’s household

- MntMeatProducts - amount spent on meat products in the last 2 years

- MntFruits - amount spent on fruits products in the last 2 years

- NumStorePurchases - number of purchases made directly in stores

- NumWebPurchases - number of purchases made through company’s web site


**Outcome variable**: The outcome variable is called Response it is 1 if customer accepted the offer in the last campaign and 0 otherwise


# Approach and Insights

## Data Cleaning

The dataset is fairly complete with only 24 values missing for the 'Income' variable. These rows were subsequently dropped because the loss in data is miniscule. A check for extreme values highlighted 3 customers whose ages were 121, 115 and 114. These values seemed very unlikely but I did not remove them as, again, they represent only a vanishingly small proportion of the data\

On the whole, the dataset is fairly clean.

## EDA and Key Findings

For EDA, I chose a select number of features to explore their relationship with the outcome variable (Response) and the profitability of the customer segments represented. 

Here are the key findings:

- The marketing campaign (MC) had a moderate overall conversion rate of 15%:


![](images/overall_conversion.png)

- The total loss incurred by the MC was $2,985 so it was a significantly unsuccessful MC overall

- The highest income earners had the greatest number and percentage of conversions, with the highest 2 income deciles having conversion percentages of 39.19% and 21.27% respectively:


![](images/income_conversions.png)

- Customers in only the highest income decile were associated with profitability, when segmented by income:

![](images/income_profitability.png)


- When segmented by age, all customer groups were associated with losses apart from those in the 80-120 group, which broke even:

![](images/age_profitability.png)

- When segmented by education level, all customer groups were associated with losses 


![](images/education_profitability.png)


- When segmented by living arrangements, customers who lived alone (without spouses or children) were associated with profitability. Those who lived with spouses or children were associated with heavy losses

![](images/living_profitability.png)

- This was unsurprising as the conversion rate of customers living alone was nearly 4 times the conversion rate of their counterparts


![](images/living_conversion.png)


- When segmented by the length of time an individual had been a customer of our company, our 'oldest' customers tended to have the greatest conversion rates

![](images/length_conversion.png)


# Clustering

I used the elbow method to find out the optimal number of clusters to choose with K-Means Clustering, which turned out to be 4

![](images/elbow.png)

Interestingly, a single cluster (cluster 2) contained contained all 333 customers who converted. These customers:

- Have the greatest average income at $60209

- Have 3 teens per 10 homes on average. So while these customers are not completely teen-less, they tend to live with fewer teens on average than customers in other clusters [specifically Cluster 3 (about 7 teens per 10 homes) and Cluster 2 (more than 1 teen per home)]

- Spent the most on wine in the last 2 years at $502

- Spent the most on meat products in the last 2 at $294

- Spent the second most on gold products in the last 2 years a $61, with customers in Cluster 3 spending the most ($66)

- Make the most purchases through catalogues at 4.2. The frequency of purchase is not listed in the meta information of the dataset, but it is reasonable to assume in the absence of information that points otherwise that this frequency is monthly

- Make the most purchases through the Web at 5. Again, this is assuming a monthly figure

- Are usually among our oldest customers (in terms of how long they've been with the company, not their Age), with an average of 449 days since their first purchase. However, they are not the 'oldest' group of customers. Those belong to cluster 3 which, it should be reiterated, did not have a single customer convert


# Conclusions

The overall conclusion seems to be that our wealthiest, highest-spending, longest-tenured customers who live alone respond best to this type of marketing campaign. This suggests that for future iterations of this campaign, only these customers should be targeted.
