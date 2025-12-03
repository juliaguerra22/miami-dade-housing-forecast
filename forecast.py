import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

df_2010= pd.read_csv('data_2010.csv')
df_2020= pd.read_csv('data_2020.csv')

income_col= 'Median Household Income'
rent_col= 'Median Gross Rent'
edu_col= "Percent Population with At Least Bachelor's Degree"

df_2010_simple = df_2010[[income_col, rent_col, edu_col]]
df_2020_simple = df_2020[[income_col, rent_col, edu_col]]

