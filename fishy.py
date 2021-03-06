# -*- coding: utf-8 -*-
"""Fishy.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1mOQfKe7bBohKpIG8hcPvW2KntscrOJEQ
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
import plotly as px
warnings.filterwarnings("ignore")
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor



fish_data =  pd.read_csv("fish.csv")

fish_data.shape

fish_data.describe

fish_data.head

fish_data.tail

fish_data.isnull().sum()

fish_data.nunique()

fish_data['Species'].unique()

fish_data['Species'].value_counts()

plt.figure(figsize=(15,6))
sns.countplot('Species', data = fish_data,palette='hls')
plt.xticks(rotation = 90)
plt.show()

sns.pairplot(fish_data)

#x defines from which column the plot has to be made and color defines how to differentiate the bars
#fig = px.hist_frame(fish_data , x= 'Species',
                    #color='Species')
# fig.show()  

fish_data.corr()

#Heatmap
plt.figure(figsize=(15,6))
sns.heatmap(fish_data.corr(), annot =True)
plt.show()

#statistical info
plt.figure(figsize=(15,6))
sns.boxplot(fish_data['Weight'])
#plt.xticks(rotation = 90)
plt.show()

#breaks the data into 
fish_weight = fish_data["Weight"]
Q3= fish_weight.quantile(0.75)
Q1= fish_weight.quantile(0.25)
IQR = Q3-Q1
lower_limit = Q1 - (1.5*IQR)
upper_limit = Q3 + (1.5*IQR)

#compares
weight_outliers = fish_weight[(fish_weight <lower_limit)|(fish_weight >upper_limit)]
weight_outliers

#statistical info
plt.figure(figsize=(15,6))
sns.boxplot(fish_data['Length1'])
#plt.xticks(rotation = 90)
plt.show()

#breaks the data into 
fish_length = fish_data["Length1"]
Q3= fish_length.quantile(0.75)
Q1= fish_length.quantile(0.25)
IQR = Q3-Q1
lower_limit = Q1 - (1.5*IQR)
upper_limit = Q3 + (1.5*IQR)

#compares
weight_outliers = fish_length[(fish_length <lower_limit)|(fish_length >upper_limit)]
weight_outliers

#statistical info
plt.figure(figsize=(15,6))
sns.boxplot(fish_data['Length2'])
#plt.xticks(rotation = 90)
plt.show()

#breaks the data into 
fish_length2 = fish_data["Length2"]
Q3= fish_length2.quantile(0.75)
Q1= fish_length2.quantile(0.25)
IQR = Q3-Q1
lower_limit = Q1 - (1.5*IQR)
upper_limit = Q3 + (1.5*IQR)

weight_outliers = fish_length2[(fish_length2 <lower_limit)|(fish_length2 >upper_limit)]
weight_outliers

#statistical info
plt.figure(figsize=(15,6))
sns.boxplot(fish_data['Length3'])
#plt.xticks(rotation = 90)
plt.show()

#breaks the data into 
fish_length3 = fish_data["Length3"]
Q3= fish_length3.quantile(0.75)
Q1= fish_length3.quantile(0.25)
IQR = Q3-Q1
lower_limit = Q1 - (1.5*IQR)
upper_limit = Q3 + (1.5*IQR)

weight_outliers = fish_length3[(fish_length3 <lower_limit)|(fish_length3 >upper_limit)]
weight_outliers

#statistical info
plt.figure(figsize=(15,6))
sns.boxplot(fish_data['Height'])
#plt.xticks(rotation = 90)
plt.show()

#breaks the data into 
fish_height = fish_data["Height"]
Q3= fish_height.quantile(0.75)
Q1= fish_height.quantile(0.25)
IQR = Q3-Q1
lower_limit = Q1 - (1.5*IQR)
upper_limit = Q3 + (1.5*IQR)

height_outliers = fish_height[(fish_height <lower_limit)|(fish_height >upper_limit)]
height_outliers

#statistical info
plt.figure(figsize=(15,6))
sns.boxplot(fish_data['Width'])
#plt.xticks(rotation = 90)
plt.show()

#breaks the data into 
fish_width = fish_data["Width"]
Q3= fish_width.quantile(0.75)
Q1= fish_width.quantile(0.25)
IQR = Q3-Q1
lower_limit = Q1 - (1.5*IQR)
upper_limit = Q3 + (1.5*IQR)

width_outliers = fish_width[(fish_width <lower_limit)|(fish_width >upper_limit)]
width_outliers

fish_data[142:145]

fish_data_new = fish_data.drop([142,143,144])

fish_data_new.head()

scaler = StandardScaler()

scaling_columns= ["Length1","Length2","Length3",
                  "Height","Weight","Width"]
fish_data_new[scaling_columns] = scaler.fit_transform(fish_data_new[scaling_columns])
fish_data_new.describe()

label_encoder = LabelEncoder()
fish_data_new['Species'] = label_encoder.fit_transform(fish_data_new['Species'].values)

data_cleaned = fish_data_new.drop("Weight", axis=1)
y= fish_data_new['Weight']

x_train,x_test,y_train,y_test=train_test_split(data_cleaned,y,test_size = 0.2,random_state=0)

model = RandomForestRegressor()
model.fit(x_train, y_train)

y_pred = model.predict(x_test)

print('Training Accuracy : ',model.score(x_train,y_train))
print('Testing Accuracy : ',model.score(x_test,y_test))

from sklearn.tree import DecisionTreeRegressor

model1 = DecisionTreeRegressor()
model1.fit(x_train,y_train)

print('Training Accuracy : ',model1.score(x_train,y_train))
print('Testing Accuracy : ',model1.score(x_test,y_test))

from sklearn.linear_model import LinearRegression

model2 = LinearRegression()
model2.fit(x_train,y_train)

print('Training Accuracy : ',model2.score(x_train,y_train))
print('Testing Accuracy : ',model2.score(x_test,y_test))

import xgboost as xgb
xgb1 = xgb.XGBRegressor()

xgb1.fit(x_train,y_train)
xgb_pred = xgb1.predict(x_test)

print('Training Accuracy : ',xgb1.score(x_train,y_train))
print('Testing Accuracy : ',xgb1.score(x_test,y_test))

xgb1.save_model("model.json")

import streamlit as st

st.header("Fish Weight Prediction App")
st.text_input("Enter your name", key = "name")

np.save('classes.npy',label_encoder.classes_)

label_encoder.classes_= np.load('classes.npy', allow_pickle=True)

xgb_best = xgb.XGBRegressor()

xgb_best.load_model("model.json")

if st.checkbox('Show Training DataFrame'):
  fish_data

st.subheader('Please select relevant features of your fish')
left_column, right_column = st.columns(2)
with left_column:
  inp_species = st.radio('Name of the fish:',
                         np.unique(fish_data['Species']))

input_Length1 = st.slider('Vertical length(cm)',0.0,max(fish_data["Length1"]),1.0)
input_Length2 = st.slider('Diagonal length(cm)',0.0,max(fish_data["Length2"]),1.0)
input_Length3 = st.slider('Cross length(cm)',0.0,max(fish_data["Length3"]),1.0)
input_Height = st.slider('Height length(cm)',0.0,max(fish_data["Height"]),1.0)
input_Width = st.slider('Width length(cm)',0.0,max(fish_data["Width"]),1.0)

if st.button('Make Predictions'):
    input_species = label_encoder.transform(np.expand_dims(inp_species,-1))
    inputs = np.expand_dims([int(input_species),input_Length1, input_Length2, input_Length3, input_Height, input_Width],0)
    prediction = xgb_best.predict(inputs)
    print("final pred", np.squeeze(prediction,-1))
    st.write(f"Your fish weight is: {np.squeeze(prediction,-1):.2f}.g")