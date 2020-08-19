#!/usr/bin/env python
# coding: utf-8

# In[52]:


import os
import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.externals import joblib
from joblib import dump, load

from sklearn.metrics import mean_squared_error, r2_score


# In[53]:


def load_model_predict(data_input,safety_factor): 
    
    today_string = datetime.datetime.today().strftime('%Y_%m_%d')
    model = load('model/close_Δt_modelSelected_'+ today_string + '.joblib') 
    
    scaler_file = "model/close_Δt_model_scaler.save"
    scaler = joblib.load(scaler_file) 
    
    data_input_transform = scaler.transform(data_input)
    Δt_pred = model.predict(data_input_transform) + safety_factor*60
    
    return Δt_pred


# In[63]:


def load_test_data(X_path, y_path, safety_factor):
    
    global X_input, y_input
    X_input = pd.read_csv(X_path).set_index(keys = '关机时间')
    y_input = pd.read_csv(y_path, header=None)[1]
    
    y_pred = load_model_predict(X_input,safety_factor)
    mse_score = mean_squared_error(y_pred/60, y_input/60)
    
    df_y_input = pd.DataFrame(data=y_input.values, index=X_input.index, columns=['Δt_true'])
    df_y_pred = pd.DataFrame(data=y_pred, index=X_input.index, columns=['Δt_predict'])
    
    return df_y_pred, df_y_input, X_input, mse_score


# In[204]:


if __name__=="__main__":

    today_string = datetime.datetime.today().strftime('%Y_%m_%d')
    
    X_path = 'data_X_y/Close_X_'+ today_string + '.csv'
    y_path = 'data_X_y/Close_y_'+ today_string + '.csv'
    
    global df_concat
    df_concat=pd.concat([load_test_data(X_path, y_path, 0.5)[2],load_test_data(X_path, y_path, 0.5)[1],load_test_data(X_path, y_path, 0.5)[0]],axis=1)
    
    df_concat['现在时间'] = pd.to_timedelta(df_concat['Δt_predict'],unit='s').index.astype('datetime64[ns]')

    df_concat['Δt_predict'] = pd.to_timedelta(df_concat['Δt_predict'],unit='s')
    df_concat['Δt_true'] = pd.to_timedelta(df_concat['Δt_true'],unit='s')

    df_concat['预测脱离标准时间点'] = df_concat['Δt_predict'] + df_concat['现在时间']
    df_concat['实际脱离标准时间点'] = df_concat['Δt_true'] + df_concat['现在时间']
    
    zhisi_path = "data\product_plan\hongyesi_order0529.csv"

    hongsi = pd.read_csv(zhisi_path, encoding='utf-8')
    hongsi.EntryEndTime = pd.to_datetime(hongsi.EntryEndTime)
    
    hongsi_last_time_pred =[]
    for i in range(len(df_concat.Δt_predict)):
        hongsi_end=hongsi['EntryEndTime'][hongsi['EntryEndTime'] <= df_concat['预测脱离标准时间点'][i]].max()
        hongsi_last_time_pred.append(hongsi_end)

    hongsi_end_next_pred=[]
    for i in range(len(hongsi_last_time_true)):
        hongsi_end_next_pred.append(hongsi['EntryEndTime'][hongsi['EntryEndTime'] > hongsi_last_time_pred[i]].min())

    hongsi_end_next2_pred=[]
    for i in range(len(hongsi_end_next_pred)):
        hongsi_end_next2_pred.append(hongsi['EntryEndTime'][hongsi['EntryEndTime'] > hongsi_end_next_pred[i]].min())

    hongsi_lasttime=[]
    for i in range(len(df_concat)):
        if (hongsi_end_next_pred[i] - hongsi_last_time_pred[i]) >= pd.Timedelta(hours=12):
            hongsi_lasttime.append(hongsi_last_time_pred[i])
        elif (hongsi_end_next2_pred[i]-hongsi_end_next_pred[i]) >= pd.Timedelta(hours=12):
            hongsi_lasttime.append(hongsi_end_next_pred[i])

    df_concat['哄切丝_最后开始时间'] = hongsi_lasttime

    df_concat.to_csv('csv_pbi/close_data_' + today_string + '.csv',index=True)


# In[200]:





# In[201]:



# df_data_close_select = df_data_open_close(biaoleng_path,huifeng_T_path,fan_elec_path,outdoor_TH_path)[1]


# In[203]:


df_concat


# In[ ]:




