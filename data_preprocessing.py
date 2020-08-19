#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from joblib import dump, load


# In[2]:


### Define 数据路径
outdoor_TH_path = "data/outdoor_HT.csv"
fan_elec_path = "data/fan_elec.csv"
huifeng_T_path = "data/huifeng_T.csv"
outdoor_weather_path = "data/outdoor_weather.csv"
biaoleng_path = "data/biaoleng.csv"
jialiao_path = "data\product_plan\jialiao_order0529.csv"


# ### 导入相关的数据集

# #### 室外温度湿度数据输入

# In[3]:


# Outdoor_TH_path = "data/outdoor_HT.csv"

def outdoor_TH_Import(path):
    Outdoor_TH = pd.read_csv(path, encoding='utf-8')
    
    values=[]
    for i in Outdoor_TH.values:
        values.append(i[0].split(";"))

    columns_name=[]
    for i in Outdoor_TH.columns[0].split(';'):
        columns_name.append(i.replace('"',"").replace(" ",""))

    df_outdoor_TH = pd.DataFrame(values, columns=columns_name)
    df_outdoor_TH.rename(columns={'室外温度Time':'时间'}, inplace = True)

    df_outdoor_TH = df_outdoor_TH.drop(['室外湿度Time'],axis=1)

    df_outdoor_TH['时间'] = pd.to_datetime(df_outdoor_TH['时间'])
    df_outdoor_TH[df_outdoor_TH.columns[1:]] = df_outdoor_TH[df_outdoor_TH.columns[1:]].astype(float, inplace=True)
    
    data_outdoor_two_minutes =[]
    for i in range(len(df_outdoor_TH)):
        for j in range(9):
            data_outdoor_two_minutes.append(df_outdoor_TH.loc[i,:] + (j+1)*(df_outdoor_TH.diff()/10)[1:].loc[j+1,:])

    df_outdoor_TH = df_outdoor_TH.append(data_outdoor_two_minutes)
    df_outdoor_TH = df_outdoor_TH.sort_values(by="时间").reset_index(drop=True)
    df_outdoor_TH = df_outdoor_TH.set_index('时间')
    
    return df_outdoor_TH


# #### 外部风机电流数据输入

# In[4]:


# fan_elec_path = "data/fan_elec.csv"

def fan_elec_Import(path):
    fan_elec = pd.read_csv(path, encoding='utf-8')

    values=[]
    for i in fan_elec.values:
        values.append(i[0].split(";"))

    columns_name=[]
    for i in fan_elec.columns[0].split(';'):
        columns_name.append(i.replace('"',"").replace(" ",""))

    df_fan_elec = pd.DataFrame(values, columns=columns_name)
    df_fan_elec.rename(columns={'KZS5送风机电流Time':'时间'}, inplace = True)

    df_fan_elec['时间'] = pd.to_datetime(df_fan_elec['时间'])
    df_fan_elec=df_fan_elec.set_index('时间')
    
    return df_fan_elec


# #### 回风温度数据输入

# In[5]:


# Huifeng_T_path = "data/huifeng_T.csv"

def Huifeng_T_Import(path):
    huifeng_T = pd.read_csv("data/huifeng_T.csv", encoding='utf-8')

    values=[]
    for i in huifeng_T.values:
        values.append(i[0].split(";"))

    columns_name=[]
    for i in huifeng_T.columns[0].split(';'):
        columns_name.append(i.replace('"',"").replace(" ",""))

    df_huifeng_T = pd.DataFrame(values, columns=columns_name)
    df_huifeng_T.rename(columns={'回风温度Time':'时间'}, inplace = True)

    df_huifeng_T['时间'] = pd.to_datetime(df_huifeng_T['时间'])

    df_huifeng_T=df_huifeng_T.set_index('时间')
    
    return df_huifeng_T


# #### 表冷阀开度反馈输入

# In[6]:


# biaoleng_path = "data/biaoleng.csv"

def biaoleng_Import(path):
    biaoleng = pd.read_csv(path, encoding='utf-8')

    values=[]
    for i in biaoleng.values:
        values.append(i[0].split(";"))

    columns_name=[]
    for i in biaoleng.columns[0].split(';'):
        columns_name.append(i.replace('"',"").replace(" ",""))

    biaoleng_T = pd.DataFrame(values, columns=columns_name)
    biaoleng_T.rename(columns={'表冷阀开度反馈Time':'时间'}, inplace = True)

    biaoleng_T['时间'] = pd.to_datetime(biaoleng_T['时间'])

    biaoleng_T=biaoleng_T.set_index('时间')

    return biaoleng_T


# #### 天气预报数据导入

# In[7]:


# Outdoor_weather_path = "data/outdoor_weather.csv"

def Outdoor_weather_Import(path):
    outdoor_weather = pd.read_csv(path, encoding='utf-8')
    outdoor_weather = outdoor_weather.append(pd.read_csv("data/outdoor_weather_5.csv", encoding='utf-8'))
    outdoor_weather.drop(outdoor_weather.columns[-6:], inplace = True, axis = 1)
    outdoor_weather['风向/度'] = outdoor_weather['风向/度'].astype(str)

    values =[]
    for i in outdoor_weather['风向/度']:
        values.append(i.split("/")[0])
    outdoor_weather['风向/度'] = values

    outdoor_weather['时间'] = pd.to_datetime(outdoor_weather['时间'])
    outdoor_weather=outdoor_weather.set_index('时间')
    
    return outdoor_weather


# #### 测量数据输入

# In[8]:


def measure_data_Import():

    path = os.getcwd()
    files = os.listdir(path+"\data\Odata")
    files_csv = [f for f in files if f[-3:] == 'csv']

    df = pd.DataFrame()
    for f in files_csv:
        data = pd.read_csv('data/Odata/'+ f, encoding='utf-8')
        df = df.append(data)

    values=[]
    for i in df.values:
        values.append(i[0].split(";"))

    columns_name=[]
    for i in df.columns[0].split(';'):
        columns_name.append(i.replace('"',"").replace(" ",""))

    df_data = pd.DataFrame(values, columns=columns_name)
    df_data.rename(columns={'KZS5\加热蒸汽阀位反馈Time':'时间'}, inplace = True)

    df_data['时间'] = pd.to_datetime(df_data['时间'])

    df_data=df_data.set_index('时间')
    df_data=df_data.drop(['表冷阀开度反馈Time'],axis=1)
    
    return df_data


#  #### 加上回风温度数据,外部风机电流数据,外部温度湿度数据

# In[9]:


def df_data_concat(biaoleng_path,huifeng_T_path,fan_elec_path,outdoor_TH_path):   
    
    df_measure_data = measure_data_Import()
    df_fan_elec = fan_elec_Import(fan_elec_path)
    df_outdoor_TH = outdoor_TH_Import(outdoor_TH_path)
    df_huifeng_T = Huifeng_T_Import(huifeng_T_path)
    df_biaoleng = biaoleng_Import(biaoleng_path)
    
    df_data = pd.concat([df_measure_data, df_fan_elec, df_outdoor_TH, df_huifeng_T, df_biaoleng], axis=1, join='inner')

    df_data.drop([col for col in df_data.columns if 'Time' in col],axis=1,inplace=True)
    df_data.drop(['风机运行ValueY'],axis=1,inplace=True)

    # 移除掉 ValueY
    for i in df_data.columns[0:]:
        df_data.rename(columns={i:i[:-6]}, inplace = True)

    for i in df_data.columns[df_data.columns.str.contains('KZS5')]:
        df_data.rename(columns={i:i[5:]}, inplace = True)

    df_data.rename(columns={'送风湿度1': '送风湿度'}, inplace = True)
    df_data.rename(columns={'风机电流': '送风机电流'}, inplace = True)

    df_data = df_data.drop_duplicates()
    df_data = df_data.astype(float)

    return df_data


# ##### 接下来，需要就选取出来的数据，对所有的测量温湿度值取平均值, 作为我们最终比较的指标数据. 首先我们需要看下5个点的测量的温湿度的数值分布情况。先看看5个测量点温湿度的最大和最小值，目的是排查是否有传感器未使用或者无法使用的情况。

# In[10]:


def T_H_Check(biaoleng_path,huifeng_T_path,fan_elec_path,outdoor_TH_path):
    
    df_data = df_data_concat(biaoleng_path,huifeng_T_path,fan_elec_path,outdoor_TH_path)
    AvgTH = df_data[df_data.columns[4:14]]

    # 5个测量点的最大/小值
    AvgTH_min = AvgTH[AvgTH.columns].min(axis=0)
    AvgTH_max = AvgTH[AvgTH.columns].max(axis=0)
      
    return AvgTH_min, AvgTH_max


# #### 加上每个时间点的平均值

# In[11]:


def df_data_Avg(biaoleng_path,huifeng_T_path,fan_elec_path,outdoor_TH_path):

    df_data = df_data_concat(biaoleng_path,huifeng_T_path,fan_elec_path,outdoor_TH_path)
    AvgTH = df_data[df_data.columns[4:14]]
    
    Avg_T=[]
    Avg_H=[]
    AvgTH = AvgTH.astype(float)
    AvgTH_Transpose = AvgTH.T

    for i in range(len(AvgTH.index)):
        timeindex = str(AvgTH.index[i])
        t = (AvgTH_Transpose[timeindex][AvgTH.columns[[0,2,4,6,8]]]).mean()
        h = (AvgTH_Transpose[timeindex][AvgTH.columns[[1,3,5,7,9]]]).mean()
        Avg_T.append(t)
        Avg_H.append(h)

    df_data['Avg_T'] = Avg_T
    df_data['Avg_H'] = Avg_H

    df_data = df_data.drop(AvgTH.columns, axis=1)
    df_data = df_data.sort_index()
    
    return df_data


# #### 再来看看送风机开机的情况

# In[12]:


def fan_elec_plot(biaoleng_path,huifeng_T_path,fan_elec_path,outdoor_TH_path):
    
    get_ipython().run_line_magic('matplotlib', 'inline')
    df_data = df_data_Avg(biaoleng_path,huifeng_T_path,fan_elec_path,outdoor_TH_path)
    
    plt.figure(figsize=(40,10))
    plt.plot(df_data['送风机电流'], 'o', color ='red', alpha=0.1)
    plt.show()


# ##### 我们对开机时间的选取采用的是，当开机电流的值与2分钟前的电流值大于 20，则判断从此时间点开始为开机状态。

# In[13]:


# 当开机电流的值与2分钟前的电流值大于20，则判断从此时间点开始为开机状态。
# 当开机电流的值与2分钟前的电流值小于-30，则判断从此时间点开始为关机状态

def df_data_open_close(biaoleng_path,huifeng_T_path,fan_elec_path,outdoor_TH_path):

    global df_data
    df_data = df_data_Avg(biaoleng_path,huifeng_T_path,fan_elec_path,outdoor_TH_path)    
    df_data_open = df_data[df_data['送风机电流'].diff() > 20]
    df_data_close = df_data[df_data['送风机电流'].diff() < -30]
    
    #这里能看到有开机和关机时间间隔很短的情况，所以这种开机的时间我们需要拿掉。
    #假设我们设定的判断标准是开机和关机时间必须要间隔8小时以上，否则视为无效开机。

    df_data_select_index =[]
    df_data_close_select_index =[]
    df_data_close_select_index.append(df_data_close.index[0])
    for i in (df_data_close.index[1:]):
        mask = (i - (df_data_open.index[df_data_open.index < i][-1])) > pd.Timedelta(hours=8)
        if mask:
            df_data_select_index.append(df_data_open.index[df_data_open.index < i][-1])
            df_data_close_select_index.append(i)
    
    global df_data_open_select
    global df_data_close_select
    
    df_data_open_select = df_data[df_data.index.isin(df_data_select_index)]
    df_data_close_select = df_data[df_data.index.isin(df_data_close_select_index)]

    return df_data_open_select, df_data_close_select


# In[14]:


# 根据加料数据，我们要找到对应的每一次开机过后第一次加料的时间点

def jiaoliao_first_time(jialiao_path,biaoleng_path,huifeng_T_path,fan_elec_path,outdoor_TH_path):
    jialiao = pd.read_csv(jialiao_path, encoding='utf-8')

    jialiao.EntryStartTime = pd.to_datetime(jialiao.EntryStartTime)
    jialiao = jialiao.sort_values(by = "EntryStartTime")

    df_data_open_select = df_data_open_close(biaoleng_path,huifeng_T_path,fan_elec_path,outdoor_TH_path)[0]

    jialiao_first_time = []
    for i in range(len(df_data_open_select.index)):
        jialiao_0 = jialiao['EntryStartTime'][jialiao.EntryStartTime >= df_data_open_select.index[i]].min()
        jialiao_first_time.append(jialiao_0)
        
    return jialiao_first_time


# ##### 接下来，我们需要根据每一次`开机的时间点后`至`第一次加料时间点以前`的时间段，把每两分钟的数据提取出来

# #### 同时，需要就数据集中的平均温湿度和生产标准的（30°C±1°，70%±2%）做判断，找到第一次达到温湿度要求范围内的时间点。从而进一步的算出从开机到第一次达到生产标准所需要的Δt。

# In[15]:


def df_open_data_filtered(jialiao_path,biaoleng_path,huifeng_T_path,fan_elec_path,outdoor_TH_path):
#接下来，我们需要根据每一次开机的时间点后至第一次加料时间点以前的时间段，把每两分钟的数据提取出来
#同时，需要就数据集中的平均温湿度和生产标准的（30°C±1°，70%±2%）做判断，找到第一次达到温湿度要求范围内的时间点。从而进一步的算出从开机到第一次达到生产标准所需要的Δt。

    df_data_filter = pd.DataFrame()

    T_standard_min = 29
    T_standard_max = 31

    H_standard_min = 68
    H_standard_max = 72

#     df_data = df_data_Avg(huifeng_T_path,fan_elec_path,outdoor_TH_path)
#     df_data_select = df_data_open_close(huifeng_T_path,fan_elec_path,outdoor_TH_path)[0]
    jialiao_first_time = jiaoliao_first_time(jialiao_path,biaoleng_path,huifeng_T_path,fan_elec_path,outdoor_TH_path)

    for i in range(len(df_data_open_select.index)):
        global df_s
        df_s = df_data[(df_data.index.to_frame()['时间'] >= df_data_open_select.index[i]) & (df_data.index.to_frame()['时间'] < jialiao_first_time[i])]
        df_s_Inrange = df_s[(df_s.Avg_T >= T_standard_min) & (df_s.Avg_T <= T_standard_max)  & (df_s.Avg_H >= H_standard_min) & (df_s.Avg_H <= H_standard_max)]
        df_s['生产计划时间'] = jialiao_first_time[i]
        df_s['开机时间'] = df_data_open_select.index[i]
        df_s['第一次到达标准时间'] = df_s_Inrange.index.min()
        df_s = df_s[df_s.index <= df_s_Inrange.index.min()]
        df_s['Δt'] = df_s['第一次到达标准时间'] - df_s.index

        df_data_filter = pd.concat([df_data_filter,df_s], axis=0)
        
    return df_data_filter


# #### 以下是10次开机时，结合`第一次到达标准时间`和`Δt`的数据集

# In[16]:


def df_open_select(jialiao_path,biaoleng_path,huifeng_T_path,fan_elec_path,outdoor_TH_path):

    df_data_filter = df_open_data_filtered(jialiao_path,biaoleng_path,huifeng_T_path,fan_elec_path,outdoor_TH_path)
    global df_data_model 
    df_data_model = df_data_filter[df_data_filter.index == df_data_filter['开机时间']].drop(['加热蒸汽阀位反馈','加湿蒸汽阀位反馈','表冷阀开度反馈','混风阀门反馈','新风阀门反馈'],axis=1)
    return df_data_model
# np.round(output_, decimals=2)


# #### 加入天气预报的数据（未来4小时的温度、湿度）后的预处理数据

# In[17]:


def df_data_openModel(outdoor_weather_path,biaoleng_path,jialiao_path,huifeng_T_path,fan_elec_path,outdoor_TH_path):

    df_open_select(jialiao_path,biaoleng_path,huifeng_T_path,fan_elec_path,outdoor_TH_path)
    outdoor_weather = Outdoor_weather_Import(outdoor_weather_path)

    df_data_model['天气预报时间'] = df_data_model.index.values
    time_index = df_data_model.index.to_series()
    df_data_model['天气预报时间'][time_index.dt.minute >= 30] = time_index[time_index.dt.minute >= 30] + pd.Timedelta(hours=1)
    df_data_model['天气预报时间_现在'] = df_data_model['天气预报时间'].dt.floor('h')


    # 根据测量数据的时间点选取需要的天气预报数据
    weather_time_future=[]
    weather_time_now = df_data_model['天气预报时间_现在'].unique()

    #只选取未来4小时以内的天气数据
    for i in range(5):
        weather_time_future.extend(weather_time_now + pd.Timedelta(hours=i))

    outdoor_weather_select = outdoor_weather[outdoor_weather.index.isin(weather_time_future)] 

    # 对于天气预报，我们只考虑温度和相对湿度的数据
    outdoor_weather_select = outdoor_weather_select[['温度℃','相对湿度%']]

    # 把天气预报相关维度的数据填入到模型的数据列里
    for i in range(5):
        df_data_model['天气预报时间_'+str(i)+'小时后'] = df_data_model['天气预报时间_现在']+ pd.Timedelta(hours=i)
    #     print(df_data['天气预报时间_'+str(i)+'小时后'])

        for j in outdoor_weather_select.columns:
            df_data_model[str(i)+'小时后_'+ j] = ''

            for k in range(len(outdoor_weather_select.index)):
                mask = df_data_model['天气预报时间_'+str(i)+'小时后'] == (outdoor_weather_select.index[k])
    #             print(mask)
                df_data_model[str(i)+'小时后_'+ j].loc[mask] = outdoor_weather_select[j][k]
    #             print(df_data_model[str(i)+'小时后_'+ j].loc[mask])

        df_data_model.drop(['天气预报时间_'+str(i)+'小时后'],axis=1, inplace=True)          

    df_data_model.drop(['天气预报时间_现在'], axis=1, inplace=True)
    df_data_model_final = df_data_model[df_data_model.index == df_data_model['开机时间']].drop(['天气预报时间','送风机电流'], axis=1)
    df_data_model_final['生产计划Δt'] = df_data_model_final['生产计划时间'] - df_data_model_final.index
    df_data_model_final = df_data_model_final.drop(['生产计划时间','开机时间','第一次到达标准时间'], axis = 1)
    
    df_data_model_final['Δt'] = df_data_model_final['Δt'].dt.seconds
    df_data_model_final['生产计划Δt'] = df_data_model_final['生产计划Δt'].dt.seconds
    
    today_string = datetime.datetime.today().strftime('%Y_%m_%d')
    df_data_model_final.to_csv('data_pre/open_data_' + today_string + '.csv',index=True)
    
    return df_data_model_final


# In[18]:


# 对最近一次开机的各维度的数据的可视化

def df_last_time_open_plot():
    get_ipython().run_line_magic('matplotlib', 'inline')
    plt.rcParams['font.sans-serif']=['SimHei']
    plt.rcParams['axes.unicode_minus'] = False

    # plt.subplots_adjust(hspace=0.5)

    fig, ax = plt.subplots(len(df_s.columns), 1, figsize=(15,220))

    for i in range(len(ax)):
    #     ax[i].plot(df_s[df_s.columns[-2:][i]].astype(float), 'o', color ='red', alpha=1)
        ax[i].plot(df_s[df_s.columns[i]], 'o', color ='red', alpha=1)
        ax[i].set_title(df_s.columns[i])
        ax[i].set(xlabel='Time')
        ax[i].set(ylabel='Value')
        plt.draw()
        ax[i].set_xticklabels(ax[i].get_xticklabels(), rotation=30, ha='right')
        extent = ax[i].get_window_extent().transformed(fig.dpi_scale_trans.inverted())
        fig.savefig('pic/' + str(df_s.index.min().date()) +'_开机_'+ df_s.columns[i] + '.png', bbox_inches=extent.expanded(1.1, 1.17))


# ## 以下是关机数据预处理
# 
# #### 对于关机预测的数据，我们需要筛选出第一次脱离（30±2°C，70%±5%)的 Δt_close

# In[19]:


#接下来，我们需要根据每一次关机的时间点后至第一次脱离（30°C±2°，70%±5%）时间点以前的时间段，把每两分钟的数据提取出来
def df_data_close_all_filter(biaoleng_path,huifeng_T_path,fan_elec_path,outdoor_TH_path):

    global df_data_filter_close
    df_data_filter_close = pd.DataFrame()

    df_data_close_select = df_data_open_close(biaoleng_path,huifeng_T_path,fan_elec_path,outdoor_TH_path)[1]

    T_standard_min = 25
    T_standard_max = 35

    H_standard_min = 65
    H_standard_max = 75

    for i in range(len(df_data_close_select.index)):
        df_s = df_data[(df_data.index.to_frame()['时间'] >= df_data_close_select.index[i])]
        df_s_Inrange = df_s[(df_s.Avg_T < T_standard_min) | (df_s.Avg_T > T_standard_max) | (df_s.Avg_H < H_standard_min) | (df_s.Avg_H > H_standard_max)]
        df_s['关机时间'] = df_data_close_select.index[i]
        df_s['第一次脱离标准时间'] = df_s_Inrange.index.min()
    #     df_s = df_s[df_s.index <= df_s_Inrange.index.min()]
        df_s['Δt_close'] = df_s['第一次脱离标准时间'] - df_s.index

        df_data_filter_close = pd.concat([df_data_filter_close,df_s], axis=0)

    return df_data_filter_close


# In[20]:


def df_close_select(biaoleng_path,huifeng_T_path,fan_elec_path,outdoor_TH_path):
    
    df_data_filter_close = df_data_close_all_filter(biaoleng_path,huifeng_T_path,fan_elec_path,outdoor_TH_path)
    output_close = df_data_filter_close[df_data_filter_close.index == df_data_filter_close['关机时间']]
    output_close = output_close[['Avg_T','Avg_H','关机时间','Δt_close']]
    
    return output_close


# In[21]:


# #加入现在天气预报数据到最终模型数据里：

def df_data_closeModel(biaoleng_path,huifeng_T_path,fan_elec_path,outdoor_TH_path,outdoor_weather_path):

    output_close = df_close_select(biaoleng_path,huifeng_T_path,fan_elec_path,outdoor_TH_path)
    outdoor_weather = Outdoor_weather_Import(outdoor_weather_path)

    output_close['天气预报时间'] = output_close.index.values
    time_index = output_close.index.to_series()
    output_close['天气预报时间'][time_index.dt.minute >= 30] = time_index[time_index.dt.minute >= 30] + pd.Timedelta(hours=1)

    output_close['天气预报时间_现在'] = output_close['天气预报时间'].dt.floor('h')
    
    # 根据测量数据的时间点选取需要的天气预报数据
    weather_time_now = output_close['天气预报时间_现在'].unique()
    weather_time_future =[]

    #只选取未来4小时以内的天气数据
    for i in range(5):
        weather_time_future.extend(weather_time_now + pd.Timedelta(hours=i))

    outdoor_weather_select = outdoor_weather[outdoor_weather.index.isin(weather_time_future)] 

    # 对于天气预报，我们只考虑温度和相对湿度的数据
    outdoor_weather_select = outdoor_weather_select[['温度℃','相对湿度%']]
    
    df_output_close = output_close.reset_index()
    df_outdoor_weather = outdoor_weather.reset_index()

    df_output_close = df_output_close.merge(df_outdoor_weather, left_on='天气预报时间_现在', right_on='时间')
    df_output_close = df_output_close.drop(['时间_x','时间_y','气压hPa','风向/度','风速m/s','降水mm','天气预报时间'],axis=1)

    df_output_close['Δt_close'] = df_output_close['Δt_close'].dt.seconds

    df_output_close.columns.values[-2:] = ['天气温度','天气湿度']
    
    today_string = datetime.datetime.today().strftime('%Y_%m_%d')
    df_output_close.to_csv('data_pre/close_data_' + today_string + '.csv',index=True)
    
    return df_output_close


# In[22]:


df_data_openModel(outdoor_weather_path,biaoleng_path,jialiao_path,huifeng_T_path,fan_elec_path,outdoor_TH_path)


# In[23]:


df_data_closeModel(biaoleng_path,huifeng_T_path,fan_elec_path,outdoor_TH_path,outdoor_weather_path)


# #### 数据可视化

# In[ ]:


# df_data_time= df_concat.set_index('时间')

# %matplotlib inline
# plt.rcParams['font.sans-serif']=['SimHei']
# plt.rcParams['axes.unicode_minus'] = False

# # plt.subplots_adjust(hspace=0.5)

# fig, ax = plt.subplots(len(df_data_time.columns),1, figsize=(15,220))

# for i in range(len(ax)):
#     ax[i].plot(df_data_time[df_data_time.columns[i]], 'o', color ='red', alpha=0.1)
#     ax[i].set_title(df_data_time.columns[i])
#     ax[i].set(xlabel='Time')
#     ax[i].set(ylabel='Value')
#     plt.draw()
#     ax[i].set_xticklabels(ax[i].get_xticklabels(), rotation=30, ha='right')
#     extent = ax[i].get_window_extent().transformed(fig.dpi_scale_trans.inverted())
#     fig.savefig('pic/' + df_data_time.columns[i] + '.png', bbox_inches=extent.expanded(1.1, 1.17))

# plt.tight_layout() 
# # plt.subplots_adjust(hspace=0.5)
# # plt.savefig("开机数据_3个月.png")


# 

# In[ ]:


# def magnify():
#     return [dict(selector="th", props=[("font-size", "7pt")]),
#             dict(selector="td", props=[('padding', "0em 0em")]),
#             dict(selector="th:hover", props=[("font-size", "12pt")]),
#             dict(selector="tr:hover td:hover", 
#                  props=[('max-width', '200px'), ('font-size', '12pt')])]


# In[ ]:


# corr = df_data_time.corr(method='spearman')
# corr.style.background_gradient(cmap='coolwarm', axis=1)\
#     .set_properties(**{'max-width': '80px', 'font-size': '10pt'})\
#     .set_caption("数据间相关性分析")\
#     .set_precision(2)\
#     .set_table_styles(magnify())
# # corr.style.background_gradient(cmap='coolwarm').set_precision(2).set_table_styles(magnify())


# In[ ]:


#### 额外的1-2月开关数据输入

# df_merge = pd.DataFrame()

# data_test = pd.read_csv('data/Odata/1231-221/T_steam.csv', encoding='utf-8')
# values=[]
# for i in data_test.values:
#     values.append(i[0].split(";"))

# columns_name=[]
# for i in data_test.columns[0].split(';'):
#     columns_name.append(i.replace('"',"").replace(" ",""))

# df_ = pd.DataFrame(values, columns=columns_name)
# df_.rename(columns={df_.columns[df_.columns.str.contains('Time')][0]:'时间'}, inplace = True)

# df_merge['时间'] = df_['时间']

# df_merge['时间'] = df_['时间']
# df_merge = pd.merge(df_, df_merge, on=('时间'))


# data_test = pd.read_csv('data/Odata/1231-221/H_steam.csv', encoding='utf-8')
# values=[]
# for i in data_test.values:
#     values.append(i[0].split(";"))

# columns_name=[]
# for i in data_test.columns[0].split(';'):
#     columns_name.append(i.replace('"',"").replace(" ",""))

# df_ = pd.DataFrame(values, columns=columns_name)
# df_.rename(columns={df_.columns[df_.columns.str.contains('Time')][0]:'时间'}, inplace = True)

# df_merge = pd.merge(df_, df_merge, on=('时间'))


# In[ ]:


# path = os.getcwd()
# files = os.listdir(path+"/data/Odata/1231-221/")
# files_csv = [f for f in files if f[-3:] == 'csv']

# for f in files_csv:
#     data_test = pd.read_csv('data/Odata/1231-221/'+ f, encoding='utf-8')
    
#     print(f + '数据size:{}'.format(data_test.shape))
    
#     values=[]
#     for i in data_test.values:
#         values.append(i[0].split(";"))

#     columns_name=[]
#     for i in data_test.columns[0].split(';'):
#         columns_name.append(i.replace('"',"").replace(" ",""))

#     df_ = pd.DataFrame(values, columns=columns_name)
#     df_.rename(columns={df_.columns[df_.columns.str.contains('Time')][0]:'时间'}, inplace = True)
    
#     df_merge = pd.merge(df_merge, df_, on=('时间'))
    
# # 移除掉 ValueY
# for i in df_merge.columns[1:]:
#     df_merge.rename(columns={i:i[:-6]}, inplace = True)

# # for i in df_merge.columns[1:5]:
# #     df_merge.rename(columns={i:i[5:]}, inplace = True)
# for i in df_merge.columns[df_merge.columns.str.contains('KZS5')]:
#     df_merge.rename(columns={i:i[5:]}, inplace = True)
    
# df_merge.rename(columns={'送风湿度1': '送风湿度'}, inplace = True)
# df_merge.rename(columns={'风机电流': '送风机电流'}, inplace = True)

# df_merge['时间'] = pd.to_datetime(df_merge['时间'])

