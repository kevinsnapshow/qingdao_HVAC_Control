#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# !pip install joblib


# In[2]:


import os
import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.externals import joblib
from joblib import dump, load

from sklearn.preprocessing import StandardScaler

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor


# In[3]:


# today_string = datetime.datetime.today().strftime('%Y_%m_%d')
# df = pd.read_csv('open_data_pre_2020_06_10.csv')

def import_train_data():
    
    global today_string
    today_string = datetime.datetime.today().strftime('%Y_%m_%d')
    filename = 'data_pre/open_data_' + today_string + '.csv'
    df = pd.read_csv(filename)
    
    # 对导入的数据做了进一步的筛选，只选择 min_hour =1 & max_hour =6 
    
    min_hour = 1
    max_hour = 6
    
    df_selected = df[(df['Δt'] >= 3600*min_hour) & (df['Δt'] <= 3600*max_hour)]
    
    X = df_selected.drop(['Δt'], axis=1)
    y = df_selected['Δt']
    
    return X, y


# In[4]:


def data_split_validation(test_size):
    
    #Split the dataset into training and test datasets   
    
    global X_train, X_test, y_train, y_test, X_train_transform, X_test_transform 
    
    X_train, X_test, y_train, y_test = train_test_split(import_train_data()[0].set_index(keys = '时间'), import_train_data()[1], test_size=test_size,  random_state=0)
    
    
    # 数据归一化和标准化
    scaler = StandardScaler()
    scaler.fit(X_train)

    X_train_transform = scaler.transform(X_train)
    X_test_transform = scaler.transform(X_test)
    
    # Save it
    scaler_file = "model/open_Δt_model_scaler.save"
    joblib.dump(scaler, scaler_file) 
    
    return X_train, X_train_transform, y_train, X_test, X_test_transform, y_test 


# In[5]:


def linear_regression(test_size, safety_factor):
    
    data_split_validation(test_size)
    
    reg = LinearRegression().fit(X_train_transform, y_train)
    Δt_pred = reg.predict(X_test_transform) + safety_factor*3600
    mse_score = mean_squared_error(Δt_pred/3600, y_test/3600)
    
    return  reg, Δt_pred/3600, mse_score


# In[6]:


def Random_Forest_Regression(test_size, safety_factor):
    data_split_validation(test_size)

    rfr = RandomForestRegressor()
    rfr.fit(X_train_transform, y_train)
    Δt_pred = rfr.predict(X_test_transform) + safety_factor*3600
    mse_score = mean_squared_error(Δt_pred/3600, y_test/3600)
    
    return rfr, Δt_pred/3600, mse_score


# In[7]:


def GB_Regression(test_size, safety_factor):
    data_split_validation(test_size)
    
    gbr = GradientBoostingRegressor()
    gbr.fit(X_train_transform, y_train)
    Δt_pred = gbr.predict(X_test_transform) + safety_factor*3600
    mse_score = mean_squared_error(Δt_pred/3600, y_test/3600)
    
    return gbr, Δt_pred/3600, mse_score


# In[8]:


def model_save(test_size, safety_factor):
    model = GB_Regression(test_size, safety_factor)[0]
    dump(model, 'model/open_Δt_modelSelected_'+ today_string + '.joblib') 


# In[10]:


def validation_data():
    X_test.to_csv('X_test_open.csv')
    y_test.to_csv('y_test_open.csv', index=False)


# In[11]:


if __name__=="__main__":
    
    test_size =0.2
    safety_factor = 0.5
    
#     import_train_data()
    data_split_validation(test_size)
    model_save(test_size, safety_factor)
    import_train_data()[0].to_csv('data_X_y/Open_X_'+ today_string + '.csv', index=False)
    import_train_data()[1].to_csv('data_X_y/Open_y_'+ today_string + '.csv', index=False)

    print('最新的GB开机训练模型已经导出')


# In[11]:


# validation_data()


# In[ ]:


# def Δt_plot():

#     plt.boxplot([df['Δt']], patch_artist=True)
#     plt.show()

