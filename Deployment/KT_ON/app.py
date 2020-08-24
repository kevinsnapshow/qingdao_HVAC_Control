#!/usr/bin/env python
# coding: utf-8

# In[4]:


# !pip freeze > requirements.txt


# In[25]:


from flask import Flask
from flask import request 
from datetime import datetime
from on_real_pred import real_time_data_pre, load_model_predict

app = Flask(__name__)

@app.route('/predict', methods=['GET', 'POST'])
def do_predict():
    
    # 使用request解析jason形式的参数：
#     name = request.json.get('name')
    realtime_data = request.json
    
    # 定义工业安全系数：
    today_string = datetime.today().strftime('%Y_%m_%d')
    safety_factor = 0.5
    
    data_input_pre, entryStartTime_thre_ = real_time_data_pre(realtime_data)
    
    Δt_pred, timestamp_pred = load_model_predict(today_string, data_input_pre, safety_factor)
    
    if all(items > entryStartTime_thre_[0] for items in timestamp_pred.to_list()):
        action_required = 1
        print('The fan will be turned on now.')
    else:
        action_required = 0
        print('The fan will remain to be off.')
        
    return action_required

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=6500)

