#A股票行情数据获取演示   https://github.com/mpquant/Ashare
from  Ashare import *
    
# 证券代码兼容多种格式 通达信，同花顺，聚宽
# sh000001 (000001.XSHG)    sz399006 (399006.XSHE)   sh600519 ( 600519.XSHG ) 

df=get_price('sh000001',frequency='1d',count=5)      #默认获取今天往前5天的日线行情
print('上证指数日线行情\n',df)

df=get_price('000001.XSHG',frequency='1d',count=5,end_date='2021-04-30')   #可以指定结束日期，获取历史行情
print('上证指数历史行情\n',df)
    
df=get_price('sh600519',frequency='15m',count=5)     #分钟线行情，只支持从当前时间往前推，可用'1m','5m','15m','30m','60m'
print('贵州茅台15分钟线\n',df)

df=get_price('600519.XSHG',frequency='60m',count=6)  #分钟线行情，只支持从当前时间往前推，可用'1m','5m','15m','30m','60m'
print('贵州茅台60分钟线\n',df)
