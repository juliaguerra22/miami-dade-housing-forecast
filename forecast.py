import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error
import matplotlib.pyplot as plt

df_2010= pd.read_csv('data_2010.csv')
df_2020= pd.read_csv('data_2020.csv')

#selecting columns
geo_ID = "GeoID"
income_col= 'Median Household Income'
rent_col= 'Median Gross Rent'
pov_col= "Percent Poverty"
edu_col= "Percent Population with At Least Bachelor's Degree"
df_2010_simple = df_2010[[geo_ID,income_col, rent_col, pov_col, edu_col]]
df_2020_simple = df_2020[[geo_ID,income_col, rent_col, pov_col, edu_col]]

#replacing missing values with column mean
df_2010.fillna(df_2010.mean(numeric_only=True), inplace=True)
df_2020.fillna(df_2020.mean(numeric_only=True), inplace=True)

#matching 2010 and 2020 by zip code(geo_ID)
data = pd.merge(df_2010_simple, df_2020_simple, on=geo_ID, suffixes=('_2010', '_2020'))
data = data.dropna() #revoe rows with missing values after merging

#using features(2010) to predict target(2020 rent)
features = ['Median Household Income_2010', 'Median Gross Rent_2010', "Percent Poverty_2010", "Percent Population with At Least Bachelor's Degree_2010"]
X = data[features]
y = data['Median Gross Rent_2020']

#spliting data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 1) Random Forest model
#training the model
r_model = RandomForestRegressor(n_estimators=200, random_state=42)
r_model.fit(X_train, y_train)
r_pred = r_model.predict(X_test)
r_mse = mean_squared_error(y_test, r_pred)
r_mae = mean_absolute_error(y_test, r_pred)

# 2) Decision Tree model
dt_model = DecisionTreeRegressor(random_state=42) 
dt_model.fit(X_train, y_train)
dt_pred = dt_model.predict(X_test)
dt_mse = mean_squared_error(y_test, dt_pred)
dt_mae = mean_absolute_error(y_test, dt_pred)

#printing random forest results
print("RANDOM FOREST RESULTS")
print("MSE:", r_mse)
print("MAE:", r_mae)
print("5 Predictions vs Actual:")
print("Pred:", r_pred[:5])
print("Real:", y_test.values[:5])

#decision tree results
print("DECISION TREE RESULTS")
print("MSE:", dt_mse)
print("MAE:", dt_mae)
print("5 Predictions vs Actual:")
print("Pred:", dt_pred[:5])
print("Real:", y_test.values[:5])

#bar plot for Random Forest 
plt.scatter(y_test, r_pred, c='blue', s=50)
plt.plot([1000, 4000], [1000, 4000], 'r-') 
plt.xlabel("Actual 2020 Rent")
plt.ylabel("Predicted 2020 Rent")
plt.title("Random Forest: Predicted vs Actual")
plt.show()

#bar plot for Decision Tree
plt.scatter(y_test, dt_pred, c='green', s=50)
plt.plot([y_test.min(),y_test.max()],[y_test.min(), y_test.max()], 'r-')
plt.xlabel("Actual 2020 Rent")
plt.ylabel("Predicted 2020 Rent")
plt.title("Decision Tree: Predicted vs Actual")
plt.show()

#bar plot comparing errors
models = ['Random Forest', 'Decision Tree']
mse_values = [r_mse, dt_mse]
mae_values = [r_mae, dt_mae]
plt.bar(models, mse_values)
plt.title("MSE: Random Forest vs Decision Tree")
plt.ylabel("MSE")
plt.show()

plt.bar(models, mae_values)
plt.title("MAE: Random Forest vs Decision Tree")
plt.ylabel("MAE")
plt.show()

#top 5 highest poverty zip codes' percent of income spent on rent
top5= data.nlargest(5, 'Percent Poverty_2010')
top5['Rent_to_Income_Ratio_2020']=(top5['Median Gross Rent_2020']/(top5['Median Household Income_2020']/12))*100
plt.bar(top5[geo_ID].astype(str), top5['Rent_to_Income_Ratio_2020'])
plt.title("Top 5 Highest Poverty ZIP Codes' Percent of Income Spent on Rent")
plt.ylabel("Percent of Income Spent on Rent")
plt.xlabel("ZIP Code")
plt.show()

#comparing avg rent increase in rural county vs dade
sumter_2010= pd.read_csv('sumter_data_2010.csv')
sumter_2020= pd.read_csv('sumter_data_2020.csv')
s_2010= sumter_2010[[geo_ID, rent_col]]
s_2020= sumter_2020[[geo_ID, rent_col]]
s_data= pd.merge(s_2010, s_2020, on=geo_ID,suffixes=('_2010', '_2020')).dropna()
miami_avg_increase= (data['Median Gross Rent_2020'] - data['Median Gross Rent_2010']).mean()
sumter_avg_increase= (s_data['Median Gross Rent_2020'] - s_data['Median Gross Rent_2010']).mean()
plt.bar(['Miami-Dade', 'Sumter'], [miami_avg_increase, sumter_avg_increase])
plt.title('Average Rent Increase: Miami-Dade vs Sumter')
plt.ylabel('Average Rent Increase (2010–2020)')
plt.show()


