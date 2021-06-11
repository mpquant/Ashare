#-*- coding:utf-8 -*-    ---------------Ashare 股票行情数据( https://github.com/mpquant/Ashare ) 
import json,requests,datetime;      import pandas as pd  #

def get_price_day_tx(code, end_date='', count=10, frequency='1d'):     #日线获取  
    if end_date:  end_date=end_date.strftime('%Y-%m-%d') if isinstance(end_date,datetime.date) else end_date.split(' ')[0]
    end_date='' if end_date==datetime.datetime.now().strftime('%Y-%m-%d') else end_date   #如果日期今天就变成空    
    URL=f'http://web.ifzq.gtimg.cn/appstock/app/fqkline/get?param={code},day,,{end_date},{count},qfq'     
    st= json.loads(requests.get(URL).content)   
    buf=st['data'][code]['qfqday'] if 'qfqday' in st['data'][code] else st['data'][code]['day']
    df=pd.DataFrame(buf,columns=['time','open','close','high','low','volume'],dtype='float')     
    df.set_index(['time'], inplace=True);   df.index.name=''          #处理索引 
    return df

def get_price_min_tx(code, end_date=None, count=10, frequency='1d'):    #分钟线获取 
    ts=int(frequency[:-1]) if frequency[:-1].isdigit() else 1           #解析K线周期数
    if end_date: end_date=end_date.strftime('%Y-%m-%d') if isinstance(end_date,datetime.date) else end_date.split(' ')[0]        
    URL=f'http://ifzq.gtimg.cn/appstock/app/kline/mkline?param={code},m{ts},,{count}' 
    st= json.loads(requests.get(URL).content);       buf=st['data'][code]['m'+str(ts)] 
    df=pd.DataFrame(buf,columns=['time','open','close','high','low','volume','n1','n2'])   
    df=df[['time','open','close','high','low','volume']]    
    df[['open','close','high','low','volume']]=df[['open','close','high','low','volume']].astype('float')
    df.time=pd.to_datetime(df.time);   df.set_index(['time'], inplace=True);   df.index.name=''          #处理索引     
    df['close'][-1]=float(st['data'][code]['qt'][code][3])      #最新基金数据是3位的
    return df


def get_price(code, end_date='',count=10, frequency='1d', fields=[]):         #主功能函数包装
    xcode= code.replace('.XSHG','').replace('.XSHE','')                       #证券代码编码兼容 
    xcode='sh'+xcode if ('XSHG' in code)  else  'sz'+xcode  if ('XSHE' in code)  else code    
    if  frequency in '1d':
         return get_price_day_tx(xcode,end_date=end_date,count=count,frequency='1d') 
    if  frequency in ['1m','5m','15m','30m','60m']:      
         return get_price_min_tx(xcode,end_date=end_date,count=count,frequency=frequency) 
        
if __name__ == '__main__':    
    df=get_price('sh000001',frequency='1d',count=10)
    print('上证指数日线行情\n',df)
    
    df=get_price('000001.XSHG',frequency='15m',count=10)  #支持'1m','5m','15m','30m','60m'
    print('上证指数分钟线\n',df)

# Ashare 股票行情数据( https://github.com/mpquant/Ashare ) 
