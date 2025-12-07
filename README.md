# IS477 Final Project: Fast Food vs. Regular Food Health Analysis

## Contributors
*   Luke
*   Evan
*   Kirthi

## Project Summary

### Overview
This project investigates the nutritional disparities between "regular foods" and "fast food" to understand the quantitative differences in their health profiles. For the purpose of this study, we define:
*   **Regular Food:** Food items found in standard nutritional databases (e.g., USDA) without specific fast-food branding, presumably representing raw ingredients or home-cooked standard meals.
*   **Fast Food:** Food items prepared quickly, sold in commercial chain restaurants (e.g., McDonald's, Wendy's), and specifically labeled as such in nutritional datasets.

### Research Questions
Our analysis is guided by the following core inquiries:
1.  How can we quantitatively distinguish between healthy and unhealthy foods using exploratory data analysis (EDA)?
2.  Are fast food items noticeably more unhealthy compared to regular foods when normalized for portion size?
3.  Are there specific nutritional components that clearly distinguish regular foods from fast food?

### Goals
We aim to discover meaningful patterns and relationships across various nutritional components in our datasets. Specifically, we strive to identify the **five most influential nutritional components**—such as calories, fat, sodium, sugar, and fiber—that differentiate regular foods from fast food. Through this analysis, we aim not only to determine the factors that contribute most significantly to the nutritional gap between these categories but also to gain a deeper understanding of their potential health implications.

## Data Profile

### Datasets Used
We integrated data from three distinct sources to build a comprehensive view of the nutritional landscape. All data was acquired via Kaggle.

1.  **Fast Food Nutrition:** Contains nutritional breakdown (calories, fat, sodium, etc.) for menu items from major fast-food chains.
2.  **USDA Food Data:** A comprehensive database of standard food items, serving as our baseline for "regular food."
3.  **Yazio Food Nutrition:** A supplementary dataset providing nutritional values for a wide variety of grocery items.

### Data Lifecycle Management
This project follows the **USGS Science Data Lifecycle** model to ensure rigor and reproducibility:
*   **Plan:** Defined research questions regarding health disparities between food groups.
*   **Acquire:** Utilized the Kaggle API to programmatically download datasets, ensuring data provenance through SHA-256 hash verification.
*   **Process:** Cleaned and harmonized column names across three different CSVs into a unified schema; normalized data to "per 100 calorie" densities to allow for fair comparison.
*   **Analyze:** Performed Exploratory Data Analysis (EDA) using Python (Pandas, Seaborn) to visualize distributions and correlations.
*   **Preserve/Publish:** Documented the workflow via Snakemake and Jupyter Notebooks to ensure the analysis can be replicated by future researchers.

### Ethical and Legal Constraints
The datasets used are publicly available on Kaggle under open licenses (e.g., CC0: Public Domain or similar). No Personally Identifiable Information (PII) is present in nutritional data. We have adhered to the terms of use for the Kaggle API during the data acquisition phase.

## Findings
*(Note: Insert specific conclusions from your graphs here. Example below:)*

Our analysis highlighted clear distinctions between the two food groups:
*   **Sodium Density:** Fast food items demonstrated a significantly higher sodium-to-calorie ratio compared to regular foods.
*   **Fat Consistency:** Fast food items clustered tightly in high-fat ranges, whereas regular foods showed greater variance (ranging from low-fat fruits to high-fat oils).
*   **Fiber Content:** Regular foods generally contained higher fiber density, a key marker for "healthy" food, compared to fast food options.

## Future Work and Lessons Learned
Throughout this project, we learned that using **Jupyter Notebooks** significantly enhances the workflow compared to standalone Python scripts. Notebooks provide immediate visual feedback and allow for narrative text to sit side-by-side with code, increasing the "ease of visualization visibility" and interpretability of the data.

**Potential Future Work:**
*   **Machine Learning Integration:** While this project focused on EDA, future work could train a classifier to predict whether a food item is "Fast Food" or "Regular" based solely on its nutritional profile.
*   **Expanded Dataset:** Incorporating micronutrient data (vitamins and minerals) could provide a more holistic view of "healthiness" beyond macros.

## Reproducibility 

To reproduce this analysis, you must first configure the Kaggle API to download the raw data, and then execute the Snakemake workflow.

### 1. Setting up the Kaggle API
To use the Kaggle API, you must install the library and authenticate using a token.

**Step-by-Step Guide:**
1.  **Install the Kaggle Library:**
    Open your terminal and run:
    ```bash
    pip install kaggle
    ```
2.  **Generate API Token:**
    *   Log in to your account at [Kaggle.com](https://www.kaggle.com/).
    *   Navigate to **Account** settings.
    *   Scroll to the "API" section and click **"Create New Token"**.
    *   This will download a file named `kaggle.json`.
3.  **Authenticate:**
    Move the file to the correct directory so the script can access it:
    ```bash
    mkdir -p ~/.kaggle
    mv ~/Downloads/kaggle.json ~/.kaggle/
    chmod 600 ~/.kaggle/kaggle.json
    ```

### 2. Running the Workflow
Once the API is set up, you can run the entire analysis (acquisition, processing, and visualization) using the provided automation script:

1.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
2.  **Execute Workflow:**
    ```bash
    snakemake --cores 1
    ```

## References
*   **Dataset:** Pedersen, U. T. (2023). *Fast Food Nutrition*. Kaggle.
*   **Dataset:** Saxena, S. (2023). *Food Nutrition Dataset*. Kaggle.
*   **Dataset:** Dey, U. (2023). *Food Nutrition Dataset (Yazio)*. Kaggle.
*   **Software:** Python Software Foundation. (2023). *Python Language Reference, version 3.11*.
*   **Software:** Waskom, M. L. (2021). *Seaborn: statistical data visualization*. Journal of Open Source Software, 6(60), 3021.
