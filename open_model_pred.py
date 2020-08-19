#!/usr/bin/env python
# coding: utf-8

# In[6]:


import os
import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.externals import joblib
from joblib import dump, load

from sklearn.metrics import mean_squared_error, r2_score


# In[47]:


def load_model_predict(data_input,safety_factor): 

    today_string = datetime.datetime.today().strftime('%Y_%m_%d')
    model = load('model/open_Δt_modelSelected_'+ today_string + '.joblib') 
    
    scaler_file = "model/open_Δt_model_scaler.save"
    scaler = joblib.load(scaler_file) 
    
    data_input_transform = scaler.transform(data_input)
    
    Δt_pred = model.predict(data_input_transform) + safety_factor*3600
    
    return Δt_pred


# In[48]:


def load_test_data(X_path, y_path, safety_factor):
    
    global X_input, y_input
    X_input = pd.read_csv(X_path).set_index(keys = '时间')
    y_input = pd.read_csv(y_path, header=None)
    
    y_pred = load_model_predict(X_input,safety_factor)
    mse_score = mean_squared_error(y_pred/3600, y_input/3600)
    
    y_input.index = X_input.index
    y_input.columns = ['Δt_true']
    
    df_y_pred = pd.DataFrame(data=y_pred, index=X_input.index, columns=['Δt_predict'])
    
    
    return df_y_pred, y_input, X_input, mse_score


# In[51]:


if __name__=="__main__":
    
    today_string = datetime.datetime.today().strftime('%Y_%m_%d')
    
    X_path = 'data_X_y/Open_X_'+ today_string + '.csv'
    y_path = 'data_X_y/Open_y_'+ today_string + '.csv'
    
    df_concat=pd.concat([load_test_data(X_path, y_path, 0.5)[2],load_test_data(X_path, y_path, 0.5)[1],load_test_data(X_path, y_path, 0.5)[0]],axis=1)
    df_concat.to_csv('csv_pbi/open_data_' + today_string + '.csv',index=True)


# In[ ]:




