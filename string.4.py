a=str(input('dati primul cuv '))
b=str(input('dati al doilea cuv '))
c=str(input("dati al treilea cuv "))
d=str(input('dati al patrulea cuv '))
if (len(list(a))<3)or(len(list(b))<3)or(len(list(c))<3)or(len(list(d))<3):
    print('scrie cuvinte formate din minimum 3 litere')
else:
    x=int((len(d))/2)
    print('cuvintele erau :',a,b,c,d)
    print('cuv format :'a[:1]+b[0]+c[:2]+d[:x])
