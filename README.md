# qingdao_HVAC_Control

### 开关机预测模型

本地CSV数据预处理：run on_off_data_preprocessing.ipynb

再训练开机模型：run open_model_trainSave.ipynb
再训练关机模型：run close_model_trainSave.ipynb

开机时间点预测：run open_model_pred.ipynb
关机时间点预测：run close_model_pred.ipynb

### 温湿度预测模型

本地CSV数据预处理：run wentai_data_preprocessing.ipynb
再训练稳态温湿度预测模型：run wentai_HT_trainSave.ipynb
送风温湿度预测：run wentai_HT_pred.ipynb


#### 能耗预测分析

本地CSV数据预处理：run wentai_data_preprocessing.ipynb
再训练稳态能耗预测模型：run wentai_HT_trainSave.ipynb
能耗预测：run wentai_energy_pred.ipynb