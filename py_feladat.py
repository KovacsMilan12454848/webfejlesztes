'''


bekér 5 számot
elso körben vizsdáljuk meg hogy pozitiv vagy negativ
az öt közül hány darab nagyobb mint husz (az öt közül enyi az amenyi nagyobb ha nincs akkor nincs


'''



szam1=int(input('adj meg egy számot(1)'))
szam2=int(input('adj meg egy számot(2)'))
szam3=int(input('adj meg egy számot(3)'))
szam4=int(input('adj meg egy számot(4)'))
szam5=int(input('adj meg egy számot(5)'))

lista=[szam1,szam2,szam3,szam4,szam5]

for i in lista:
    if i%2==0:
        print('negatí')
    else:
        print('pozitív')
g=0
for n in lista:
    if n>20:
        g+=1
if g==0:
    print('az öt szám közül nincs nagyobb')
else:
    print(f'az öt szám közül {g} szám nagyobb')


    

