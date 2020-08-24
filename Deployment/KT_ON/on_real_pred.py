#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import datetime
from datetime import datetime
import time
from time import mktime
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
from sklearn.externals import joblib
from joblib import dump, load

from sklearn.metrics import mean_squared_error, r2_score


# In[2]:


def real_time_data_pre(sample_data):
    df = pd.DataFrame.from_dict(sample_data)

    time_col = ['entryStartTime', 'time']
    for i in range(len(time_col)):
        ts=[]
        for j in df[time_col[i]]:
            time_local = time.localtime(j/1000)
            ts.append(pd.to_datetime(datetime.fromtimestamp(mktime(time_local))))
        df[time_col[i]] = ts
        
    df_col = ['time',
      'supplyAirHumidity',
      'supplyAirTemperature',
      'returnAirHumidity',
      'freshAirTemperature',
      'freshAirHumidity',
      'outdoorTemperature',
      'outdoorHumidity',
      'returnAirTemperature1',
      'avgT',
      'avgH',
      'tempAfter0Hour',
      'humiAfter0Hour',
      'tempAfter1Hour',
      'humiAfter1Hour',
      'tempAfter2Hour',
      'humiAfter2Hour',
      'tempAfter3Hour',
      'humiAfter3Hour',
      'tempAfter4Hour',
      'humiAfter4Hour']
    
    if all(df.blowerCurrent) == 0:
        df_input = df[df_col]
        # Set the humid in percentages value
        df_input[df_input.columns[[-1,-3,-5,-7,-9]]] = df_input[df_input.columns[[-1,-3,-5,-7,-9]]]*100
    else:
        print('The electrical fan has been turned on')
        
    return df_input, df.entryStartTime


# In[3]:


def load_model_predict(today_string, data_input,safety_factor): 

    model = load('model/open_Δt_modelSelected_'+ today_string + '.joblib') 
    
    scaler_file = "model/open_Δt_model_scaler.save"
    scaler = joblib.load(scaler_file) 
    
    data_input = data_input.set_index('time')
    data_input_transform = scaler.transform(data_input)
    
    # timedelta预测值
    Δt_pred = model.predict(data_input_transform) + safety_factor*3600
    
    # 转化为timestamp预测值
    timestamp_pred = pd.to_datetime(data_input.index) + pd.Timedelta(seconds = Δt_pred[0])
    
    return Δt_pred[0]/3600, timestamp_pred


# In[4]:


if __name__=="__main__":

    sample_data = [{"avgH":70.92013852,"avgT":30.190974419999996,"blowerCurrent":0.0,"entryStartTime":1594311352000,"freshAirHumidity":49.6238441,"freshAirTemperature":29.3344917,"humiAfter0Hour":0.91,"humiAfter1Hour":0.71,"humiAfter2Hour":0.62,"humiAfter3Hour":0.62,"humiAfter4Hour":0.68,"outdoorHumidity":60.8217583,"outdoorTemperature":26.7881966,"returnAirHumidity":54.4270821,"returnAirTemperature1":31.765049,"supplyAirHumidity":71.09375,"supplyAirTemperature":27.598381,"tempAfter0Hour":25.79,"tempAfter1Hour":25.82,"tempAfter2Hour":26.86,"tempAfter3Hour":25.9,"tempAfter4Hour":25.93,"time":1594363961258},{"avgH":70.92013852,"avgT":30.190974419999996,"blowerCurrent":0.0,"entryStartTime":1594311352000,"freshAirHumidity":49.6238441,"freshAirTemperature":29.3344917,"humiAfter0Hour":0.91,"humiAfter1Hour":0.71,"humiAfter2Hour":0.62,"humiAfter3Hour":0.62,"humiAfter4Hour":0.68,"outdoorHumidity":60.8217583,"outdoorTemperature":26.7881966,"returnAirHumidity":54.4270821,"returnAirTemperature1":31.765049,"supplyAirHumidity":71.09375,"supplyAirTemperature":27.598381,"tempAfter0Hour":25.79,"tempAfter1Hour":25.82,"tempAfter2Hour":26.86,"tempAfter3Hour":25.9,"tempAfter4Hour":25.93,"time":1594363917252},{"avgH":70.92013852,"avgT":30.190974419999996,"blowerCurrent":0.0,"entryStartTime":1594311352000,"freshAirHumidity":49.6238441,"freshAirTemperature":29.3344917,"humiAfter0Hour":0.91,"humiAfter1Hour":0.71,"humiAfter2Hour":0.62,"humiAfter3Hour":0.62,"humiAfter4Hour":0.68,"outdoorHumidity":60.8217583,"outdoorTemperature":26.7881966,"returnAirHumidity":54.4270821,"returnAirTemperature1":31.765049,"supplyAirHumidity":71.09375,"supplyAirTemperature":27.598381,"tempAfter0Hour":25.79,"tempAfter1Hour":25.82,"tempAfter2Hour":26.86,"tempAfter3Hour":25.9,"tempAfter4Hour":25.93,"time":1594363829262}]
    
    data_input_pre, entryStartTime_thre_ = real_time_data_pre(sample_data)
    today_string = datetime.today().strftime('%Y_%m_%d')
    safety_factor = 0.5
    
    Δt_pred, timestamp_pred = load_model_predict(today_string, data_input_pre,safety_factor)
    
    if all(items > entryStartTime_thre_[0] for items in timestamp_pred.to_list()):
        action_required = 1
        print('The fan will be turned on now.')
    else:
        action_required = 0
        print('The fan will remain to be off.')
    
#     print('现在开机到达标范围所需时间 {} 小时'.format(round(Δt_pred,2)) +'\n'+
#           '达标时间戳： {}'.format(timestamp_pred)+'\n'+
#           '开机时间预测完成')


# In[ ]:




