a=str(input('cum viata? '))
b=str(input('ce vrei acum? '))
c=str(input("ce mancare vrei? "))
d=str(input('ce mancare vrei?.2 '))
if (len(a.split(' '))>1) or(len(b.split(' '))>1)or(len(c.split(' '))>1)or(len(d.split(' '))>1):
    print('raspunde printr-un cuvant')
else:
    print('cuvintele erau :',a,b,c,d)
    print(f'Totul e {a}, vreau {b}, acasa ma asteapta {c} si {d}.')
