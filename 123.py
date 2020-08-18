#def ameba (x):
#    return x

ameba=lambda x:x


print(ameba(5))



def summa(a,b):
        return a + b
sum = lambda a,b: a +b
x=summa(4,5)




def func(n):
    return lambda a:a*n

func2 = func(10)

print(func2(5))


strlist=['1','2','3','4','5']

intlist=[]
for item in strlist:
    intlist.append(int(item))

def mile_to_km(s_mile):
    return s_mile*1.6
s_miles = [2.3,5.4,6.3]
s_kms=list(map(mile_to_km,s_miles))

list2=list(map(print,strlist))

#print(intlist)
#print(intlist2)
