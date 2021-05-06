# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 10:01:38 2021

@author: User
"""

#yosh=int(input('Yoshingiz nechada? >> '))
#if yosh<=4:
#     price=0
#elif yosh<=12:
#     price=5000
#elif yosh<65:
#     price=10000
#elif yosh>=65:
#     price=8000
#print(f'sizga kirish chiptasi {price} so\'m' )

#kun=input('bugungi kun nima? >>>')
#harorat=float(input('havo harorati qanday, bro? >> '))
#if kun.lower()=='yakshanba' and harorat>=30:
#    print('urra plyajga boramiz.')
#else:
#    print('ko\'zingizni qising.')

#narx=12000
#tea=1
#salad=0
#if tea and salad:
#    narx=narx+10000
#elif tea or salad:
#    narx=narx+5000
#print(f'Jami {narx} so\'m')

#narx=12000
#tea=1
#salad=0
#non=True
#kompot=False
#assorti=1
#if salad:
#    print('salat oldi')
#    narx=narx+6000
#if tea:
#    print('choy oldi')
#    narx=narx+2000
#if non:
#    print('non oldi')
#    narx=narx+3000
#if kompot:
#    print('kompot oldi')
#    narx=narx=4000
#if assorti:
#    print('assorti oldi')
#    narx=narx+15000
#print(f'Jami {narx} so\'m')

#menu=['osh','lavash','chizburg','gamburg','turk kabob']
#ovqat=input('nima ovqat hohlaysiz? >> ')
#if ovqat.lower() in menu:
#    print('buyurtmangiz qabul qilindi.')
#else:
#    print('bunday ovqatlar bizda yo, quyonni rasmini chizing')

#countries=['turkey', 'france', 'uk','italy','germany']
#nom=input('qaysi davlatga sayohat qilmoqchisiz? >>> ')
#if nom.lower() not in countries:
#    print(f'biz {nom}ga jo\'natishga shartnomamiz yo\'q, uzur.')
#else:
#    print(f'siz  {nom}ga sayoxat qilishiz uchun hali joylar bor.')

#menu=['osh','lavash','chizburg','gamburg','turk kabob']
#buyurtmalar=['osh','lavash','kabob']
#if buyurtmalar:
#    for taom in buyurtmalar:
#        if taom in menu:
#            print(f'{taom} buyurtmangiz qabul qilindi.')
#        else:
#            print(f'kechirasiz {taom} menyuda yoq ')
#else:
#    print('siz buyurtma kiritmadingiz')

#AMaliyot
#son=int(input("juft sonni kiriting: >>> "))
#if son%2==0:
#    print('rahmat')
#else:
#    print('juft son emas')

#age=int(input('yoshingizni kiriting: >>> '))
#if age<=4 or age>=60:
#    print('kirish chiptasi bepul')
#elif age<=18:
#    print('kirish chiptasi 10000 som')
#else:
#    print("kirish chiptasi 20000 som")

#x=int(input('1-sonni kiriting: >>> '))
#y=int(input('2-sonni kiriting: >>> '))
#if x>y:
#    print(f'{x} katta {y}dan')
#elif x<y:
#    print(f'{x} kichik {y}dan')
#elif x==y:
#    print('ikkala son teng')

#mahsulotlar=['olma','tarvuz','uzum','nok','kivi','banana','xurmo','limon','mandarin', 'pamidor']
#savat=[]
#for n in range(5):
#    savat.append(input(f'{n+1}- maxsulotni kiriting: >> '))
#for mahsulot in savat:
#    if mahsulot in mahsulotlar:
#        print(f'Do\'konimizda {mahsulot} bor')
#    else:
#        print(f'Do\'konimizda {mahsulot} yo\'q')
        
#davlatlar=['turkiya','usa','BAA','korea','italy']
#travel=[]
#for n in range(3):
#    travel.append(input(f"{n+1} - davlatni kiriting: >> "))
#for sayohat in travel:
#    if sayohat.lower() in davlatlar:
#        print(f'{sayohat} bizning agentligimizda bor.')
#    else:
#        print(f'{sayohat} - bizning agentligimizda yo\'q')     

#products=['phone','armchair','chair','ring','pen','pencil']
#goods=[]
#bor_maxsulotlar=[]
#mavjud_emas=[]
#for n in range(5):
#    goods.append(input(f'{n+1} - maxsulotni kiriting: '))
#print('bizda bu maxsulotlar yo')
#for tovar in goods:
#    if tovar.lower() in products:
#        bor_maxsulotlar.append(tovar)
#    else:
#        mavjud_emas.append(tovar)
#        print(f'{tovar} \n')
        
#loginlar=[]
#for n in range(5):
#    loginlar.append(input(f"{n+1}- loginni kiriting: >> "))
#login=input('yangi loginni kiriting: >> ')
#if login in loginlar:
#        print('bu login band ,boshqasini tanlang.')
#else:
#        print('xush kelibsiz!')

x=int(input("Istalgan sonni kiriting? >> "))
for n in range(2,11):
    if x%n==0:
        print(f"{x} soni {n}ga qoldiqsiz bo\'linadi.")
#    else:
#       print(f"{x} soni {n}ga qoldiqsiz bo\'linmaydi.")


























    
    
    