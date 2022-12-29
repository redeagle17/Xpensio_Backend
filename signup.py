from firebase import create_collection
def findstring(l,q):
    li=l.split(',')
    for i in range(0,len(li)):
        word=li[i]
        newli=word.split(' ')
        if(i==len(li)-1):
            ans=newli[len(newli)-1]
            create_collection([newli[1],newli[3],ans[0:len(ans)-2]],q)
        else:
            create_collection([newli[1],newli[3],newli[len(newli)-1]],q)
        