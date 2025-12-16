**Miami-Dade Housing Price Prediction in 10 Years Using Machine Learning**
--
This project uses machine learning to predict housing prices in 10 years by comparing 2010 and 2020 data for zip codes within Miami-Dade County. 


**Overview**

This project analyses **Miami-Dade ZIP code data from 2010 and 2020** to understand how rent burden has changed over time. Using **Random Forest and Decision Tree regression models**, chosen for their strong performance in **identifying nonlinear relationships** in gentrification studies (Yoo, 2023), we predicted **2020 median rents** based on **2010 socioeconomic features** such as **income, poverty rate, and education level**. Our findings revealed that Miami-Dade’s **highest-poverty ZIP codes** (33034, 33136, 33054, 33142, 33128) had renters spending about 33-44% of their household income on rent in 2020, highlighting **significant affordability challenges**.


**Dataset**

- The dataset combines multiple publicly available sources from PolicyMap, using data from the **American Community Survey (ACS)** for **Miami-Dade County ZIP codes from 2010 and 2020**.
- It includes key socioeconomic indicators such as **Median Gross Rent, Median Household Income, and Percent Population with at Least a Bachelor’s Degree**, all at the ZIP code level.
- Additional data from **Sumter County**, including **GeoID** and **Median Gross Rent** for both years, was used to calculate and **compare average rent increase**s between 2010 and 2020.
- After preprocessing and cleaning, the final dataset contains **predictive variables** from 2010 that were used to model and **analyze rent changes** observed in 2020.


**Features**

The key features used to predict housing prices include:
- Median Household Income
- Median Gross Rent
- Percent Poverty
- Percent Population with At Least Bachelor's Degree


**Model Evaluation**

We will evaluate model performance primarily using regression metrics such as:
- Mean Squared Error **(MSE)**
- Mean Absolute Error **(MAE)**


**Replication Instructions**

1. Clone the repository
2. Ensure Python is installed (Python 3.8 is recommended)
3. Run the main forecasting script: python3 forecast.py
4. The script performs the following: 
- Preprocesses ACS ZIP-code–level data from 2010 and 2020 
- Trains a Random Forest and a Decision Tree regression model 
- Prints evaluation metrics (MSE, MAE) and sample predictions 
- Generates plots, including: 
  - Predicted vs Actual rents for both models Feature importances for both models 
  - Model performance comparison (MSE/MAE) 
  - Rent burden and increase analysis by ZIP code 
  - Comparison of average rent increase between Miami-Dade and Sumter County 
  - Projected 2030 rent and rent-to-income ratios


**Future Directions**

Future work can improve this project by adding housing policy and climate risk data to better understand drivers of rent growth. We can:
- Integrate ZIP-code–level information on rent control, zoning changes, or upzoning to separate policy effects from market trends and support more actionable recommendations.
- Add coastal flooding and climate exposure data to examine whether displacement from flood-prone areas contributes to rising rents in nearby inland, lower-income ZIP codes, helping identify patterns of climate-driven gentrification.


**Contributions**

Task| Time Spent| Person
Collect Data and Preprocess it| 8 days | Julia
Model Implementation and training| 7 days | Aayusha
Model Evaluation and Validation | 3 days | Julia
Final Poster Introduction |1 day| Julia
Final Poster Experimental setup |1 day| Aayusha
Summary + Conclusion |1 day| Both
Background |1 day| Julia
Results |1 day| Aayusha
Future directions |1 day| Both
Edits Based on Milestone Two Feedback 
Add Rural County Rent Compared to Miami-Dade Rent |1 day| Julia
Compare Rent Increases between Low/High-income ZIP codes |1 day| Aayusha
Add Feature Importance Graph to Poster |1 day| Aayusha 
