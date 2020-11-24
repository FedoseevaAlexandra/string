nr=0
nn=0
nc=0
n=str(input('introduceti un sir de caractere :'))
for i in n:
    if ord(i) in range(65,91):
        nr+=1
    if ord(i) in range(48,58):
        nn+=1
    if (ord(i) in range(33,48)) or (ord(i) in range(58,64)) or (ord(i) in range(91,97)) or (ord(i) in range(123,127)):
        nc+=1
print(nr,'litere majuscule')
print(nn,'cifre')
print(nc,'caractere speciale')