# System recommendation from Expedia Hotel

## Table of Contents
- [Project Overview](#project-overview)
- [Problem Statement](#problem-statement)
- [Dataset Description](#dataset-description)
  - [Data Source](#data-source)
  - [Data Overview](#data-overview)
  - [Data Dictionary](#data-dictionary)



## Project Overview
This project dives into the fascinating realm of customer behavior data from Expedia Hotels Website. It involves a comprehensive analysis of what customers are searching for, their interactions with search results (including clicks and bookings), or whether a search result corresponds to a travel package that includes a flight. The dataset covers the years 2013 through July 2014, with test data spanning from August to December 2014.

The primary objective of this analysis is to predict the hotel cluster that a user is likely to book. Expedia utilizes a hotel cluster, an in-house algorithm that groups similar hotels based on various factors such as historical pricing, customer ratings, and proximity to city centers. These clusters are invaluable for predicting user preferences when booking hotels. It is important to note that the dataset contains 100 distinct hotel clusters. This predictive goal requires anticipating a user's booking outcome (hotel cluster) based on their search and related event attributes.

## Problem Statement
The problem we aim to address is the typical hotel search experience where random hotels are displayed in a user's chosen area. This project seeks to enhance user experiences by recommending hotels that align with the preferences and behaviors of users with similar profiles and based on the user's past search history, providing a more tailored and convenient hotel booking experience.

Both Expedia and customers stand to benefit from this prediction model. Customers will find it easier to identify hotels that match their preferences and will be more likely to use the Expedia platform regularly. This, in turn, can lead to increased revenue for the company as customers book more hotels due to the improved user experience.

## Dataset Description
The dataset used in this project is sourced from Kaggle. It does not represent the overall statistics of all Expedia data but is sampled for analysis due to its substantial size. As this problem involves time series data, the dataset is partitioned into a training dataset (2013 to July 2014) and a test dataset (August to December 2014) for model validation after the prediction.

One notable characteristic of this dataset is the absence of categorical columns; all variables are stored numerically. The data provide insights into customer interactions on the website, whether they booked a hotel or simply clicked on one, the time they searched for a hotel, and the duration of their trip.

### Data Source
The dataset was collected from Kaggle, and it is publicly accessible at  https://www.kaggle.com/competitions/expedia-hotel-recommendations/data?select=test.csv. You do not require specific permissions to access the data; a Kaggle account is sufficient.

### Data Overview
This project uses a sample from the Kaggle dataset to explore customer behavior on Expedia's platform. The dataset contains a training set from 2013 to July 2014 and a test set from August to December 2014 for model validation. Pre-processing and cleaning are performed to ensure data quality and relevance.

### Data Dictionary
| Column name |Description	Data| Type |
|----------|----------|----------|
|  date_time |	Timestamp when the customer made the interaction in the website	| string|
| posa_continent	| ID of continent associated with site_name	| int |
| user_location_country	| The ID of the country the customer is located	| int |
| user_location_region	| The ID of the region the customer is located	|int|
| user_location_city |	The ID of the city the customer is located	|int|
|orig_destination_distance | Physical distance between a hotel and a customer at the time of search. A null means the distance could not be calculated	double
user_id	ID of user|	int|
| is_mobile	| 1 when a user connected from a mobile device, 0 otherwise	tiny|int|
|is_package|	1 if the click/booking was generated as a part of a package (i.e. combined with a flight), 0 otherwise|	int|
|channel|	ID of a marketing channel	|int|
|srch_ci	|Checkin date	|string|
|srch_co|	Checkout date	|string|
|srch_adults_cnt|	The number of adults specified in the hotel room|	int|
|srch_children_cnt|	The number of (extra occupancy) children specified in the hotel room	|int|
|srch_rm_cnt	|The number of hotel rooms specified in the search	|int|
|srch_destination_id|	ID of the destination where the hotel search was performed	|int|
|srch_destination_type_id	|Type of destination|	int|
|is_booking	|1 if a booking, 0 if a click	|tinyint|
|cnt|	Numer of similar events in the context of the same user session	|bigint|
|hotel_continent	|Hotel continent	|int|
|hotel_country|	Hotel country|	int|
|hotel_market|	Hotel market	|int|
|hotel_cluster|	ID of a hotel cluster	|int|

