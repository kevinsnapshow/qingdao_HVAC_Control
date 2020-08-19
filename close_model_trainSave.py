#!/usr/bin/env python
# coding: utf-8

# In[ ]:


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


# In[22]:


# today_string = datetime.datetime.today().strftime('%Y_%m_%d')
# df = pd.read_csv('open_data_pre_2020_06_10.csv')

def import_train_data():
    
    global today_string
    today_string = datetime.datetime.today().strftime('%Y_%m_%d')
    filename = 'data_pre/close_data_' + today_string + '.csv'
    df = pd.read_csv(filename, index_col=[0])
    
    df_selected = df.drop(['关机时间','天气预报时间_现在'],axis=1)
    df_selected.index = df['关机时间']
    df_selected = df_selected[df_selected['Δt_close'] > 0]
    
    X = df_selected.drop(['Δt_close'], axis=1)
    y = df_selected['Δt_close']
    
    return X, y


# In[ ]:


# df_selected = df[(df['Δt'] >= 10000) & (df['Δt'] <= 21000)][['Avg_T','Avg_H','0小时后_温度℃','0小时后_相对湿度%','4小时后_温度℃','4小时后_相对湿度%','Δt']]
# df_selected = df[df['Δt'] >= 10000][['Avg_T','Avg_H','0小时后_温度℃','0小时后_相对湿度%','4小时后_温度℃','4小时后_相对湿度%','Δt']]


# In[15]:


def data_split_validation(test_size):
    
    global X_train, X_test, y_train, y_test, X_train_transform, X_test_transform 
    X_train, X_test, y_train, y_test = train_test_split(import_train_data()[0], import_train_data()[1], test_size=test_size,  random_state=0)
    
    # 数据归一化和标准化
    scaler = StandardScaler()
    scaler.fit(X_train)

    X_train_transform = scaler.transform(X_train)
    X_test_transform = scaler.transform(X_test)
    
    # Save it
    scaler_file = "model/close_Δt_model_scaler.save"
    joblib.dump(scaler, scaler_file) 
    
    return X_train, X_train_transform, y_train, X_test, X_test_transform, y_test 


# In[16]:


def linear_regression(test_size, safety_factor):
    
    data_split_validation(test_size)
    
    reg = LinearRegression().fit(X_train_transform, y_train)
    Δt_pred = reg.predict(X_test_transform) + safety_factor*60
    mse_score = mean_squared_error(Δt_pred/60, y_test/60)
    
    return  reg, Δt_pred/60, mse_score


# In[17]:


def Random_Forest_Regression(test_size, safety_factor):
    data_split_validation(test_size)

    rfr = RandomForestRegressor()
    rfr.fit(X_train_transform, y_train)
    Δt_pred = rfr.predict(X_test_transform) + safety_factor*60
    mse_score = mean_squared_error(Δt_pred/60, y_test/60)
    
    return rfr, Δt_pred/60, mse_score


# In[18]:


def GB_Regression(test_size, safety_factor):
    data_split_validation(test_size)
    
    gbr = GradientBoostingRegressor()
    gbr.fit(X_train_transform, y_train)
    Δt_pred = gbr.predict(X_test_transform) + safety_factor*60
    mse_score = mean_squared_error(Δt_pred/60, y_test/60)
    
    return gbr, Δt_pred/60, mse_score


# In[19]:


def validation_data():
    X_test.to_csv('X_test_close.csv',index=False)
    y_test.to_csv('y_test_close.csv',index=False)


# In[20]:


def model_save(test_size, safety_factor):
    model = GB_Regression(test_size, safety_factor)[0]
    dump(model, 'model/close_Δt_modelSelected_'+ today_string + '.joblib') 


# In[24]:


if __name__=="__main__":
    
    test_size =0.2
    safety_factor = 0.5
    
#     import_train_data()
    data_split_validation(test_size)
    model_save(test_size, safety_factor)
    import_train_data()[0].to_csv('data_X_y/Close_X_'+ today_string + '.csv', index=True)
    import_train_data()[1].to_csv('data_X_y/Close_y_'+ today_string + '.csv', index=True)
    
    print('最新的GB关机训练模型已经导出')


# In[ ]:




