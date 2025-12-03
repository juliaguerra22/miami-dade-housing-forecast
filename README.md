**Miami-Dade Housing Price Prediction in 10 Years Using Machine Learning**
--
This project uses machine learning to predict housing prices in 10 years by comparing 2010 and 2020 data for zip codes within Miami-Dade County. 

**Approach**
We built a **Random Forest regression model**, chosen because prior research (Yoo, 2023) shows that Random Forests perform especially well in gentrification prediction tasks, which was our previous idea, but we expect it to perform just as well for this model. This model makes use of RF in order to find **nonlinear relationships** between **housing prices and factors like income, rent, and education levels**.

**Dataset**
- The dataset is created by combining multiple public sources found in Policy Map from the **American Community Survey (ACS)** for Miami-Dade County zip codes from **2010** and **2020**.
- **This data includes:** Median rents, income levels, and education attainment all at the zip code level, with columns like **Median Gross Rent, Median Household Income, and Percent Population with At Least Bachelors Degree**. - After preprocessing and cleaning, the dataset includes:
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
