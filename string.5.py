cnp=str(input('introduceti cnp :'))
t=0
f=0

for i in cnp:
    if ord(i) in range(48,58):
        t+=1
    else:
        f+=1
        
if (f!=0) or(len(cnp)!=13):
    print('cnp este gresit')
else:
    print('cnp este corect')
