Python Device Control Lib: Lib interface between App & IOT HUB
Testing Environment:Windows 10/python 3.7.7

设备控制接口说明：

设备接口函数主要包括两个：

一、定制化命令接口函数：RunPLCCommand(self,commandtype,args)
   参数说明：
   commandtype：设备命令类型编号，每个编号对应一个具体的命令
   args：字符串数组类型的动态参数，参数示例：["110","120"]，传入两个参数值110和120

二、自定义命令接口函数：RunPLCCommand2(self,command)
    1.参数说明：
	string command： json格式的命令参数
	2.命令格式说明：
	Address:PLC点位标签地址（用于写入）
	DataType: PLC点位数据类型
	Value: PLC点位写入值（没有检查值时默认写入以后再读取比对）
	CheckAddress: PLC点位标签地址（用于读取检查）
	CheckDataType:PLC点位数据类型
	CheckValue:PLC点位检查值
	3.命令使用说明：
	情形1：写入一个点位，并且在写入以后读取该点位的值用来确认是否写入成功，这个时候只需要设置Address,DataType,Value三个值。
	情形2：写入一个点位，从另一个点位读取值判断是否写入成功：这个时候Address,DataType,Value用于写入，CheckAddress,CheckDataType,CheckValue用于读取对比，其中从CheckAddress读取的值必需跟CheckValue值一致才算成功。
	情形3：不写入点位，只读取点位的值：这个时候仅使用CheckAddress,CheckDataType,CheckValue，其中CheckValue可不填写。
	4.参数示例：
	[{"Address":"5H.5H.LD5_test1","DataType":"float","Value":"11","CheckAddress":null,"CheckDataType":null,"CheckValue":null},{"Address":"5H.5H.LD5_test2","DataType":"float","Value":"100","CheckAddress":null,"CheckDataType":null,"CheckValue":null}]
          

定制化命令详细说明：
    初始化CommandHandler：
    url = "http://10.114.147.6/api/PLC/SetPLC"
    handler = CommandHandler(url)


  1.接口需求：2.1.	五千线烘丝机筒壁1区、2区温度控制流程
    接口功能：设置五千线烘丝机筒壁1区、2区温度设定值
    命令类型编号：ML_5K_HS_TB_WD_SET_ALL
    参数说明：args[0]:1区温度,args[1]:2区温度
    调用示例：res = handler.RunPLCCommand(DeviceCommandTypes.ML_5K_HS_TB_WD_SET_ALL, ["100","100"])

  2.接口需求：2.1.	五千线烘丝机筒壁1区、2区温度控制流程
    接口功能：恢复五千线烘丝机筒壁1区、2区温度设定值
    命令类型编号：ML_5K_HS_TB_WD_RESET_ALL
    参数说明：args[0]:1区温度,args[1]:2区温度
    调用示例：res = handler.RunPLCCommand(DeviceCommandTypes.ML_5K_HS_TB_WD_RESET_ALL, ["100","100"])

  3.接口需求：2.1.	五千线烘丝机筒壁1区、2区温度控制流程
    接口功能：设置五千线烘丝机筒壁1区、2区温度,读取HMI判断
    命令类型编号：ML_5K_HS_TB_WD_READ_HMI
    参数说明：无参数
    调用示例：res = handler.RunPLCCommand(DeviceCommandTypes.ML_5K_HS_TB_WD_READ_HMI, [])

  4.接口需求：2.1.	五千线烘丝机筒壁1区、2区温度控制流程
    接口功能：读取当前五千线烘丝机筒壁1区、2区温度
    命令类型编号：ML_5K_HS_TB_WD_READ_TEMPS
    参数说明：无参数
    调用示例：res = handler.RunPLCCommand(DeviceCommandTypes.ML_5K_HS_TB_WD_READ_TEMPS, [])

  5.接口需求：2.1.	五千线烘丝机筒壁1区、2区温度控制流程
    接口功能：设置当前五千线烘丝机筒壁1区、2区温度,不执行切换
    命令类型编号：ML_5K_HS_TB_WD_SET_TEMPS
    参数说明：args[0]:设置1区温度,args[1]:设置2区温度
    调用示例：res = handler.RunPLCCommand(DeviceCommandTypes.ML_5K_HS_TB_WD_SET_TEMPS, ["100","100"])

  6.接口需求：2.1.	五千线烘丝机筒壁1区、2区温度控制流程
    接口功能：设置当前五千线烘丝机筒壁1区、2区正向控制除水      
    命令类型编号：ML_5K_HS_TB_WD_SET_TIC_COS
    参数说明：args[0]:设置1区正向控制除水,args[1]:设置2区正向控制除水
    调用示例：res = handler.RunPLCCommand(DeviceCommandTypes.ML_5K_HS_TB_WD_SET_TIC_COS, ["100","100"])

  7.接口需求：2.1.	五千线烘丝机筒壁1区、2区温度控制流程
    接口功能：设置五千线烘丝机筒壁1区、2区温度,切换到Hauni手工
    命令类型编号：ML_5K_HS_TB_WD_SWITCH_MAN
    参数说明：无参数
    调用示例：res = handler.RunPLCCommand(DeviceCommandTypes.ML_5K_HS_TB_WD_SWITCH_MAN, [])

  8.接口需求：2.1.	五千线烘丝机筒壁1区、2区温度控制流程
    接口功能：设置五千线烘丝机筒壁1区、2区温度,切换到Hauni自动  
    命令类型编号：ML_5K_HS_TB_WD_SWITCH_AUTO
    参数说明：无参数
    调用示例：res = handler.RunPLCCommand(DeviceCommandTypes.ML_5K_HS_TB_WD_SWITCH_AUTO, [])

  9.接口需求：test
    接口功能：SIM_TEST_D1_T1
    命令类型编号：SIM_TEST_D1_T1
    参数说明：args[0]:测试点位1,ML
    调用示例：res = handler.RunPLCCommand(DeviceCommandTypes.SIM_TEST_D1_T1, ["100"])

  10.接口需求：test
    接口功能：SIM_TEST_D1_T2
    命令类型编号：SIM_TEST_D1_T2
    参数说明：args[0]:测试点位2,ML
    调用示例：res = handler.RunPLCCommand(DeviceCommandTypes.SIM_TEST_D1_T2, ["100"])

  11.接口需求：test
    接口功能：SIM_TEST_D1_T4
    命令类型编号：SIM_TEST_D1_T4
    参数说明：args[0]:测试点位3,APP
    调用示例：res = handler.RunPLCCommand(DeviceCommandTypes.SIM_TEST_D1_T4, ["100"])

  12.接口需求：test
    接口功能：ML_5H_5H_LD5_TEST_SET_ALL
    命令类型编号：ML_5H_5H_LD5_TEST_SET_ALL
    参数说明：args[0]:设置五千线烘丝机筒壁1区、2区温度测试值设定test1,args[1]:设置五千线烘丝机筒壁1区、2区温度测试值设定test2
    调用示例：res = handler.RunPLCCommand(DeviceCommandTypes.ML_5H_5H_LD5_TEST_SET_ALL, ["100","100"])

  13.接口需求：test
    接口功能：ML_5H_5H_LD5_TEST_RESET_ALL
    命令类型编号：ML_5H_5H_LD5_TEST_RESET_ALL
    参数说明：args[0]:恢复五千线烘丝机筒壁1区、2区温度测试值恢复test1,args[1]:恢复五千线烘丝机筒壁1区、2区温度测试值恢复test2
    调用示例：res = handler.RunPLCCommand(DeviceCommandTypes.ML_5H_5H_LD5_TEST_RESET_ALL, ["100","100"])

  14.接口需求：3.1.	烟叶回潮
    接口功能：3.1.1.	设置烟叶回潮流量
    命令类型编号：ZZ_5K_HS_YYHC_SET_YYHCLL
    参数说明：args[0]:烟叶回潮流量
    调用示例：res = handler.RunPLCCommand(DeviceCommandTypes.ZZ_5K_HS_YYHC_SET_YYHCLL, ["100"])

  15.接口需求：3.1.	烟叶回潮
    接口功能：3.1.2.	设置水分仪通道号
    命令类型编号：ZZ_5K_HS_YYHC_SET_SFYTDH
    参数说明：args[0]:水分仪通道号3375,args[1]:水分仪通道号2118
    调用示例：res = handler.RunPLCCommand(DeviceCommandTypes.ZZ_5K_HS_YYHC_SET_SFYTDH, ["sample","sample"])

  16.接口需求：3.1.	烟叶回潮
    接口功能：3.1.3.	设置热风温度
    命令类型编号：ZZ_5K_HS_YYHC_SET_RFWD
    参数说明：args[0]:热风温度
    调用示例：res = handler.RunPLCCommand(DeviceCommandTypes.ZZ_5K_HS_YYHC_SET_RFWD, ["100"])

  17.接口需求：3.1.	烟叶回潮
    接口功能：3.1.4.	设置入口水分
    命令类型编号：ZZ_5K_HS_YYHC_SET_RKSF
    参数说明：args[0]:入口水分
    调用示例：res = handler.RunPLCCommand(DeviceCommandTypes.ZZ_5K_HS_YYHC_SET_RKSF, ["100"])

  18.接口需求：3.1.	烟叶回潮
    接口功能：3.1.5.	设置出口水分
    命令类型编号：ZZ_5K_HS_YYHC_SET_CKSF
    参数说明：args[0]:出口水分
    调用示例：res = handler.RunPLCCommand(DeviceCommandTypes.ZZ_5K_HS_YYHC_SET_CKSF, ["100"])

  19.接口需求：3.1.	烟叶回潮
    接口功能：3.1.6.	设置加水系数
    命令类型编号：ZZ_5K_HS_YYHC_SET_JSXS
    参数说明：args[0]:加水系数
    调用示例：res = handler.RunPLCCommand(DeviceCommandTypes.ZZ_5K_HS_YYHC_SET_JSXS, ["100"])

  20.接口需求：3.1.	烟叶回潮
    接口功能：3.1.7.	设置真空电子秤流量
    命令类型编号：ZZ_5K_HS_YYHC_SET_ZKDZCLL
    参数说明：args[0]:真空电子秤流量
    调用示例：res = handler.RunPLCCommand(DeviceCommandTypes.ZZ_5K_HS_YYHC_SET_ZKDZCLL, ["100"])

  21.接口需求：3.2.	薄片回潮
    接口功能：3.2.1.	设置薄片回潮流量
    命令类型编号：ZZ_5K_HS_BPHC_SET_BPHCLL
    参数说明：args[0]:薄片回潮流量
    调用示例：res = handler.RunPLCCommand(DeviceCommandTypes.ZZ_5K_HS_BPHC_SET_BPHCLL, ["100"])

  22.接口需求：3.2.	薄片回潮
    接口功能：3.2.2.	设置水分仪通道号
    命令类型编号：ZZ_5K_HS_BPHC_SET_SFYTDH
    参数说明：args[0]:水分仪通道号2124,args[1]:水分仪通道号2129
    调用示例：res = handler.RunPLCCommand(DeviceCommandTypes.ZZ_5K_HS_BPHC_SET_SFYTDH, ["sample","sample"])

  23.接口需求：3.2.	薄片回潮
    接口功能：3.2.3.	设置热风温度
    命令类型编号：ZZ_5K_HS_BPHC_SET_RFWD
    参数说明：args[0]:热风温度
    调用示例：res = handler.RunPLCCommand(DeviceCommandTypes.ZZ_5K_HS_BPHC_SET_RFWD, ["100"])

  24.接口需求：3.2.	薄片回潮
    接口功能：3.2.4.	设置入口水分
    命令类型编号：ZZ_5K_HS_BPHC_SET_RKSF
    参数说明：args[0]:入口水分
    调用示例：res = handler.RunPLCCommand(DeviceCommandTypes.ZZ_5K_HS_BPHC_SET_RKSF, ["100"])

  25.接口需求：3.2.	薄片回潮
    接口功能：3.2.5.	设置出口水分
    命令类型编号：ZZ_5K_HS_BPHC_SET_CKSF
    参数说明：args[0]:出口水分
    调用示例：res = handler.RunPLCCommand(DeviceCommandTypes.ZZ_5K_HS_BPHC_SET_CKSF, ["100"])

  26.接口需求：3.2.	薄片回潮
    接口功能：3.2.6.	设置加水比例
    命令类型编号：ZZ_5K_HS_BPHC_SET_JSBL
    参数说明：args[0]:加水比例
    调用示例：res = handler.RunPLCCommand(DeviceCommandTypes.ZZ_5K_HS_BPHC_SET_JSBL, ["100"])

  27.接口需求：3.2.	薄片回潮
    接口功能：3.2.7.	设置出口水分上限设定值
    命令类型编号：ZZ_5K_HS_BPHC_SET_CKSFSX
    参数说明：args[0]:出口水分上限设定值
    调用示例：res = handler.RunPLCCommand(DeviceCommandTypes.ZZ_5K_HS_BPHC_SET_CKSFSX, ["100"])

  28.接口需求：3.2.	薄片回潮
    接口功能：3.2.8.	设置出口水分下限设定值
    命令类型编号：ZZ_5K_HS_BPHC_SET_CKSFXX
    参数说明：args[0]:出口水分下限设定值
    调用示例：res = handler.RunPLCCommand(DeviceCommandTypes.ZZ_5K_HS_BPHC_SET_CKSFXX, ["100"])

  29.接口需求：3.2.	薄片回潮
    接口功能：3.2.9.	设置入口水分比例设定值
    命令类型编号：ZZ_5K_HS_BPHC_SET_CKSFBL
    参数说明：args[0]:入口水分比例设定值
    调用示例：res = handler.RunPLCCommand(DeviceCommandTypes.ZZ_5K_HS_BPHC_SET_CKSFBL, ["100"])

  30.接口需求：3.2.	薄片回潮
    接口功能：3.2.10.	头料加水量
    命令类型编号：ZZ_5K_HS_BPHC_SET_TLJSL
    参数说明：args[0]:头料加水量
    调用示例：res = handler.RunPLCCommand(DeviceCommandTypes.ZZ_5K_HS_BPHC_SET_TLJSL, ["100"])

  31.接口需求：3.2.	薄片回潮
    接口功能：3.2.11.	设置尾料加水量
    命令类型编号：ZZ_5K_HS_BPHC_SET_WLJSL
    参数说明：args[0]:尾料加水量
    调用示例：res = handler.RunPLCCommand(DeviceCommandTypes.ZZ_5K_HS_BPHC_SET_WLJSL, ["100"])

  32.接口需求：3.3.	加料
    接口功能：3.3.1.	设置烟叶流量
    命令类型编号：ZZ_5K_HS_JL_SET_YYLL
    参数说明：args[0]:烟叶流量
    调用示例：res = handler.RunPLCCommand(DeviceCommandTypes.ZZ_5K_HS_JL_SET_YYLL, ["100"])

  33.接口需求：3.3.	加料
    接口功能：3.3.2.	设置水分仪通道号
    命令类型编号：ZZ_5K_HS_JL_SET_SFYTDH
    参数说明：args[0]:水分仪通道号2143A,args[1]:水分仪通道号2151
    调用示例：res = handler.RunPLCCommand(DeviceCommandTypes.ZZ_5K_HS_JL_SET_SFYTDH, ["sample","sample"])

  34.接口需求：3.3.	加料
    接口功能：3.3.3.	设置加料比例
    命令类型编号：ZZ_5K_HS_JL_SET_JLBL
    参数说明：args[0]:加料比例
    调用示例：res = handler.RunPLCCommand(DeviceCommandTypes.ZZ_5K_HS_JL_SET_JLBL, ["100"])

  35.接口需求：3.3.	加料
    接口功能：3.3.4.	设置热风温度
    命令类型编号：ZZ_5K_HS_JL_SET_RFWD
    参数说明：args[0]:热风温度
    调用示例：res = handler.RunPLCCommand(DeviceCommandTypes.ZZ_5K_HS_JL_SET_RFWD, ["100"])

  36.接口需求：3.3.	加料
    接口功能：3.3.5.	设置料桶1温度
    命令类型编号：ZZ_5K_HS_JL_SET_LT1WD
    参数说明：args[0]:料桶1温度
    调用示例：res = handler.RunPLCCommand(DeviceCommandTypes.ZZ_5K_HS_JL_SET_LT1WD, ["100"])

  37.接口需求：3.3.	加料
    接口功能：3.3.6.	设置料桶2温度
    命令类型编号：ZZ_5K_HS_JL_SET_LT2WD
    参数说明：args[0]:料桶2温度
    调用示例：res = handler.RunPLCCommand(DeviceCommandTypes.ZZ_5K_HS_JL_SET_LT2WD, ["100"])

  38.接口需求：3.3.	加料
    接口功能：3.3.7.	设置头料修正系数
    命令类型编号：ZZ_5K_HS_JL_SET_TLXZXS
    参数说明：args[0]:头料修正系数
    调用示例：res = handler.RunPLCCommand(DeviceCommandTypes.ZZ_5K_HS_JL_SET_TLXZXS, ["100"])

  39.接口需求：3.3.	加料
    接口功能：3.3.8.	设置尾料修正系数
    命令类型编号：ZZ_5K_HS_JL_SET_WLXZXS
    参数说明：args[0]:尾料修正系数
    调用示例：res = handler.RunPLCCommand(DeviceCommandTypes.ZZ_5K_HS_JL_SET_WLXZXS, ["100"])

  40.接口需求：3.3.	加料
    接口功能：3.3.9.	设置尾料流量
    命令类型编号：ZZ_5K_HS_JL_SET_WLLL
    参数说明：args[0]:尾料流量
    调用示例：res = handler.RunPLCCommand(DeviceCommandTypes.ZZ_5K_HS_JL_SET_WLLL, ["100"])

  41.接口需求：3.3.	加料
    接口功能：3.3.10.	设置加水系数
    命令类型编号：ZZ_5K_HS_JL_SET_JSXS
    参数说明：args[0]:加水系数
    调用示例：res = handler.RunPLCCommand(DeviceCommandTypes.ZZ_5K_HS_JL_SET_JSXS, ["100"])

  42.接口需求：3.3.	加料
    接口功能：3.3.11.	设置加水比例
    命令类型编号：ZZ_5K_HS_JL_SET_JSBL
    参数说明：args[0]:加水比例
    调用示例：res = handler.RunPLCCommand(DeviceCommandTypes.ZZ_5K_HS_JL_SET_JSBL, ["100"])

  43.接口需求：3.3.	加料
    接口功能：3.3.12.	设置出口含水量
    命令类型编号：ZZ_5K_HS_JL_SET_CKHSL
    参数说明：args[0]:出口含水量
    调用示例：res = handler.RunPLCCommand(DeviceCommandTypes.ZZ_5K_HS_JL_SET_CKHSL, ["100"])

  44.接口需求：3.3.	加料
    接口功能：3.3.13.	设置带速范围
    命令类型编号：ZZ_5K_HS_JL_SET_DSFW
    参数说明：
    调用示例：res = handler.RunPLCCommand(DeviceCommandTypes.ZZ_5K_HS_JL_SET_DSFW, [])

  45.接口需求：3.3.	加料
    接口功能：3.3.14.	设置要料重量
    命令类型编号：ZZ_5K_HS_JL_READ_YLAN
    参数说明：无参数
    调用示例：res = handler.RunPLCCommand(DeviceCommandTypes.ZZ_5K_HS_JL_READ_YLAN, [])

  46.接口需求：3.3.	加料
    接口功能：3.3.14.	设置要料重量
    命令类型编号：ZZ_5K_HS_JL_SET_LTXZ1
    参数说明：args[0]:料筒1要料重量
    调用示例：res = handler.RunPLCCommand(DeviceCommandTypes.ZZ_5K_HS_JL_SET_LTXZ1, ["sample"])

  47.接口需求：3.3.	加料
    接口功能：3.3.14.	设置要料重量
    命令类型编号：ZZ_5K_HS_JL_SET_LTXZ2
    参数说明：args[0]:料筒2要料重量
    调用示例：res = handler.RunPLCCommand(DeviceCommandTypes.ZZ_5K_HS_JL_SET_LTXZ2, ["sample"])

  48.接口需求：3.3.	加料
    接口功能：3.3.15.	设置料液代码
    命令类型编号：ZZ_5K_HS_JL_READ_LYAN
    参数说明：无参数
    调用示例：res = handler.RunPLCCommand(DeviceCommandTypes.ZZ_5K_HS_JL_READ_LYAN, [])

  49.接口需求：3.3.	加料
    接口功能：3.3.15.	设置料液代码
    命令类型编号：ZZ_5K_HS_JL_SET_LYDM1
    参数说明：args[0]:料筒1料液代码
    调用示例：res = handler.RunPLCCommand(DeviceCommandTypes.ZZ_5K_HS_JL_SET_LYDM1, ["sample"])

  50.接口需求：3.3.	加料
    接口功能：3.3.15.	设置料液代码
    命令类型编号：ZZ_5K_HS_JL_SET_LYDM2
    参数说明：args[0]:料筒2料液代码
    调用示例：res = handler.RunPLCCommand(DeviceCommandTypes.ZZ_5K_HS_JL_SET_LYDM2, ["sample"])

  51.接口需求：3.4.	烘丝 
    接口功能：3.4.1.	设置来料流量
    命令类型编号：ZZ_5K_HS_HS_SET_LLLL
    参数说明：args[0]:来料流量
    调用示例：res = handler.RunPLCCommand(DeviceCommandTypes.ZZ_5K_HS_HS_SET_LLLL, ["100"])

  52.接口需求：3.4.	烘丝 
    接口功能：3.4.3.	设置SIROX蒸汽流量
    命令类型编号：ZZ_5K_HS_HS_SET_SIROX
    参数说明：args[0]:SIROX蒸汽流量
    调用示例：res = handler.RunPLCCommand(DeviceCommandTypes.ZZ_5K_HS_HS_SET_SIROX, ["100"])

  53.接口需求：3.4.	烘丝 
    接口功能：3.4.3.	设置热风风速
    命令类型编号：ZZ_5K_HS_HS_SET_RFFS
    参数说明：args[0]:热风风速
    调用示例：res = handler.RunPLCCommand(DeviceCommandTypes.ZZ_5K_HS_HS_SET_RFFS, ["100"])

  54.接口需求：3.4.	烘丝 
    接口功能：3.4.4.	设置热风温度
    命令类型编号：ZZ_5K_HS_HS_SET_RFWD
    参数说明：args[0]:热风温度
    调用示例：res = handler.RunPLCCommand(DeviceCommandTypes.ZZ_5K_HS_HS_SET_RFWD, ["100"])

  55.接口需求：3.4.	烘丝 
    接口功能：3.4.5.	设置出口水分
    命令类型编号：ZZ_5K_HS_HS_SET_CKSF
    参数说明：args[0]:出口水分
    调用示例：res = handler.RunPLCCommand(DeviceCommandTypes.ZZ_5K_HS_HS_SET_CKSF, ["100"])

  56.接口需求：3.4.	烘丝 
    接口功能：3.4.6.	设置水分仪通道
    命令类型编号：ZZ_5K_HS_HS_SET_SFYTD
    参数说明：args[0]:通道1,args[1]:通道2
    调用示例：res = handler.RunPLCCommand(DeviceCommandTypes.ZZ_5K_HS_HS_SET_SFYTD, ["sample","sample"])

  57.接口需求：3.4.	烘丝 
    接口功能：3.4.7.	设置脱水速度
    命令类型编号：ZZ_5K_HS_HS_SET_TSSD
    参数说明：args[0]:脱水速度
    调用示例：res = handler.RunPLCCommand(DeviceCommandTypes.ZZ_5K_HS_HS_SET_TSSD, ["100"])

  58.接口需求：3.5.	回潮/加料/烘丝
    接口功能：3.5.1.	设置回潮组合启动
    命令类型编号：ZZ_5K_HS_HCJLHS_SET_HCZHQD
    参数说明：无参数
    调用示例：res = handler.RunPLCCommand(DeviceCommandTypes.ZZ_5K_HS_HCJLHS_SET_HCZHQD, [])

  59.接口需求：3.5.	回潮/加料/烘丝
    接口功能：3.5.1.	设置加料组合启动:料筒1选择
    命令类型编号：ZZ_5K_HS_HCJLHS_READ_JLZHQD_LT1XZ
    参数说明：无参数
    调用示例：res = handler.RunPLCCommand(DeviceCommandTypes.ZZ_5K_HS_HCJLHS_READ_JLZHQD_LT1XZ, [])

  60.接口需求：3.5.	回潮/加料/烘丝
    接口功能：3.5.1.	设置加料组合启动:料筒1重量
    命令类型编号：ZZ_5K_HS_HCJLHS_READ_JLZHQD_LT1ZL
    参数说明：无参数
    调用示例：res = handler.RunPLCCommand(DeviceCommandTypes.ZZ_5K_HS_HCJLHS_READ_JLZHQD_LT1ZL, [])

  61.接口需求：3.5.	回潮/加料/烘丝
    接口功能：3.5.1.	设置加料组合启动:料筒2选择
    命令类型编号：ZZ_5K_HS_HCJLHS_READ_JLZHQD_LT2XZ
    参数说明：无参数
    调用示例：res = handler.RunPLCCommand(DeviceCommandTypes.ZZ_5K_HS_HCJLHS_READ_JLZHQD_LT2XZ, [])

  62.接口需求：3.5.	回潮/加料/烘丝
    接口功能：3.5.1.	设置加料组合启动:料筒2重量
    命令类型编号：ZZ_5K_HS_HCJLHS_READ_JLZHQD_LT2ZL
    参数说明：无参数
    调用示例：res = handler.RunPLCCommand(DeviceCommandTypes.ZZ_5K_HS_HCJLHS_READ_JLZHQD_LT2ZL, [])

  63.接口需求：3.5.	回潮/加料/烘丝
    接口功能：3.5.1.	设置加料组合启动
    命令类型编号：ZZ_5K_HS_HCJLHS_SET_JLZHQD
    参数说明：无参数
    调用示例：res = handler.RunPLCCommand(DeviceCommandTypes.ZZ_5K_HS_HCJLHS_SET_JLZHQD, [])

  64.接口需求：3.5.	回潮/加料/烘丝
    接口功能：3.5.1.	设置切丝组合启动
    命令类型编号：ZZ_5K_HS_HCJLHS_SET_QSZHQD
    参数说明：无参数
    调用示例：res = handler.RunPLCCommand(DeviceCommandTypes.ZZ_5K_HS_HCJLHS_SET_QSZHQD, [])

  65.接口需求：3.5.	回潮/加料/烘丝
    接口功能：3.5.1.	设置烘丝组合启动
    命令类型编号：ZZ_5K_HS_HCJLHS_SET_HSZHQD
    参数说明：无参数
    调用示例：res = handler.RunPLCCommand(DeviceCommandTypes.ZZ_5K_HS_HCJLHS_SET_HSZHQD, [])

  66.接口需求：3.5.	回潮/加料/烘丝
    接口功能：3.5.2.	设置组合停止：回潮组合停止
    命令类型编号：ZZ_5K_HS_HCJLHS_SET_HCZHTZ
    参数说明：无参数
    调用示例：res = handler.RunPLCCommand(DeviceCommandTypes.ZZ_5K_HS_HCJLHS_SET_HCZHTZ, [])

  67.接口需求：3.5.	回潮/加料/烘丝
    接口功能：3.5.2.	设置组合停止：加料组合停止
    命令类型编号：ZZ_5K_HS_HCJLHS_SET_JLZHTZ
    参数说明：无参数
    调用示例：res = handler.RunPLCCommand(DeviceCommandTypes.ZZ_5K_HS_HCJLHS_SET_JLZHTZ, [])

  68.接口需求：3.5.	回潮/加料/烘丝
    接口功能：3.5.2.	设置组合停止：切丝段组合停止
    命令类型编号：ZZ_5K_HS_HCJLHS_SET_QSZHTZ
    参数说明：无参数
    调用示例：res = handler.RunPLCCommand(DeviceCommandTypes.ZZ_5K_HS_HCJLHS_SET_QSZHTZ, [])

  69.接口需求：3.5.	回潮/加料/烘丝
    接口功能：3.5.2.	设置组合停止：烘丝段组合停止
    命令类型编号：ZZ_5K_HS_HCJLHS_SET_HSZHTZ
    参数说明：无参数
    调用示例：res = handler.RunPLCCommand(DeviceCommandTypes.ZZ_5K_HS_HCJLHS_SET_HSZHTZ, [])

  70.接口需求：3.5.	回潮/加料/烘丝
    接口功能：3.5.3.	设置预热:回潮预热启动
    命令类型编号：ZZ_5K_HS_HCJLHS_SET_SZYR_HCYRQD
    参数说明：无参数
    调用示例：res = handler.RunPLCCommand(DeviceCommandTypes.ZZ_5K_HS_HCJLHS_SET_SZYR_HCYRQD, [])

  71.接口需求：3.5.	回潮/加料/烘丝
    接口功能：3.5.3.	设置预热:回潮预热停止
    命令类型编号：ZZ_5K_HS_HCJLHS_SET_SZYR_HCYRTZ
    参数说明：无参数
    调用示例：res = handler.RunPLCCommand(DeviceCommandTypes.ZZ_5K_HS_HCJLHS_SET_SZYR_HCYRTZ, [])

  72.接口需求：3.5.	回潮/加料/烘丝
    接口功能：3.5.3.	设置预热:加料预热启动
    命令类型编号：ZZ_5K_HS_HCJLHS_SET_SZYR_JLYRQD
    参数说明：无参数
    调用示例：res = handler.RunPLCCommand(DeviceCommandTypes.ZZ_5K_HS_HCJLHS_SET_SZYR_JLYRQD, [])

  73.接口需求：3.5.	回潮/加料/烘丝
    接口功能：3.5.3.	设置预热:加料预热停止
    命令类型编号：ZZ_5K_HS_HCJLHS_SET_SZYR_JLYRTZ
    参数说明：无参数
    调用示例：res = handler.RunPLCCommand(DeviceCommandTypes.ZZ_5K_HS_HCJLHS_SET_SZYR_JLYRTZ, [])

  74.接口需求：3.5.	回潮/加料/烘丝
    接口功能：3.5.3.	5000烘丝机控制模式判断
    命令类型编号：ZZ_5K_HS_HCJLHS_READ_KZMS
    参数说明：无参数
    调用示例：res = handler.RunPLCCommand(DeviceCommandTypes.ZZ_5K_HS_HCJLHS_READ_KZMS, [])

  75.接口需求：3.5.	回潮/加料/烘丝
    接口功能：3.5.3.	设置预热:SIROX预热启动
    命令类型编号：ZZ_5K_HS_HCJLHS_SET_SZYR_SIROX_YRQD
    参数说明：无参数
    调用示例：res = handler.RunPLCCommand(DeviceCommandTypes.ZZ_5K_HS_HCJLHS_SET_SZYR_SIROX_YRQD, [])

  76.接口需求：3.5.	回潮/加料/烘丝
    接口功能：3.5.3.	设置预热:SIROX预热停止
    命令类型编号：ZZ_5K_HS_HCJLHS_SET_SZYR_SIROX_YRTZ
    参数说明：无参数
    调用示例：res = handler.RunPLCCommand(DeviceCommandTypes.ZZ_5K_HS_HCJLHS_SET_SZYR_SIROX_YRTZ, [])

  77.接口需求：3.5.	回潮/加料/烘丝
    接口功能：3.5.3.	设置预热:烘丝预热启动
    命令类型编号：ZZ_5K_HS_HCJLHS_SET_SZYR_HSYRQD
    参数说明：无参数
    调用示例：res = handler.RunPLCCommand(DeviceCommandTypes.ZZ_5K_HS_HCJLHS_SET_SZYR_HSYRQD, [])

  78.接口需求：3.5.	回潮/加料/烘丝
    接口功能：3.5.3.	设置预热:烘丝预热停止
    命令类型编号：ZZ_5K_HS_HCJLHS_SET_SZYR_HSYRTZ
    参数说明：无参数
    调用示例：res = handler.RunPLCCommand(DeviceCommandTypes.ZZ_5K_HS_HCJLHS_SET_SZYR_HSYRTZ, [])

  79.接口需求：3.5.	回潮/加料/烘丝
    接口功能：3.5.4.	设置冷却:烘丝冷却开始
    命令类型编号：ZZ_5K_HS_HCJLHS_SET_SZLQ_HSLQKS
    参数说明：无参数
    调用示例：res = handler.RunPLCCommand(DeviceCommandTypes.ZZ_5K_HS_HCJLHS_SET_SZLQ_HSLQKS, [])

  80.接口需求：3.5.	回潮/加料/烘丝
    接口功能：3.5.4.	设置冷却:烘丝冷却停止
    命令类型编号：ZZ_5K_HS_HCJLHS_SET_SZLQ_HSLQTZ
    参数说明：无参数
    调用示例：res = handler.RunPLCCommand(DeviceCommandTypes.ZZ_5K_HS_HCJLHS_SET_SZLQ_HSLQTZ, [])

  81.接口需求：3.5.	回潮/加料/烘丝
    接口功能：3.5.4.	设置冷却:SIROX冷却开始
    命令类型编号：ZZ_5K_HS_HCJLHS_SET_SZLQ_SIROXLQKS
    参数说明：无参数
    调用示例：res = handler.RunPLCCommand(DeviceCommandTypes.ZZ_5K_HS_HCJLHS_SET_SZLQ_SIROXLQKS, [])

  82.接口需求：3.5.	回潮/加料/烘丝
    接口功能：3.5.4.	设置冷却:SIROX冷却停止
    命令类型编号：ZZ_5K_HS_HCJLHS_SET_SZLQ_SIROXLQTZ
    参数说明：无参数
    调用示例：res = handler.RunPLCCommand(DeviceCommandTypes.ZZ_5K_HS_HCJLHS_SET_SZLQ_SIROXLQTZ, [])

  83.接口需求：3.5.	回潮/加料/烘丝
    接口功能：3.5.5.	设置生产停止:烘丝机生产开始
    命令类型编号：ZZ_5K_HS_HCJLHS_SET_SCTZ_HSSCKS
    参数说明：无参数
    调用示例：res = handler.RunPLCCommand(DeviceCommandTypes.ZZ_5K_HS_HCJLHS_SET_SCTZ_HSSCKS, [])

  84.接口需求：3.5.	回潮/加料/烘丝
    接口功能：3.5.5.	设置生产停止:烘丝机生产停止
    命令类型编号：ZZ_5K_HS_HCJLHS_SET_SCTZ_HSSCTZ
    参数说明：无参数
    调用示例：res = handler.RunPLCCommand(DeviceCommandTypes.ZZ_5K_HS_HCJLHS_SET_SCTZ_HSSCTZ, [])

  85.接口需求：3.5.	回潮/加料/烘丝
    接口功能：3.5.5.	设置生产停止:烘丝机生产暂停
    命令类型编号：ZZ_5K_HS_HCJLHS_SET_SCTZ_HSSCZT
    参数说明：无参数
    调用示例：res = handler.RunPLCCommand(DeviceCommandTypes.ZZ_5K_HS_HCJLHS_SET_SCTZ_HSSCZT, [])

  86.接口需求：3.5.	回潮/加料/烘丝
    接口功能：3.5.6.	设置复位
    命令类型编号：ZZ_5K_HS_HCJLHS_SET_SZFW
    参数说明：无参数
    调用示例：res = handler.RunPLCCommand(DeviceCommandTypes.ZZ_5K_HS_HCJLHS_SET_SZFW, [])

  87.接口需求：3.5.	回潮/加料/烘丝
    接口功能：3.5.7.	设置清洗:SIROX清洁开始
    命令类型编号：ZZ_5K_HS_HCJLHS_SET_SZQX_SIROXQJKS
    参数说明：无参数
    调用示例：res = handler.RunPLCCommand(DeviceCommandTypes.ZZ_5K_HS_HCJLHS_SET_SZQX_SIROXQJKS, [])

  88.接口需求：3.5.	回潮/加料/烘丝
    接口功能：3.5.7.	设置清洗:SIROX清洁停止
    命令类型编号：ZZ_5K_HS_HCJLHS_SET_SZQX_SIROXQJTZ
    参数说明：无参数
    调用示例：res = handler.RunPLCCommand(DeviceCommandTypes.ZZ_5K_HS_HCJLHS_SET_SZQX_SIROXQJTZ, [])

  89.接口需求：2.4.	回潮模型加水系数
    接口功能：智能模型输出加水系数
    命令类型编号：ML_5K_HS_HC_SET_JSXS
    参数说明：args[0]:智能模型输出加水系数,args[1]:智能模型输出（入口）,args[2]:智能模型输出（出口）,args[3]:智能模型输出
    调用示例：res = handler.RunPLCCommand(DeviceCommandTypes.ML_5K_HS_HC_SET_JSXS, ["100","sample","sample","100"])

  90.接口需求：2.5.	加料模型加水系数
    接口功能：智能模型输出加料模型加水系数
    命令类型编号：ML_5K_HS_JL_SET_JSXS
    参数说明：args[0]:加料模型加水系数,args[1]:智能模型输出
    调用示例：res = handler.RunPLCCommand(DeviceCommandTypes.ML_5K_HS_JL_SET_JSXS, ["100","100"])

  91.接口需求：2.5.	加料模型加水比例
    接口功能：智能模型输出加料模型加水比例
    命令类型编号：ML_5K_HS_JL_SET_JSBL
    参数说明：args[0]:料模型加水比例
    调用示例：res = handler.RunPLCCommand(DeviceCommandTypes.ML_5K_HS_JL_SET_JSBL, ["100"])

  92.接口需求：3.1.	烟叶回潮
    接口功能：3.1.8.	设置预配柜选柜打自动
    命令类型编号：ZZ_5K_HS_YYHC_SET_YPGXGDZD
    参数说明：无参数
    调用示例：res = handler.RunPLCCommand(DeviceCommandTypes.ZZ_5K_HS_YYHC_SET_YPGXGDZD, [])

  93.接口需求：3.1.	烟叶回潮
    接口功能：3.1.8.	设置预配柜选柜打自动--路径选择
    命令类型编号：ZZ_5K_HS_YYHC_SET_YPGLJXZ
    参数说明：无参数
    调用示例：res = handler.RunPLCCommand(DeviceCommandTypes.ZZ_5K_HS_YYHC_SET_YPGLJXZ, [])

  94.接口需求：3.3.	加料
    接口功能：3.3.16.	设置预配柜选柜打自动
    命令类型编号：ZZ_5K_HS_JL_SET_YPGXGDZD
    参数说明：无参数
    调用示例：res = handler.RunPLCCommand(DeviceCommandTypes.ZZ_5K_HS_JL_SET_YPGXGDZD, [])

  95.接口需求：3.3.	加料
    接口功能：3.3.18.	设置叶柜入柜状态自动
    命令类型编号：ZZ_5K_HS_JL_SET_YGRGZTZD
    参数说明：无参数
    调用示例：res = handler.RunPLCCommand(DeviceCommandTypes.ZZ_5K_HS_JL_SET_YGRGZTZD, [])

  96.接口需求：3.3.	加料
    接口功能：3.3.19.	设置叶柜选择路径
    命令类型编号：ZZ_5K_HS_JL_SET_YGXZLJ
    参数说明：无参数
    调用示例：res = handler.RunPLCCommand(DeviceCommandTypes.ZZ_5K_HS_JL_SET_YGXZLJ, [])

  97.接口需求：3.5.	回潮/加料/烘丝
    接口功能：3.5.8.	设置生产提升-加料生产提升
    命令类型编号：ZZ_5K_HS_HCJLHS_SET_SCTS_JLSCTS
    参数说明：无参数
    调用示例：res = handler.RunPLCCommand(DeviceCommandTypes.ZZ_5K_HS_HCJLHS_SET_SCTS_JLSCTS, [])

  98.接口需求：3.5.	回潮/加料/烘丝
    接口功能：3.5.8.	设置生产提升-加料强制停止
    命令类型编号：ZZ_5K_HS_HCJLHS_SET_SCTS_JLQZTZ
    参数说明：无参数
    调用示例：res = handler.RunPLCCommand(DeviceCommandTypes.ZZ_5K_HS_HCJLHS_SET_SCTS_JLQZTZ, [])

  99.接口需求：3.5.	回潮/加料/烘丝
    接口功能：3.5.8.	设置生产提升-加料强制提升
    命令类型编号：ZZ_5K_HS_HCJLHS_SET_SCTS_JLQZTS
    参数说明：无参数
    调用示例：res = handler.RunPLCCommand(DeviceCommandTypes.ZZ_5K_HS_HCJLHS_SET_SCTS_JLQZTS, [])

  100.接口需求：3.5.	回潮/加料/烘丝
    接口功能：3.5.8.	设置生产提升-薄片回潮生产提升
    命令类型编号：ZZ_5K_HS_HCJLHS_SET_SCTS_BPHCSCTS
    参数说明：无参数
    调用示例：res = handler.RunPLCCommand(DeviceCommandTypes.ZZ_5K_HS_HCJLHS_SET_SCTS_BPHCSCTS, [])

  101.接口需求：3.5.	回潮/加料/烘丝
    接口功能：3.5.8.	设置生产提升-薄片回潮强制停止
    命令类型编号：ZZ_5K_HS_HCJLHS_SET_SCTS_BPHCQZTZ
    参数说明：无参数
    调用示例：res = handler.RunPLCCommand(DeviceCommandTypes.ZZ_5K_HS_HCJLHS_SET_SCTS_BPHCQZTZ, [])

  102.接口需求：3.5.	回潮/加料/烘丝
    接口功能：3.5.8.	设置生产提升-薄片回潮强制提升
    命令类型编号：ZZ_5K_HS_HCJLHS_SET_SCTS_BPHCQZTS
    参数说明：无参数
    调用示例：res = handler.RunPLCCommand(DeviceCommandTypes.ZZ_5K_HS_HCJLHS_SET_SCTS_BPHCQZTS, [])

  103.接口需求：3.5.	回潮/加料/烘丝
    接口功能：3.5.8.	设置生产提升-回潮生产提升
    命令类型编号：ZZ_5K_HS_HCJLHS_SET_SCTS_HCSCTS
    参数说明：无参数
    调用示例：res = handler.RunPLCCommand(DeviceCommandTypes.ZZ_5K_HS_HCJLHS_SET_SCTS_HCSCTS, [])

  104.接口需求：3.5.	回潮/加料/烘丝
    接口功能：3.5.8.	设置生产提升-回潮强制停止
    命令类型编号：ZZ_5K_HS_HCJLHS_SET_SCTS_HCQZTZ
    参数说明：无参数
    调用示例：res = handler.RunPLCCommand(DeviceCommandTypes.ZZ_5K_HS_HCJLHS_SET_SCTS_HCQZTZ, [])

  105.接口需求：3.5.	回潮/加料/烘丝
    接口功能：3.5.8.	设置生产提升-回潮强制提升
    命令类型编号：ZZ_5K_HS_HCJLHS_SET_SCTS_HCQZTS
    参数说明：无参数
    调用示例：res = handler.RunPLCCommand(DeviceCommandTypes.ZZ_5K_HS_HCJLHS_SET_SCTS_HCQZTS, [])

  106.接口需求：3.5.	回潮/加料/烘丝
    接口功能：3.5.10.	批次号,工单号,牌号PLC点位信息下发
    命令类型编号：ZZ_5K_HS_HCJLHS_SET_PCHGDHPH_HC
    参数说明：args[0]:回潮批次号点位,args[1]:回潮工单号点位,args[2]:回潮牌号点位
    调用示例：res = handler.RunPLCCommand(DeviceCommandTypes.ZZ_5K_HS_HCJLHS_SET_PCHGDHPH_HC, ["sample","sample","sample"])

  107.接口需求：3.5.	回潮/加料/烘丝
    接口功能：3.5.10.	批次号,工单号,牌号PLC点位信息下发
    命令类型编号：ZZ_5K_HS_HCJLHS_SET_PCHGDHPH_JL
    参数说明：args[0]:加料批次号点位,args[1]:加料工单号点位,args[2]:加料牌号点位
    调用示例：res = handler.RunPLCCommand(DeviceCommandTypes.ZZ_5K_HS_HCJLHS_SET_PCHGDHPH_JL, ["sample","sample","sample"])

  108.接口需求：3.5.	回潮/加料/烘丝
    接口功能：3.5.10.	批次号,工单号,牌号PLC点位信息下发
    命令类型编号：ZZ_5K_HS_HCJLHS_SET_PCHGDHPH_BPHC
    参数说明：args[0]:薄片回潮批次号点位,args[1]:薄片回潮工单号点位,args[2]:薄片回潮牌号点位
    调用示例：res = handler.RunPLCCommand(DeviceCommandTypes.ZZ_5K_HS_HCJLHS_SET_PCHGDHPH_BPHC, ["sample","sample","sample"])

  109.接口需求：3.5.	回潮/加料/烘丝
    接口功能：3.5.11.	薄片回潮预热启停
    命令类型编号：ZZ_5K_HS_HCJLHS_SET_BPHCYL_Q
    参数说明：无参数
    调用示例：res = handler.RunPLCCommand(DeviceCommandTypes.ZZ_5K_HS_HCJLHS_SET_BPHCYL_Q, [])

  110.接口需求：3.5.	回潮/加料/烘丝
    接口功能：3.5.11.	薄片回潮预热启停
    命令类型编号：ZZ_5K_HS_HCJLHS_SET_BPHCYL_T
    参数说明：无参数
    调用示例：res = handler.RunPLCCommand(DeviceCommandTypes.ZZ_5K_HS_HCJLHS_SET_BPHCYL_T, [])

  111.接口需求：3.5.	回潮/加料/烘丝
    接口功能：3.5.13.	预配柜选柜，人工确认点位
    命令类型编号：ZZ_5K_HS_HCJLHS_Get_YPGXGRGQRDW_7
    参数说明：无参数
    调用示例：res = handler.RunPLCCommand(DeviceCommandTypes.ZZ_5K_HS_HCJLHS_Get_YPGXGRGQRDW_7, [])

  112.接口需求：3.5.	回潮/加料/烘丝
    接口功能：3.5.13.	预配柜选柜，人工确认点位
    命令类型编号：ZZ_5K_HS_HCJLHS_Get_YPGXGRGQRDW_6
    参数说明：无参数
    调用示例：res = handler.RunPLCCommand(DeviceCommandTypes.ZZ_5K_HS_HCJLHS_Get_YPGXGRGQRDW_6, [])

  113.接口需求：3.5.	回潮/加料/烘丝
    接口功能：3.5.13.	预配柜选柜，人工确认点位
    命令类型编号：ZZ_5K_HS_HCJLHS_Get_YPGXGRGQRDW_5
    参数说明：无参数
    调用示例：res = handler.RunPLCCommand(DeviceCommandTypes.ZZ_5K_HS_HCJLHS_Get_YPGXGRGQRDW_5, [])

  114.接口需求：3.5.	回潮/加料/烘丝
    接口功能：3.5.13.	预配柜选柜，人工确认点位
    命令类型编号：ZZ_5K_HS_HCJLHS_Get_YPGXGRGQRDW_4
    参数说明：无参数
    调用示例：res = handler.RunPLCCommand(DeviceCommandTypes.ZZ_5K_HS_HCJLHS_Get_YPGXGRGQRDW_4, [])

  115.接口需求：2.7.	空调模型阀门开度设定
    接口功能：控制流程
    命令类型编号：ML_5K_KTMX_FM_Set_KD
    参数说明：args[0]:输出空调模型加热阀开度设定,args[1]:空调模型加湿阀开度设定,args[2]:空调模型新风阀开度设定,args[3]:空调模型混风阀开度设定,args[4]:空调模型表冷阀开度设定01,args[5]:空调模型表冷阀开度设定02
    调用示例：res = handler.RunPLCCommand(DeviceCommandTypes.ML_5K_KTMX_FM_Set_KD, ["True","True","True","True","True","True"])

  116.接口需求：2.8.	空调模型送风机的频率开机设定
    接口功能：控制流程
    命令类型编号：ML_5K_KTMX_SFJ_Set_PLKJ
    参数说明：args[0]:智能模型输出
    调用示例：res = handler.RunPLCCommand(DeviceCommandTypes.ML_5K_KTMX_SFJ_Set_PLKJ, ["True"])

  117.接口需求：2.9.	空调模型送风机的频率关机设定
    接口功能：控制流程
    命令类型编号：ML_5K_KTMX_SFJ_Set_PLGJ
    参数说明：args[0]:智能模型输出
    调用示例：res = handler.RunPLCCommand(DeviceCommandTypes.ML_5K_KTMX_SFJ_Set_PLGJ, ["True"])
