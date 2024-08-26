
# Handling Missing Data in the Weather Forecast Dataset

## Problem Description
-**The dataset provided for weather forecasting contained missing values in the severerisk and precip columns.**
-**Missing data can compromise the accuracy of machine learning models and lead to biased or incomplete predictions.**
-**Therefore, it was crucial to handle these missing values effectively.**

## Analysis Goals

The following aspects of the data that are missing need to be filled:

- **severerisk**: The risk level for severe weather events.
- **precip**: The amount of precipitation (rainfall) recorded.


## How to solve the problem

I employed a **Random Forest Regressor** to predict and fill in the missing severerisk values.

This approach leverages the relationships between **severerisk** and other related features in the dataset, such as:
 **tempmax**, **tempmin**, **temp**, **humidity**, and **precip**.

Higher maximum temperatures and humidity levels might correlate with a higher severerisk.

Precipitation can also impact severe weather risk.

I trained the model on the subset of data where severerisk values were available. This allowed the model to learn patterns and associations between the known features and the **severerisk**.

After training, I used the model to predict **severerisk** values for rows where this data was missing. These predictions were then used to fill in the missing values.
