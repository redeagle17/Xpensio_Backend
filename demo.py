from firebase import create_collection
# from category import cat
def findstring(str,q):
    for word in str:
        x = word.find('on')
        y = word.find('to')
        z = word.find('Rs')

        i = x + 3
        ans1 = ""
        while word[i]!=' ':
            ans1 = ans1 + word[i]
            i += 1

        ans2 =""
        j = y + 3
        while word[j]!=' ' :
            ans2 = ans2 + word[j]
            j += 1

        ans3 =""
        m = z + 2
        while word[m]!=' ':
            ans3 = ans3 + word[m]
            m += 1
        create_collection([ans1,ans2,ans3],q)