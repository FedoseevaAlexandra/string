a=str(input('cum viata? '))
b=str(input('ce vrei acum? '))
c=str(input("ce mancare vrei? "))
d=str(input('ce mancare vrei?.2 '))
if (len(list(a))>1)or(len(list(b))>1)or(len(list(c))>1)or(len(list(d))>1):
    print('raspunde printr-un cuvant')
else:
    print('cuvintele erau :',a,b,c,d)
    print(f'Totul e {a}, vreau {b}, acasa ma asteapta {c} si {d}.')
