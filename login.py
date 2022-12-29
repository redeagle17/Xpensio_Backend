from firebase import create_collection
def findstring_1(l,q):
    
    for i in range(0,len(l)):
        word=l[i]
        newli=word.split(' ')
        if(i==len(l)-1):
            ans=newli[len(newli)-1]
            create_collection([newli[1],newli[3],ans[0:len(ans)-2]],q)
        else:
            create_collection([newli[1],newli[3],newli[len(newli)-1]],q)