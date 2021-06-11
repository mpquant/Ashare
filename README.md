# Ashare (免费 开源 极简 A股实时行情数据)

中国股市A股股票行情实时数据最简封装API接口,包含日线,分时分钟线,全部格式成DataFrame格式数据,可用来研究，量化分析，简单的自动化交易系统

功能特点
---
* 核心库轻量化： 项目库就一个文件Ashare.py,不用安装，不用设置，可自由裁剪，随用随走 ( from  Ashare import * 即可 )

* 内核封装的是腾讯股票的实时行情数据，包括日线，任意历史日线，分钟线，小时线等

* 全部数据格式清理成DataFrame格式数据，让您非常方便的使用pandas来分析和处理

* 和其他行情库（tushare等）比的优点是什么？ --  简单 轻量  便携  免费 开源

* Ashare把复杂的数据获取，拆分，整合逻辑全部封装成一个函数 `get_price()` 看完下面例子就会了 

* Ashare可以用在任何需要量化研究，量化分析的场合



### 先看一个最简单的例子 [Demo1.py](https://github.com/mpquant/Ashare/blob/main/Demo1.py)

```python
from  Ashare import *
    
# 证券代码兼容多种格式 通达信，同花顺，聚宽
# sh000001 (000001.XSHG)    sz399006 (399006.XSHE)   sh600519 ( 600519.XSHG ) 

df=get_price('sh000001',frequency='1d',count=5)      #默认获取今天往前5天的日线行情
print('上证指数日线行情\n',df)

df=get_price('000001.XSHG',frequency='1d',count=5,end_date='2021-04-30')  #可以指定结束日期，获取历史行情
print('上证指数历史行情\n',df)
    
df=get_price('sh600519',frequency='15m',count=5)     #分钟线行情，可用'1m','5m','15m','30m','60m'
print('贵州茅台15分钟线\n',df)

df=get_price('600519.XSHG',frequency='60m',count=6)  #分钟线行情，可用'1m','5m','15m','30m','60m'
print('贵州茅台60分钟线\n',df)
```



```
#上证指数日线行情----------------------------------------------------
              open    close     high      low       volume
2021-06-07  3597.14  3599.54  3600.38  3581.90  303718677.0
2021-06-08  3598.75  3580.11  3621.52  3563.25  304491470.0
2021-06-09  3576.80  3591.40  3598.71  3572.64  298323296.0
2021-06-10  3587.53  3610.86  3624.34  3584.13  318174808.0
2021-06-11  3614.11  3589.75  3614.40  3587.15  360554970.0


#贵州茅台60分钟线----------------------------------------------------
                       open    close     high      low    volume
2021-06-10 14:00:00  2237.00  2224.16  2245.00  2222.00   4541.53
2021-06-10 15:00:00  2222.21  2238.48  2240.34  2222.21   4146.88
2021-06-11 10:30:00  2239.00  2220.00  2244.00  2197.86  12030.00
2021-06-11 11:30:00  2220.01  2210.18  2231.80  2200.18   4868.00
2021-06-11 14:00:00  2210.10  2223.35  2224.48  2206.01   4544.00
2021-06-11 15:00:00  2223.33  2178.81  2226.80  2178.81  12529.00
```


### 再看一个配合[MyTT](https://github.com/mpquant/MyTT)的例子 [Demo2.py](https://github.com/mpquant/Ashare/blob/main/Demo2.py)

```python
#股市行情数据获取和作图 -2
from  Ashare import *          #股票数据库    https://github.com/mpquant/Ashare
from  MyTT import *            #myTT麦语言工具函数指标库  https://github.com/mpquant/MyTT
    
# 证券代码兼容多种格式 通达信，同花顺，聚宽
# sh000001 (000001.XSHG)    sz399006 (399006.XSHE)   sh600519 ( 600519.XSHG ) 

df=get_price('000001.XSHG',frequency='1d',count=120)      #获取今天往前120天的日线行情
print('上证指数日线行情\n',df.tail(5))

#-------有数据了，下面开始正题 -------------
# 也支持pd序列，列表,例如 CLOSE=df.close ,   CLOSE=list(df.close) 都是一样
CLOSE=df.close;         OPEN=df.open           #基础数据定义，只要传入的是序列都可以   
HIGH=df.high;           LOW=df.low             

MA5=MA(CLOSE,5)                                #获取5日均线序列
MA10=MA(CLOSE,10)                              #获取10日均线序列
up,mid,lower=BOLL(CLOSE)                       #获取布林带指标数据

#-------------------------作图显示-----------------------------------------------------------------
import matplotlib.pyplot as plt ;  from matplotlib.ticker import MultipleLocator
plt.figure(figsize=(15,8))  
plt.plot(CLOSE,label='SHZS');    plt.plot(up,label='UP');           #画图显示 
plt.plot(mid,label='MID');       plt.plot(lower,label='LOW');
plt.plot(MA10,label='MA10',linewidth=0.5,alpha=0.7);
plt.show()
```

<div  align="center"> <img src="/img/sh_boll.png" width = "960" height = "480" alt="boll" /> </div>


----------------------------------------------------
### 团队其他开源项目
* [MyTT 通达信,同花顺公式指标，文华麦语言的python实现](https://github.com/mpquant/MyTT)

* [Hb_Spark数字货币高速免费实时行情服务器,量化必备](https://github.com/mpquant/huobi_intf)

* [hb_trade火币网交易接口API最简封装,提供现货期货合约](https://github.com/mpquant/huobi_trade)

* [backtest数字货币历史回测服务器,高速内存数据库实现](https://github.com/mpquant/huobi_backtest)

* [ths_trade同花顺自动化交易股票下单接口API,量化框架](https://github.com/mpquant/ths_trade)

* [Ashare最简股票行情数据接口API,A股行情完全开源免费](https://github.com/mpquant/Ashare)


### 巴特量化
* 数字货币 股市量化工具 行情系统软件开发 通达信同花顺公式开发 python量化系统开发

* BTC虚拟货币量化交易策略开发 自动化交易策略运行

----------------------------------------------------

![加入群聊](https://github.com/mpquant/huobi_intf/blob/main/img/qrcode.png) 

> #### 股市程序化交易大群,数字货币量化交易探讨, 圈内大咖量化策略分享
> #### 全是干货，无闲聊 ，物以类聚,人以群分，一起感受思维碰撞的力量!
