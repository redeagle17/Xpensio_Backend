import pandas as pd
import numpy as np
import statsmodels.tsa.stattools as tsa
from statsmodels.tsa.arima.model import ARIMA
from datetime import datetime

def arima_prediction(date,amount):
    df = pd.DataFrame(list(zip(date,amount)),columns =['DATE', 'Expense'])
    # df.rename(columns = {'IPG2211A2N':'Production'}, inplace = True)
    df['DATE']=pd.to_datetime(df['DATE'])
    df.set_index('DATE',inplace=True)
    x=len(df.axes[0])
    new_x=(x*70)//100
    def adf_test(series):
        result=tsa.adfuller(series)
        return result[1]
    def MAPE(Y_actual,Y_Predicted):
        mape = np.mean(np.abs((Y_actual - Y_Predicted)/Y_actual))*100
        return mape
    r=adf_test(df['Expense'])
    flag=0
    d=0
    if(r<=0.05):
        d=0
        flag=1
    d=d+1
    while flag==0:
        r=adf_test((df['Expense']-df['Expense'].shift(d)).dropna())
        if(r<=0.5): break
        d=d+1
    train=df[:new_x]
    test=df[new_x:]

    score=10000000
    new_p=0
    new_q=0
    p=[1,2,3,4,5,6,7,8]
    q=[1,2,3,4,5,6,7,8]
    for i in p:
        for j in q:
            model_ARIMA=ARIMA(train['Expense'],order=(i,d,j))
            model_Arima_fit=model_ARIMA.fit()
            pred_start_date=test.index[0]
            pred_end_date=test.index[-1]
            pred=model_Arima_fit.predict(start=pred_start_date,end=pred_end_date)
            mape=MAPE(test['Expense'],pred)
            if mape<=0.5 and mape<score:
                score=mape
                new_p=i
                new_q=j

    new_model_ARIMA=ARIMA(df['Expense'],order=(new_p,d,new_q))
    new_model_ARIMA_fit=new_model_ARIMA.fit()
    pred=new_model_ARIMA_fit.forecast(1)
    ans=pred[0]
    return ans