import tushare as ts
import pandas as pd
import time

pro = ts.pro_api()

date=pro.trade_cal(exchange='', is_open=1,start_date='20181213', end_date='20181223',fields='cal_date')                 #所有时间dataFrame
allStock=pro.stock_basic(exchange='', list_status='L', fields='ts_code')['ts_code']                                     #所有股票series
d=date


for sn in range(2200,3565):
    time.sleep(0.25)
    da=d
    oneStock=pro.daily(ts_code=allStock[sn], start_date='20171213', end_date='20181221',fields='trade_date,pct_chg')
    oneSeries=pd.merge(da,oneStock,left_on='cal_date',right_on='trade_date',how='left')['pct_chg']
    k=0
    for i in range(6):
        if(oneSeries[i]>9.94):
            oneSeries[i]=k+1
            k=k+1
        else:
            k=0
            oneSeries[i]=k
    date[allStock[sn]]=oneSeries
    print(allStock[sn]+'is ok')
date=date.T
date.to_csv('D://zt3.csv')



"""

oneStock=pro.daily(ts_code='300175.SZ', start_date='20171201', end_date='20181207',fields='trade_date,pct_chg')['pct_chg']
print(oneStock)
k=0
for y in range(124):
    oneStock[y],oneStock[248-y]=oneStock[248-y],oneStock[y]
for i in range(249):
    if(oneStock[i]>9.94):
        oneStock[i]=k+1
        k=k+1
    else:
        k=0
        oneStock[i]=k
print(oneStock)

oneStock=pro.daily(ts_code='000001.SZ', start_date='20171201', end_date='20181207',fields='pct_chg')['pct_chg']
date['000001.SZ']=oneStock
oneStock=pro.daily(ts_code='000002.SZ', start_date='20171201', end_date='20181207',fields='pct_chg')['pct_chg']
date['000002.SZ']=oneStock
oneStock=pro.daily(ts_code='000005.SZ', start_date='20171201', end_date='20181207',fields='pct_chg')['pct_chg']
date['000005.SZ']=oneStock
oneStock=pro.daily(ts_code='000006.SZ', start_date='20171201', end_date='20181207',fields='pct_chg')['pct_chg']
date['000006.SZ']=oneStock
print(date)
"""

"""
sn=3
oneStock=pro.daily(ts_code=allStock[sn], start_date='20171201', end_date='20181207',fields='trade_date,pct_chg')
oneSeries=pd.merge(d,oneStock,left_on='cal_date',right_on='trade_date',how='left')['pct_chg']
k=0
for i in range(249):
        if(oneSeries[i]>1):
            oneSeries[i]=k+1
            k=k+1
        else:
            k=0
            oneSeries[i]=k
print(oneSeries)
"""