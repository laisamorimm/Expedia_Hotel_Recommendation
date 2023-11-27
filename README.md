# System recommendation from Expedia Hotel

## Table of Contents
- [Project Overview](#project-overview)
- [Problem Statement](#problem-statement)
- [Dataset Description](#dataset-description)
  - [Data Source](#data-source)
  - [Data Overview](#data-overview)
  - [Data Dictionary](#data-dictionary)
- [Project Organization](#project-organization)
  - [Flowchart](#flowchart)
  - [Baseline Models](#baseline-models)
  - [Model Selection](#model-selection)
- [Conclusion](#conclusion)




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

### Data findings
In the course of this project, several noteworthy findings emerged, shedding light on user behaviors and preferences within the Expedia Hotels Website dataset:

In both 2013 and 2014, the website experienced interaction peaks in March, July, and October. These periods signify a noticeable surge in user engagement, suggesting a growing interest in hotel-related activities. Notably, 2014 witnessed a significant uptick in website traffic compared to the previous year. The median distance between the origin and destination points is approximately 1168.39 miles. This insight provides a glimpse into the average travel distances customers are interested in, potentially influencing the recommendation of hotels within a specific radius. A predominant number of users access the website from non-mobile devices. This emphasizes a substantial interest in hotel searches via traditional platforms, highlighting the need for an optimized desktop experience. User booking preferences lean towards one-day stays for two people, with a notable trend of starting these stays on Sundays. Understanding such patterns is crucial for tailoring recommendations and improving the overall user experience. Only 8.71% of user interactions culminate in actual bookings. This metric underscores the importance of refining recommendation models to increase conversion rates and improve the platform's effectiveness. These insights provide a foundation for further analysis and model development, enabling the creation of more personalized and effective hotel recommendations for Expedia users.


### Data Dictionary
| Column name |Description	Data| Type |
|----------|----------|----------|
|  date_time |	Timestamp when the customer made the interaction in the website	| string|
| posa_continent	| ID of continent associated with site_name	| int |
| user_location_country	| The ID of the country the customer is located	| int |
| user_location_region	| The ID of the region the customer is located	|int|
| user_location_city |	The ID of the city the customer is located	|int|
|orig_destination_distance | Physical distance between a hotel and a customer at the time of search. A null means the distance could not be calculated	|double|
|user_id	| ID of user|	int|
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

## Project Organization

### Flowchart
Beginning with data collection, the process unfolds through essential stages such as data preprocessing, exploratory data analysis (EDA), and the implementation of baseline models, including Random Cluster Selection, Logistic Regression, KNeighbors, and Decision Tree

### Baseline Models
For the initial phase, I've selected four baseline models to kickstart the analysis. These models include:
- **Random Cluster Selection**
- **Logistic Regression**
- **KNeighbors**
- **Decision Tree**

### Model Selection
For model selection, the following considerations were made:
- **Random Cluster Selection:** Served as a basic benchmark to compare against other models.
- **Logistic Regression:** Chosen for its simplicity, adaptability to non-linear decision boundaries, and interpretability.
- **KNeighbors:** Selected for its ability to handle classification tasks based on proximity in the feature space and versatility in capturing complex patterns.
- **Decision Tree:** Employed due to its versatility in handling both classification and regression tasks, interpretability, and the optimization of hyperparameters using GridSearchCV.

Insights gained from baseline models and exploratory data analysis were instrumental in guiding the selection process. Further details on model evaluations and comparisons will be included in subsequent sections.

## Conclusion:

This project centers on elevating the user experience on Expedia's platform through the prediction of hotel clusters. Following an exploration of diverse baseline models such as Random Cluster Selection, Logistic Regression, KNeighbors, and Decision Tree, the latter emerged as the standout performer, seamlessly combining adaptability and interpretability. Further enhancing the Decision Tree's efficacy, the project delved into hyperparameter tuning, resulting in noticeable improvements. The project's success with the Decision Tree underscores its aptness for the task. The iterative nature of the project ensures continuous refinement, aligning with the overarching objective of providing precise and tailored hotel recommendations on Expedia's platform.
