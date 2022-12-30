from fastapi import FastAPI
from signup import findstring
from category import cat
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from login import findstring_1
from firebase import create_collection
from prediction import arima_prediction
import pandas as pd
db=firestore.client()
app = FastAPI()

@app.get('/signup/')
async def status(q:str,t:str):
    db.collection(q).document("Message List").collection("List").document('List').set({'list':t[0:len(t)-1]})
    findstring(t,q)
    x=cat(q)
    return x

@app.get('/login/')
async def login(q:str,t:str):
    li= t.split(',')
    old=db.collection(q).document("Message List").collection("List").get()
    new_list=[]
    for i in old:
        j=list(i.to_dict().values())
        new_list.append(j[0])
    new_li=new_list[0]
    x=new_li[0:len(new_li)-1]
    y=x.split(',')    
    ans_list=(list(set(li[0:len(li)-1]) - set(y)))
    
    db.collection(q).document("Message List").collection("List").document('List').set({'list':li[0:len(li)-1]})
   
    findstring_1(ans_list,q)
    x=cat(q)
    return x

@app.get('/predict/{q}')
async def predict(q:str):
    doc=db.collection(q).document("Predictions_of_next_month").collection("Predictions").get()
    if len(doc)>0:
        y=db.collection(q).document("Predictions_of_next_month").collection("Predictions").document('Prediction').get()
        ans=list(y.to_dict().values())
        return ans[0]
    else:
        trans=db.collection(q).document("Transactions").collection("Transaction").get()
        date=[]
        amount=[]
        for d in trans:
            doc=d.to_dict()
            a=doc.get('Amount')
            c=doc.get('Date')
            date.append(c)
            amount.append(a)
        x=arima_prediction(date,amount)
        db.collection("Email").document("Predictions_of_next_month").collection("Predictions").document('Prediction').set({'Prediction':x})
        return x







