import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import pandas as pd 
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db=firestore.client()

def create_collection(li,q):
    db.collection(q).document("Transactions").collection("Transaction").document().set({"Date":li[2],"To":li[0],"Amount":float(li[1])})


