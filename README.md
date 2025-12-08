# IS477 Final Project: Fast Food vs. Regular Food Health Analysis

Software: Python 3.10+, Snakemake, Pandas
Date: December 2025
Software: Python 3.11+, Snakemake, Pandas

## Contributors
*   Luke
*   Evan
*   Kirthi

## Project Summary

### Overview
Overview:
This project investigates the nutritional disparities between "regular foods" and "fast food" to understand the quantitative differences in their health profiles. For the purpose of this study, we define:
Regular Food: Food items found in standard nutritional databases (e.g., USDA) without specific fast-food branding, presumably representing raw ingredients or home-cooked standard meals.
Fast Food: Food items prepared quickly, sold in commercial chain restaurants (e.g., McDonald's, Wendy's"[Wendy's](https://www.wendys.com/)"), and specifically labeled as such in nutritional datasets.
Research Questions:
Our analysis is guided by the following core inquiries:
How can we quantitatively distinguish between healthy and unhealthy foods using exploratory data analysis (EDA)?
Are fast food items noticeably more unhealthy compared to regular foods when normalized for portion size?
Are there specific nutritional components that clearly distinguish regular foods from fast food?

Goals:
We aim to discover meaningful patterns and relationships across various nutritional components in our datasets. Specifically, we strive to identify the five most influential nutritional components—such as calories, fat, sodium, sugar, and fiber—that differentiate regular foods from fast food. Through this analysis, we aim not only to determine the factors that contribute most significantly to the nutritional gap between these categories but also to gain a deeper understanding of their potential health implications.

Significance: 
The motivation behind our study is to provide a data-driven perspective on dietary quality by comparing fast food and regular food. By identifying patterns across core nutrients, our analysis informs discussions about dietary choices and possible policy interventions needed if we find anything very jarring. The approach helps prioritize transparency, reproducibility, and the ability to allow for future researchers to test the generalizability of findings beyond the initial scope. 

Our initial expected findings: 
We anticipated that fast food would exhibit way less healthy ingredients and higher energy density and higher sodium and sugar content on average, even after adjusting for portion size. We also believed that nutrients like fiber would be lower in fast food due to food processing and commonplace formulation practices. Our initial interpretation focuses on the scale of observed gaps across datasets and how these gaps translate into practical implications for guidance regarding diet and consumer awareness. For this, we created visualizations and quantitative summaries to convey our findings clearly and support transparent conclusions. 

Limitations + Ethical Considerations:
Explicit limitations have been acknowledged, including representativeness of datasets, potential misclassification between regular and fast food items, and how generalizable of findings beyond the sampled data. Our ethical considerations will cover data licensing, usage rights, and the responsible interpretation of nutritional claims to avoid overstating specific health implications. Clear communication will accompany any caveats to prevent misinterpretation by non-specialist audiences.

Next Steps:
For our project we aim to deliver a transparent and reproducible analysis that  portrays the gaps in nutritional value between regular and fast foods. If initial results reveal robust nutrient-driven separations, future work could extend the analysis to regional dietary patterns or demographic interactions and more. This could help further address more nutritional gaps. This overall summary shows a path toward more practical impact while maintaining our rigorous documentation and an accessible narrative. 

## Data Profile
For our project, we combined data from three different sources in order to develop a comprehensive understanding of the nutritional landscape. We acquired all our data through Kaggle. Each of our datasets contains various information about types of food, and in combining them, we strove to create a dataset that provides complete information that can be used to make a holistic assessment of the health implications associated with different foods.

Our first dataset was titled “[Fast Food Nutrition](https://www.kaggle.com/datasets/ulrikthygepedersen/fastfood-nutrition)”. This Kaggle dataset contains the nutritional breakdown of menu items from many well-known fast-food restaurants. The data includes information about the food’s calories, fat, and sodium, among other components. Ulrik Thyge Pederson created this dataset on Kaggle. To ensure the authenticity of the data, we looked into Pederson’s background and the origins of the information in the dataset. We found that Pederson is a data scientist based in Denmark. While his lack of credibility was of concern to us, we looked into the data’s origins to determine its trustworthiness. We found that the data was data.world API, but were unable to find any direct links to the data source itself. Additionally, we noticed that the data doesn’t get updated regularly. There hasn’t been a single update to the dataset since its initial release 3 years ago. Before we began using this data, we looked into the licensing to ensure that we were using it correctly. We found that this dataset is licensed under Attribution 4.0 International (CC BY 4.0). This license allows anyone to access, use, adapt and share the data as long as the data is attributed to its original source. 

Our second dataset was titled “[USDA Food Data](https://www.kaggle.com/datasets/shrutisaxena/food-nutrition-dataset)”. This dataset contains nutritional information about standard food items that are commonly consumed in the US. Throughout our project, we used this data as the baseline for “regular food”. Similar to our first dataset, this one also contains information about the nutritional components of different foods. This dataset is hosted on Kaggle and was created by Shruti Saxena four years ago. This dataset has not been updated since its initial release. However, the data was taken directly from the USDA (the United States Department of Agriculture). While the Kaggle page attributes the data to this source, it lacks a description of how the data was acquired from the USDA. Upon reviewing the data licensure, we found that the data also falls under the CC BY 4.0, meaning that we can freely download, use, adapt, and share it. However, we must attribute the data to the original source.

Our third and final dataset was titled “[Yazio Food Nutrition](https://www.kaggle.com/datasets/utsavdey1410/food-nutrition-dataset)”. Once again, this was a dataset that we found on Kaggle that provides the nutritional information for a wide array of groceries that can be found at traditional supermarkets. We used the data in the dataset to supplement the information from the USDA food dataset. This dataset was created by Utsav Dev. The data was scraped from yazio.com, using the BeautifulSoup Python library. Once the data was scraped, the files were processed using the Pandas, Seaborn, and Matplotlib Python libraries. This dataset is licensed under the CC0 Public Domain License. This essentially means that anyone can freely download, edit, and publish this data. However, correctly citing the data ensures proper data use practices, even though it isn’t required. 

As none of the three datasets contain any personally identifiable information (PII) or confidential information, we don’t need to worry about data anonymization. Similarly, from an ethical and legal perspective, we are able to use the data hosted on Kaggle because they are under different types of open licenses. Similarly, during the data acquisition process, we adhered to the terms of use for the Kaggle API. 

As we worked on this project, we were conscious of following the USGS Science Data Lifecycle model. In doing so, we strive to ensure reproducibility in our work. Before we began, we created an initial plan for our project. We defined a set of research questions on health disparities and their relationship to food groups. Then we began the data acquisition process. We used the Kaggle API "[Kaggle API](https://www.kaggle.com/docs/api)" to download our datasets programmatically. We used the SHA-256 hash verification to ensure data provenance. Then we began cleaning the data and harmonizing the column names across the three CSV files to create a unified schema. As a part of that process, we normalized the data to “per 100 calorie” densities to ensure that our comparisons were fair. During the analysis, we conducted basic exploratory data analysis (EDA) using Python. We specifically used the Pandas and Seaborn libraries to visualize the distribution and correlations of different variables. Finally, we focused on preserving and publishing our work. To do this, we documented all our entire workflow using Snakemake and a series of Jupyter Notebooks. In doing so, we are able ot ensure that all the analysis can be replicated by future researchers.

## Data Quality
To determine the quality of the data, we assessed in using the four data quality dimensions - accuracy, completeness, consistency, and timeliness. When looking at our first dataset, the fast food data, we verified the accuracy of the values within it by comparing them to publicly available records for a few of the restaurants to identify any inconsistencies. This dataset contains the nutritional information for different menu items at fast food chains, and oftentimes, the nutritional components of these foods are available online and are often published by the fast food chains themselves. For example, one of the items in the dataset is the Artisan Grilled Chicken Sandwich. We then found McDonald’s "[McDonald's](https://www.mcdonalds.com/us/en-us.html)" Nutrition Calculator, which is freely available online. We observed that the calorie count, protein value, and total fat were consistent across the two sources and concluded that the information in our Kaggle dataset for that item was likely reliable. We selected 15 items from the dataset across a range of fast-food chains to verify using this method. After completing this process multiple times and finding consistent values, we deemed the data in this dataset accurate. After we determined that the data was accurate, we began investigating its completeness. In doing so, we found missing values in 5 different features (fiber, protein, vitamin A, vitamin C, and calcium). Although certain features in some of these instances were missing, we still felt that the remaining data for those instances was valuable. Rather than eliminating all the cases with NA values, we replaced the missing values with the median value of that feature so that we could continue using those data points. After we accounted for the gaps in the data, we began analyzing it for consistency. As we began analyzing and examining our data, we didn’t identify any gaps in the semantic rules. None of the columns had significant outliers, which would have indicated data inconsistencies. Additionally, there were no data values that violated the schema rules. Finally, we began to investigate the timeliness of the data. As all of this data pertains to food, it is unlikely to change drastically over time. All of the datasets we used were created in the last 5 years. Additionally, as our main investigational questions focus on identifying key differences between fast food and regular food, we felt it was acceptable if our data didn’t reflect minor changes resulting from more recent fast-food menu item modifications, as these wouldn’t significantly impact our findings. 

We repeated this process for both the USDA and Yazio datasets and deemed them accurate, consistent, and timely. While the Yazio dataset didn’t have any missing data, the USDA dataset had two features that had missing values. These features were the Data .Household Weights.1st Household Weights Description and the Data.Household Weights.2nd Household Weights Description. Using the same logic and process as above, we replaced all NA values with the feature's median across the dataset. We understand that this may not accurately represent the data that belongs in that feature, but we also determined that the missing value didn’t convey any information about the instance. Once we filled in the missing values of the USDA dataset, we completed our data quality validation and deemed them fit for use during our analysis process.


## Findings
From our integrated analysis of the fast food, USDA, and Yazio datasets, we noticed consistent and substantial nutritional differences between fast food and regular foods, especially when nutrients are normalized per 100 calories. After cleaning all three sources to a unified schema (Name, calories, total fat, saturated fat, sodium, sugar, fiber, protein, type), the combined dataset contained 8,455 items, clearly labeled as fast food or regular food for side-by-side comparison. This structure enabled both per-serving and per-100-calorie analyses, which helped us ground our findings about “healthiness” in complementary perspectives. 

In terms of calories per serving, fast food items cluster around a higher mean calorie count and display a right-skewed distribution driven by a few very high-calorie outliers. The highest-calorie fast food items are large sandwiches and burgers that exceed many regular foods by several hundred calories per serving. In contrast, the most calorie-dense regular foods tend to be nuts and oils, but they coexist with a long tail of low and moderate-calorie items, resulting in a more balanced overall distribution. This confirms that fast food disproportionately contributes to high calorie intake even before portion size normalization, which helps answer some of our initial guiding questions. 

Our distribution plots of key nutrients show that fast food typically occupies higher ranges for total fat, sodium, and calories while regular foods show greater variability with many low-end values. Our boxplots by Type indicate that fast food has higher interquartile ranges for calories and fat, whereas regular foods span from very low fat items to high fat.  

Within fast food, savory entrees often have moderate sugar density while beverages elevate the overall sugar profile, making a simple fast food equals more sugar conclusion not as reliable. Protein behaves similarly as within the USDA dataset regular foods average about 10.8 grams of protein, with a right skewed distribution while fast food items offer moderate protein that does not distinguish healthiness.

We created correlation heatmaps "[What is a heatmap?](https://www.optimizely.com/optimization-glossary/heatmap/#:~:text=A%20heatmap%20is%20a%20graphical,web%20pages%20or%20webpage%20templates.)" to clarify how much nutrients move in a similar way within each category. For fast foods, calories, total fat, and sodium tend to be positively associated, indicating formulations where energy density and fat rise together in the same items. In regular foods, correlations are more spread with high calorie items not always being very high in sodium or saturated fat, and nutrient combos vary widely across categories such as fruits and grains. This suggests that while regular foods include unhealthy extremes, fast food more consistently occupies a small clustered, high-calorie, high-fat, and high sodium region of the nutritional space. 

Across all analyses, the most important components distinguishing fast food from regular food are total fat, sodium, fiber, calories and sugar. Sodium emerges as the clearest differentiator with fast food showing a higher sodium to calorie ratio, making sodium density a strong market of fast food like profiles. Sugar and protein add more nuance rather than providing clean separation which highlights no single metric fully captures the healthiness. 

Overall, the findings confirm that fast food is less healthy than regular foods on core nutritional indicators when evaluated on a per calorie basis. Some regular foods can be calorie dense or high in specific nutrients, and variables like cholesterol or sugar by themselves are not reliable health proxies. High sodium and fat, low fiber, and elevated per serving calories most strongly characterizes fast food relative to regular foods in the integrated dataset. 


## Future Work and Lessons Learned
Lessons Learned
Throughout the lifecycle "[8 Steps In the Data Lifecycle](https://online.hbs.edu/blog/post/data-life-cycle)" of this project, our team navigated the complexities of transforming raw, heterogeneous data into actionable nutritional insights. While the results provided clear distinctions between fast food and regular food, the process itself yielded valuable lessons regarding data engineering workflow and tooling.

The Shift to Literate Programming
One of the most significant pivots in our methodology was the transition from standalone Python scripts (.py files) to Jupyter Notebooks. Initially, our workflow relied on executing scripts via the command line to generate static image files of graphs. While functionally sound, this approach created a disconnect between the code, the underlying logic, and the visual output. By adopting Jupyter Notebooks, we embraced the paradigm of "literate computing." This allowed us to interleave narrative text, data cleaning logic, and immediate visual feedback in a single document. This shift drastically improved "visualization visibility"—the ability to instantly verify if a data transformation resulted in the expected visual distribution—and facilitated a more cohesive narrative structure for our findings.
The Importance of Schema Harmonization
Data integration proved to be the most labor-intensive phase of the project. We learned that "standard" nutritional data is rarely standard across different sources. The USDA dataset used specific keys like Data.Fat.Total Lipid, while the Fast Food dataset used total_fat. Furthermore, measurement units varied (e.g., milligrams vs. grams). We learned the critical importance of creating a rigorous Data Dictionary early in the project lifecycle. Future projects would benefit from creating an automated schema-mapping utility to handle these discrepancies more efficiently, rather than manual mapping.
Provenance and Automation
Finally, implementing Snakemake was a revelation in workflow management. In early iterations, we manually downloaded datasets, leading to version control issues and "it works on my machine" errors. By scripting the acquisition via the Kaggle API and wrapping the process in a Snakemake workflow, we ensured that the analysis was reproducible from scratch. This reinforced the lesson that reproducibility is not an afterthought, but a foundational requirement of data science.
Potential Future Work
While our Exploratory Data Analysis (EDA) successfully identified sodium density, fat consistency, and fiber content as key differentiators, this study serves as a foundational layer for more advanced inquiries. There are several promising avenues for extending this research.
1. Integration of Machine Learning Models
The logical next step in this analysis is moving from descriptive analytics (what the data looks like) to predictive analytics. Currently, we categorize food based on its source dataset. Future work could involve training a Binary Classifier (e.g., Logistic Regression, Random Forest, or Support Vector Machines) to predict whether an unlabelled food item is "Fast Food" or "Regular Food" based solely on its nutritional profile.
Feature Importance: Using tree-based models (like Random Forest or XGBoost) would allow us to mathematically rank feature importance. This would validate our EDA findings by quantifying exactly how much "Sodium per 100g" contributes to the classification of a food item as "Fast Food" compared to "Sugar."
Clustering Analysis: We could apply unsupervised learning techniques, such as K-Means Clustering or DBSCAN, to identify "unhealthy clusters" within the Regular Food dataset. This would help reveal foods that, while not sold at a drive-thru, share the same nutritional fingerprint as fast food (e.g., frozen processed meals), effectively identifying "ultra-processed" foods within standard grocery data.
2. Expanded Dataset: The Micronutrient Gap
Our current analysis focuses on macronutrients (Fat, Protein, Carbs) and major health indicators (Sodium, Fiber, Sugar). However, nutritional health is multidimensional. A diet high in protein but void of vitamins is still unhealthy. Future iterations of this project should incorporate Micronutrient Data.
Vitamins and Minerals: By integrating columns for Vitamin A, Vitamin C, Iron, Calcium, and Potassium, we could assess "Nutrient Density" more holistically. Fast food might track closely with regular food on calories, but we hypothesize it would show a severe deficit in micronutrients.
The "Hidden Hunger" Analysis: This expansion would allow us to explore the concept of "hidden hunger"—diets that are calorically sufficient (or excessive) but nutrient-poor. This distinction is vital for public health policy, as it shifts the conversation from simply "reducing calories" to "increasing nutrient density."
3. Natural Language Processing (NLP) on Food Names
The text data within the Item and Description columns remains largely untapped. Future work could employ Natural Language Processing (NLP) to analyze correlations between food descriptors and health metrics.
Semantic Analysis: Do words like "Crispy," "Loaded," or "Supreme" correlate statistically with higher trans-fats or sodium? Conversely, do "Fresh" or "Artisan" actually correlate with better nutritional profiles, or are they merely marketing terms?
Ingredient parsing: If ingredient lists can be scraped or acquired, we could analyze the complexity of the food matrix. Exploring the relationship between the number of ingredients and the health score of the item would likely show a strong negative correlation, offering another metric for distinguishing processed foods.

## Reproducibility
To reproduce this analysis, you must first configure the Kaggle API to download the raw data and then execute the Snakemake workflow.
1. Setting up the Kaggle API
To use the Kaggle API, you must install the library and authenticate using a token.
Step-by-Step Guide:
Install the Kaggle Library: Open your terminal and run:
pip install kaggle
Generate API Token:
Log in to your account at Kaggle.com.
Navigate to Account settings.
Scroll to the "API" section and click "Create New Legacy Token".
This will download a file named kaggle.json.
Authenticate: Move the file to the correct directory so the script can access it:
mkdir -p ~/.kaggle
mv ~/Downloads/kaggle.json ~/.kaggle/
chmod 600 ~/.kaggle/kaggle.json
2. Running the Workflow
Once the API is set up, you can run the entire analysis (acquisition, processing, and visualization) using the provided automation script:
Install Dependencies:
git clone https://github.com/Evimess/IS477_FInal_Project.git
Pip install snakemake
pip install pulp==2.7.0
pip install -r requirements.txt
Execute Workflow:
snakemake --cores 1 --forceall


The structure for the workflow: 
Main/
├── Snakefile
├── is477_analysis.ipynb
├── requirements.txt
└── scripts/
    └── acquire_data.py



## References
*   **Dataset:** Pedersen, U. T. (2023). *Fast Food Nutrition*. Kaggle.
*   **Dataset:** Saxena, S. (2023). *Food Nutrition Dataset*. Kaggle.
*   **Dataset:** Dey, U. (2023). *Food Nutrition Dataset (Yazio)*. Kaggle.
*   **Software:** Python Software Foundation. (2023). *Python Language Reference, version 3.11*.
*   **Software:** Waskom, M. L. (2021). *Seaborn: statistical data visualization*. Journal of Open Source Software, 6(60), 3021.
### Research Papers
Data Integration & Harmonization
Doan, A., Halevy, A., & Ives, Z. (2012). Principles of Data Integration. Morgan Kaufmann.
Presser, K., et al. (2010). Review of food composition data interchange and harmonization. Journal of Food Composition and Analysis, 23(6), 554-562.
Workflow & Reproducibility
Mölder, F., Jablonski, K. P., Letcher, B., et al. (2021). Sustainable data analysis with Snakemake. F1000Research, 10, 33.
Rule, A., Birmingham, A., & Zuniga, C. (2019). Ten simple rules for writing and sharing computational analyses in Jupyter Notebooks. PLOS Computational Biology, 15(7), e1007007.
Nutritional Analysis
Bowman, S. A., & Vinyard, B. T. (2004). Fast food consumption of US adults: impact on energy and nutrient intakes. Journal of the American College of Nutrition, 23(2), 163-168.

Food Nutrition Dataset - https://www.kaggle.com/datasets/utsavdey1410/food-nutrition-dataset/data
Food Nutrition Dataset 2 - https://www.kaggle.com/datasets/shrutisaxena/food-nutrition-dataset
Fastfood Nutrition - https://www.kaggle.com/datasets/ulrikthygepedersen/fastfood-nutrition

