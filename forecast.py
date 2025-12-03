import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error
import matplotlib.pyplot as plt

df_2010= pd.read_csv('data_2010.csv')
df_2020= pd.read_csv('data_2020.csv')

#selecting columns
geo_ID = "GeoID"
income_col= 'Median Household Income'
rent_col= 'Median Gross Rent'
edu_col= "Percent Population with At Least Bachelor's Degree"
df_2010_simple = df_2010[[geo_ID,income_col, rent_col, edu_col]]
df_2020_simple = df_2020[[geo_ID,income_col, rent_col, edu_col]]

#replacing missing values with column mean
df_2010.fillna(df_2010.mean(numeric_only=True), inplace=True)
df_2020.fillna(df_2020.mean(numeric_only=True), inplace=True)

#matching 2010 and 2020 by zip code(geo_ID)
data = pd.merge(df_2010_simple, df_2020_simple, on=geo_ID, suffixes=('_2010', '_2020'))
data = data.dropna() #revoe rows with missing values after merging

#using features(2010) to predict target(2020 rent)
features = ['Median Household Income_2010', 'Median Gross Rent_2010', "Percent Population with At Least Bachelor's Degree_2010"]
X = data[features]
y = data['Median Gross Rent_2020']

#spliting data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#training the model
model = RandomForestRegressor(n_estimators=200, random_state=42)
model.fit(X_train, y_train)

# predict and check accuracy
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)


print("MSE:", mse) 
print("MAE:",mae)
print("5 Predictions vs Actual:")
print("Pred:", y_pred[:10])
print("Real:", y_test.values[:10])

# bar-plot

importances = model.feature_importances_

plt.bar(features, importances)
plt.title("Feature Importance")
plt.ylabel("Importance", fontsize="8")
plt.show()
plt.pause(1)


plt.scatter(y_test, y_pred, c='blue', s=50)
plt.plot([1000, 4000], [1000, 4000], c='red')
plt.xlabel("Actual 2020 Rent")
plt.ylabel("Predicted 2020 Rent")
plt.title("Predicted vs Actual")
plt.show()
