import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import pandas as pd 
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db=firestore.client()

def create_collection(li,q):
    db.collection(q).document("Transactions").collection("Transaction").document().set({"Date":li[1],"To":li[0],"Amount":float(li[2])})
# def solve():
#     date=[]
#     amount=[]
#     # category=[]
#     to=[]
#     docs=db.collection('email1').get()
#     for doc in docs:
#         d=list(doc.to_dict().values())
#         date.append(d[1])
#         amount.append(d[2])
#         to.append(d[0])
    
    # dict= {'Date': date, 'amount': amount,'TO':to}    
    # return dict    
# df = pd.DataFrame(dict) 
# df.to_csv('dataset.csv')


