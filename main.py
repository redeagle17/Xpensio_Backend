from fastapi import FastAPI
from demo import findstring
from category import cat
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
# from firebase import solve
from firebase import create_collection
from prediction import arima_prediction
import pandas as pd
db=firestore.client()
app = FastAPI()

# li=["Dear SBI User, your Ac X3380-debited by Rs90.0 on 24Dec22 transfer to Aradhna Ref No 235868808086. If not done by u, fwd this SMS to 9223008333Call 1800111109 or 09449112211 to block UPI -SBI",
# "Dear SBI User, your Ac X3380-debited by Rs5.0 on 23Dec22 transfer to Sameer ahmed Ref No 235849801277. If not done by u, fwd this SMS to 9223008333Call 1800111109 or 09449112211 to block UPI -SBI",
# "Dear SBI User, your Ac X3380-debited by Rs20.0 on 22Dec22 transfer to Sri Hanuman Rice Ref No 235835371020. If not done by u, fwd this SMS to 9223008333Call 1800111109 or 09449112211 to block UPI -SBI",
# "Dear SBI User, your A X3380-debited by Rs76.0 on 21Dec22 transfer to KSHITIJ VERMA Ref No 235812432203. If not done by u, fwd this SMS to 9223008333Call 1800111109 or 09449112211 to block UPI -SBI",
# "Dear SBI User, your Ac X3380-debited by Rs35.0 on 20Dec22 transfer to SHALAM AGNU MIYA Ref No 235547425203. If not done by u, fwd this SMS to 9223008333Call 1800111109 or 09449112211 to block UPI -SBI",
# "Dear SBI User, your Ac X3380-debited by Rs366.0 on 19Dec22 transfer to ARNAV RAHUL GHULE Ref No 235310911743. If not done by u, fwd this SMS to 9223008333Call 1800111109 or 09449112211 to block UPI -SBI",
# "Dear SBI User, your Ac X3380-debited by Rs40.0 on 18Dec22 transfer to SHANI Ref No 235168438606. If not done by u, fwd this SMS to 9223008333Call 1800111109 or 09449112211 to block UPI -SBI",
# "Dear SBI User, your Ac X3380-debited by Rs75.0 on 17Dec22 transfer to Aryan Singh Ref No 235290721453. If not done by u, fwd this SMS to 9223008333Call 1800111109 or 09449112211 to block UPI -SBI",
# "Dear SBI User, your Ac X3380-debited by Rs190.0 on 16Dec22 transfer to SAMYAK BHABHRA Ref No 235105794084. If not done by u, fwd this SMS to 9223008333Call 1800111109 or 09449112211 to block UPI -SBI",
# "Dear SBI User, your Ac X3380-debited by Rs65.0 on 15Dec22 transfer to EURONETGPAY Ref No 235041860831. If not done by u, fwd this SMS to 9223008333Call 1800111109 or 09449112211 to block UPI -SBI",
# "Dear SBI User, your Ac X3380-debited by Rs35.0 on 14Dec22 transfer to ARNAV RAHUL GHULE Ref No 235009147014. If not done by u, fwd this SMS to 9223008333Call 1800111109 or 09449112211 to block UPI -SBI",
# "Dear SBI User, your Ac X3380-debited by Rs307.0 on 13Dec22 transfer to RAJU TATU RATHOD Ref No 234899349010. If not done by u, fwd this SMS to 9223008333Call 1800111109 or 09449112211 to block UPI -SBI",
# "Dear SBI User, your Ac X3380-debited by Rs10.0 on 12Dec22 transfer to Kumary manjula Ref No 234778018951. If not done by u, fwd this SMS to 9223008333Call 1800111109 or 09449112211 to block UPI -SBI",
# "Dear SBI User, your Ac X3380-debited by Rs30.0 on 11Dec22 transfer to MANIK Ref No 234654657572. If not done by u, fwd this SMS to 9223008333Call 1800111109 or 09449112211 to block UPI -SBI",
# "Dear SBI User, your Ac X3380-debited by Rs10.0 on 10Dec22 transfer to SAMEER AHMED Ref No 234537410978. If not done by u, fwd this SMS to 9223008333Call 1800111109 or 09449112211 to block UPI -SBI",
# "Dear SBI User, your Ac X3380-debited by Rs329.0 on 09Dec22 transfer to AMAZON SELLER Ref No 234056993483. If not done by u, fwd this SMS to 9223008333Call 1800111109 or 09449112211 to block UPI -SBI",
# "Dear SBI User, your Ac X3380-debited by Rs9800.0 on 08Dec22 transfer to MANJULA K C Ref No 233902929109. If not done by u, fwd this SMS to 9223008333Call 1800111109 or 09449112211 to block UPI -SBI",
# "Dear SBI User, your Ac X3380-debited by Rs28.0 on 07Dec22 transfer to SREE HANUMAN Ref No 233825590869. If not done by u, fwd this SMS to 9223008333Call 1800111109 or 09449112211 to block UPI -SBI",
# "Dear SBI User, your Ac X3380-debited by Rs147.0 on 06Dec22 transfer to KSHITIJ VERMA Ref No 233630672311. If not done by u, fwd this SMS to 9223008333Call 1800111109 or 09449112211 to block UPI -SBI",
# "Dear SBI User, your Ac X3380-debited by Rs306.0 on 05Dec22 transfer to Dominos Pizza Ref No 233493861442. If not done by u, fwd this SMS to 9223008333Call 1800111109 or 09449112211 to block UPI -SBI",
# "Dear SBI User, your Ac X3380-debited by Rs25.0 on 04Dec22 transfer to Sameer ahmed Ref No 233347503397. If not done by u, fwd this SMS to 9223008333Call 1800111109 or 09449112211 to block UPI -SBI",
# "Dear SBI User, your Ac X3380-debited by Rs10.0 on 03Dec22 transfer to Sameer ahmed Ref No 233274650174. If not done by u, fwd this SMS to 9223008333Call 1800111109 or 09449112211 to block UPI -SBI",
# "Dear SBI User, your Ac X3380-debited by Rs20.0 on 02Dec22 transfer to Sameer ahmed Ref No 233057131501. If not done by u, fwd this SMS to 9223008333Call 1800111109 or 09449112211 to block UPI -SBI",
# "Dear SBI User, your Ac X3380-debited by Rs650.0 on 01Dec22 transfer to Kaggis Cakes And Ref No 232711006724. If not done by u, fwd this SMS to 9223008333Call 1800111109 or 09449112211 to block UPI -SBI",
# "Dear SBI User, your Ac X3380-debited by Rs1000.0 on 01Dec22 transfer to Kaggis Cakes And Ref No 232711006724. If not done by u, fwd this SMS to 9223008333Call 1800111109 or 09449112211 to block UPI -SBI"]

@app.get('/signup/{q}/{t}')
async def status(q:str,t:str):
    li=[]
    t = t.split("\", ")
    for item in t:
        li.append(item)
    li.reverse()
    db.collection(q).document("Message List").collection("List").document('List').set({'list':li})
    findstring(li,q)
    x=cat(q)
    return x

@app.get('/login/{q}/{t}')
async def login(q:str,t:str):
    li=[]
    t = t.split("\", ")
    for item in t:
        li.append(item)
    li.reverse()
    old=db.collection(q).document("Message List").collection("List").get()
    new_list=[]
    for i in old:
        j=list(i.to_dict().values())
        new_list.append(j[0])
    new_li=new_list[0]
    ans_list=(list(set(li) - set(new_li)))
    db.collection(q).document("Message List").collection("List").document('List').set({'list':li})
    findstring(ans_list,q)
    x=cat(q)
    return x

@app.get('/predict')
async def predict():
    doc=db.collection("Email").document("Predictions_of_next_month").collection("Predictions").get()
    if len(doc)>0:
        y=db.collection("Email").document("Predictions_of_next_month").collection("Predictions").document('Prediction').get()
        ans=list(y.to_dict().values())
        return ans[0]
    else:
        trans=db.collection("Email").document("Transactions").collection("Transaction").get()
        date=[]
        amount=[]
        for d in trans:
            d=doc.to_dict()
            a=d.get('Amount')
            c=d.get('Category')
            date.append(c)
            amount.append(a)
        x=arima_prediction(date,amount)
        return x
        # db.collection("Email").document("Predictions_of_next_month").collection("Predictions").document('Prediction').set({'Prediction':x})







