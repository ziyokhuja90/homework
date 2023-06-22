


# sonlar = []
# for i in range(1,10):
#     sonlar.append(i)
#     if i == 4:
#         sonlar.append('bu 5')
#         break    
    
    
# print(sonlar)

kitoblar = {}
 
nomi = input('nomi>>> ')
necta = int(input('nechta qushmoqchisiz>>> '))


def nameFunc(name,**kwargs):
    kitoblar[name] = kwargs
    
    
   

if necta == 1:
    bir = input('muallifi>>> ')
    nameFunc(name=nomi,muallifi = bir)
    
elif necta == 2:
    bir = input('muallifi>>> ')
    ikki = input('janr>>> ')
    nameFunc(name=nomi,muallifi = bir,janr=ikki)
    
elif necta == 3:
    bir = input('muallifi>>> ')
    ikki = input('janr>>> ')
    uch = int(input('yili>>> '))
    nameFunc(name=nomi,muallifi = bir,janr=ikki,yili = uch)
    
elif necta == 4:
    bir = input('muallifi>>> ')
    ikki = input('janr>>> ')
    uch = int(input('yili>>> '))
    tur = int(input('necta sotilgaligi>>> '))
    nameFunc(name=nomi,muallifi = bir,janr=ikki,yili = uch , sotilgan=tur)
    
else:
    print('sorry i do not understand you!')
    

print(kitoblar)

