## Overview:
We want to look at the nutrition of different foods, specifically looking at the difference in nutrition between “regular foods” and fast food. Regular food is defined as food without a fast-food label that presumably has better nutritional statistics. Fast food is food that can be prepared quickly to be sold in restaurants as a quick meal and has a label like “McDonalds” or “Wendys.”

## Research Question:
How can we distinguish between healthy and unhealthy foods? Are fast food items noticeably more unhealthy compared to the other foods? Are there particular nutritional components that clearly distinguish “regular foods” from fast food?

Our analysis will be guided by the questions listed above, framing our inquiries about the nutritional distinctions between fast food and “regular foods”. By exploring these questions, we aim to discover meaningful patterns and relationships across the various nutritional components in the datasets. Specifically, we strive to identify the five most influential nutritional components – such as calories, fat, sodium, sugar, and fiber, among others – that differentiate “regular foods” from fast food. Through our analysis, we aim not only to determine the factors that contribute most significantly to the differences between these two categories of food but also to gain a deeper understanding of their health implications. 

## Team Roles:

Luke Gauer: Helps organize meetings with the team outside of class to ensure assignments are completed on time. Will make sure that the work is spread evenly across all team members. 
Kirthi Ravichandran: Breaks down the organization of each part of the project to help make it into smaller digestible sections with a brief summary of each. 
Evan Ma: In charge of submitting project updates to GitHub, and looking over the finalized version of each part of the project to ensure effective completion.

## Datasets:

To begin our project, we will examine three different datasets that contain information on the nutritional components of various food types. The names and links to each of the datasets are listed below:

Food Nutrition Dataset - https://www.kaggle.com/datasets/utsavdey1410/food-nutrition-dataset/data

food nutrition dataset - https://www.kaggle.com/datasets/shrutisaxena/food-nutrition-dataset

Fastfood Nutrition - https://www.kaggle.com/datasets/ulrikthygepedersen/fastfood-nutrition 

The first dataset, titled the Food Nutrition Dataset, was created by Utsav Dey on Kaggle. This dataset was created by scraping data from the Yazio.com website using the BeautifulSoup Python library. The files from the scraped data were then created using the Pandas, Seaborn, and Matplotlib libraries. This data is licensed under the CC0 Public Domain. This means that anyone can freely download, use, and edit the data without any restrictions, though it is good practice to provide a proper citation. The data in this dataset was last updated about a year ago. The dataset has 35 different features. These features include the name of the food, its caloric value, fat and vitamin contents, and finally a column that describes its nutritional density per calorie. This dataset also includes over 2,000 rows of data, each representing a different type of food. 

The second dataset, also titled the food nutrition dataset, differs slightly from the first dataset we are analyzing. Shruti Saxena created this dataset on Kaggle. The data within this dataset is taken from a database about the nutritional contents of food created by the USDA, the United States Department of Agriculture. However, the Kaggle page doesn’t have details about how the data was acquired from this source. Upon reviewing the licensure of this data, we found that the original author holds the copyrights to the data files. This means that we would need to contact the owner of the dataset in order to use it. The dataset itself comprises 48 features/columns, including the food category, a description of the food, and a detailed breakdown of its vitamin, protein, and fat components. This dataset contains over 7,000 rows. Similar to the previous dataset, each row represents a distinct food and all its nutritional components. 

The third and final dataset we will analyze as part of this project is titled "Fastfood Nutrition" and was created by Ulrik Thyge Pederson on Kaggle. According to the Kaggle page, the data was taken from data.world API, but did not include any direct links to the source itself. The data has not been updated since it was initially uploaded to Kaggle three years ago. This dataset is licensed under Attribution 4.0 International (CC BY 4.0,) which essentially means that we can use, share, and adapt any of the data, but we must attribute the data to its original source. The data itself has 17 features, including the item name, the restaurant, and basic nutritional information such as the calories, sodium, and fats. This dataset is significantly smaller than the previous two datasets, as it only has 500 rows. 

## Timeline:

We plan on meeting every week to have checkpoints on our work. We will work individually, each of us working on our individual roles and tasks. For the weekly meetings, we plan on reviewing the work we did and planning next week’s work, similar to an Agile sprint. 

Our goals are to complete the project at least a day before the due date for both the interim status report and the final deadline. 

Week 6: Complete project plan

Week 7: Look into the dataset statistics, create basic EDAs and statistics, and clean the dataset. Also, research the data source and how it was obtained. Map out a project workflow. Evan will clean the data, Luke will research the data source, and Kirthi will organize everything in a concise way. 

Week 8: Find ways to integrate datasets together. Use research papers or other projects for inspiration. Keep a work cited containing all sources

Week 9: How does data relate to the thesis, and how can we back up some claims

Week 10: Complete interim status report

Week 11: Attempt to integrate the datasets and create some analysis. Get supporting evidence for the claims.

Week 12: Finalize dataset integration, organizing the dataset to be easily analyzed using SQL and Python. 

Week 13: Create visualizations for more supporting evidence and check data integrity

Week 14: Create documentation on how to replicate our work 

Week 15: Rerun all scripts and code sections to make sure they run well 

Week 16: Complete the final project 

## Constraints:

Data Structure Differences:

Since the datasets come from different sources, the features and units don’t align perfectly. This will require us to work on standardizing column names, serving sizes, and nutrient measurements to make sure everything lines up before we make any comparisons. 

## Data Reliability:

Because some of the data is web-scraped or user-uploaded, there may be missing values or inconsistencies in the recording of each nutrient. These gaps could alter the overall quality and accuracy of our findings. 

Health Classification Ambiguity:

We have to identify exactly what is considered healthy or unhealthy when making our claims which could be difficult considering so many nutrient factors go into every food. Establishing a fair way to classify foods could be subjective and may impact how our final model interprets the results. 


## Gaps:

Dataset Integration Plan:

We still need to find the most efficient way to combine the datasets, especially since each one uses different column names and formats. This step is essential before we start our actual in depth analysis. 

## Category Labeling:

We have to define a definition for “regular food” vs. “fast food” and a consistent rule for labeling foods across datasets to ensure our comparisons are accurate. 

## Analytical Approach:

We haven’t selected specific analytical methods yet to identify the top nutritional factors so we still have to work on that. Once we get more familiar with the datasets, we will decide on what approach we want, such as clustering or statistical tests. 

## Measuring Health Differences:

We haven’t determined how to quantify “healthiness” yet in a measurable way. This decision will influence how we look at and interpret our findings later on. Such techniques could be to use a scoring system or nutrient ratio analysis. 
