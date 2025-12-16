**Miami-Dade Housing Price Prediction in 10 Years Using Machine Learning**
--
This project uses machine learning to predict housing prices in 10 years by comparing 2010 and 2020 data for zip codes within Miami-Dade County. 

**Approach**

We built a **Random Forest regression model**, chosen because prior research (Yoo, 2023) shows that Random Forests perform especially well in gentrification prediction tasks, which was our previous idea, but we expect it to perform just as well for this model. This model makes use of RF in order to find **nonlinear relationships** between **housing prices and factors like income, rent, and education levels**.

**Dataset**

- The dataset is created by combining multiple public sources found in Policy Map from the **American Community Survey (ACS)** for Miami-Dade County zip codes from **2010** and **2020**.
- **This data includes:** Median rents, income levels, and education attainment all at the zip code level, with columns like **Median Gross Rent, Median Household Income, and Percent Population with At Least Bachelors Degree**. - After preprocessing and cleaning, the dataset includes:
  - Predictive variables (features) from **2010** to train on changes observed in **2020**.
  
**Features**

The key features used to predict housing prices include:
- Median rent
- Median household income
- Levels of educational attainment

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

Future work can enhance this project by incorporating housing policy and climate risk data to better explain the drivers of rent growth. We can include ZIP-code–level information on rent control and zoning changes to separate policy effects from market trends and make more actionable recommendations. We can also add coastal flooding and climate exposure data to examine whether displacement from flood-prone areas increases rents in nearby inland, lower-income ZIP codes, helping identify patterns of climate-driven gentrification.


