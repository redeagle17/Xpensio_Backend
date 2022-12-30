import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
db=firestore.client()

def cat(q):
    sumFood=0
    sumTravel=0
    sumEcom=0
    sumOther=0
    amount=0
    docs=db.collection(q).document("Transactions").collection("Transaction").get()
    for doc in docs:
        # d=list(doc.to_dict().values())
        d=doc.to_dict()
        amount=d.get('Amount')
        category=d.get('To')
        food = ['zomato','swiggy','eatsure','eatclub','dominos','pizzahut','ovenstory','mcdonalds','burger king','mojo pizza','fasoos','kaggis','kfc']
        travel = ['makemytrip','goibibo','easemytrip','indigo','airasia','spicejet','airindia','gofirst','ola','uber','rapido']
        ecommerce = ['dunzo','amazon','flipkart','myntra','bigbasket','dmart','bookmyshow']
        
        if category.lower() in food:
            sumFood = sumFood + amount
        elif category.lower() in travel:
            sumTravel = sumTravel + amount
        elif category.lower() in ecommerce:
            sumEcom = sumEcom + amount
        else:
            sumOther = sumOther + amount
    db.collection(q).document('Categories').collection('Category').document("Category").set({"Food":sumFood,"Travel":sumTravel,"ECommerce":sumEcom,"Other":sumOther})
    return {"Food":sumFood,"Travel":sumTravel,"ECommerce":sumEcom,"Other":sumOther}