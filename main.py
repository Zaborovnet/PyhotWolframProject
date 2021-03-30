
import numpy
import sympy as sym
import wolframalpha

import keyboard
app_id = 'QEG74T-P28PX35G4H'
client = wolframalpha.Client(app_id)



s = input ().split()
a=list (map(int,s))
A= numpy.array(a)
global d
d=''
for i in range(len(A)):
    if i==0:
        if A[i]==0:
            pass
        elif A[i] == 1:
            if i!=len(A):
                d= 'x**' + str (len(A)-i-1)
        else:
            d = str(A[i]) + '*' + 'x**' + str(len(A)-i-1)
    elif i==len(A-1):
        if A[i]==0:
            pass
        elif A[i] == 1:
            if i!=len(A):
                d= 'x'
        else:
            d = +str(A[i])+ '*' +'x'
    elif i==len(A):
        if A[i]==0:
            d=0
        elif A[i] == 1:
            if i!=len(A):
                d= 1
        else:
            d = d + str(A[i])
    elif i > 0 & i < (len(A) - 1):
        if A[i] == 0:
            pass
        elif A[i] == 1:
            if i != len(A):
                d = d + '+ x**' + str(len(A) - i - 1)
        else:
            d = d + '+' + str(A[i]) + '*' + 'x**' + str(len(A) - i - 1)
b=0
global k
k=''
h=d.find("**")
l=d.find("+")
x=d.find("-")
c=''
if (l<x and x>0 and l>0):
    pass
elif(x>l and l>0 and d>0):
    l=x
elif (x<0 and l>0):
    pass
elif (l<0 and x>0):
    l=x
elif (h<0 and l<0):
    l=len(d)

if (l<h or x<h):
    l = d.find("+",2)
    x = d.find("-",2)
    if (l < x and x > 0 and l > 0):
        pass
    elif (x > l and l > 0 and d > 0):
        l = x
    elif (x < 0 and l > 0):
        pass
    elif (l < 0 and x > 0):
        l = x
    elif (h < 0 and l < 0):
        l = len(d)+1


for i in range (h+2,l):
    k=k+str(d[i])
print("Степень введённого полинома =", k)
f=sym.simplify(d)
z='"'
g=str(z)+str(f)+str(z)
f = g.replace("**", "^")
f = f.replace(z, "")
print ("Введённый полином =",f)
#QEG74T-P28PX35G4H
question = '('+f+')'+"'"
res = client.query(question)
answer = next(res.results).text
print(answer)









