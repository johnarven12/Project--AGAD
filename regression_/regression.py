import pandas as pd
import numpy as np
import math
from sklearn.linear_model import LinearRegression

df = pd.read_csv('C:/Users/ceejay/Desktop/reg2/DATA.csv')
df.head()

#print (df.columns.tolist())

y = df['scale']
x = df[['precipitation','surface_soil_wetness','rootsurface_soil_wetness','soil_moisture','elevation']]

linear_regress = LinearRegression()
linear_regress.fit(x,y)
"""
a_pred = linear_regress.predict([[.29,.87,.88,.83,268.37]]) #test for scale 1
a_pred1 = linear_regress.predict([[4.27,.73,.73,.72,95.38]]) #test for scale 1
a_pred2 = linear_regress.predict([[5.04,.84,.84,.87,715.65]]) #test for 2
a_pred3 = linear_regress.predict([[2.87,.83,.83,.8,58.58]])#test for 2
a_pred4 = linear_regress.predict([[18.14,.89,.88,.99,715.65]])#test for 3
a_pred5 = linear_regress.predict([[.545,.88,.89,.93,98.77]])#test for 3
a_pred6 = linear_regress.predict([[.53,.91,.95,.91,123.85]])#test for 4
a_pred7 = linear_regress.predict([[.545,.68,.07,.68,98.77]])#test for 4
a_pred8 = linear_regress.predict([[.545,.84,.85,.84,62.5]])#test for 5
a_pred9 = linear_regress.predict([[.545,.88,.89,.93,184.24]])#test for 5
a_pred10 = linear_regress.predict([[.545,.88,.89,.93,184.24]])#test for 5
a_pred11 = linear_regress.predict([[0,.15,.20,.20,50]])#test for none
a_pred12 = linear_regress.predict([[0,.15,.20,.20,150]])#test for none

print("POSSIBLE CHANCE OF LANDSLIDE:",a_pred)
print("POSSIBLE CHANCE OF LANDSLIDE:",a_pred1)
print("POSSIBLE CHANCE OF LANDSLIDE:",a_pred2)
print("POSSIBLE CHANCE OF LANDSLIDE:",a_pred3)
print("POSSIBLE CHANCE OF LANDSLIDE:",a_pred4)
print("POSSIBLE CHANCE OF LANDSLIDE:",a_pred5)
print("POSSIBLE CHANCE OF LANDSLIDE:",a_pred6)
print("POSSIBLE CHANCE OF LANDSLIDE:",a_pred7)
print("POSSIBLE CHANCE OF LANDSLIDE:",a_pred8)
print("POSSIBLE CHANCE OF LANDSLIDE:",a_pred9)
print("POSSIBLE CHANCE OF LANDSLIDE:",a_pred10)
print("POSSIBLE CHANCE OF LANDSLIDE:",a_pred11)
print("POSSIBLE CHANCE OF LANDSLIDE:",a_pred12)
"""
