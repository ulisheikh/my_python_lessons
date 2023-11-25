# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 18:55:09 2023

@author: uli
"""
# topshiriq 1
books = []
flag = 1
n=1
while flag:
    print('\nYoqtirgan kitoblaringiz ro\'yxatini shakllantiramiz.')
    print("Dasturni to'xtatish uchun kitob o'rniga \"stop\" kalit so'zini yozing yozing")
    promt = input(f"\n{n}-yaxshi ko'rgan kitobiz nomini kiriting: ")
    if promt:
        if promt != 'stop':
            books.append(promt)
            n+=1
        else:
            flag = 0
print("\nSizning yoqtirgan kitoblaringiz quyidagilar: ")        
for book in books:
    print(book.title())

# topshiriq 2 
while 1:
    yosh = (input('\nYoshingiz nechida?\n>>>'))
    if yosh.isdigit():
        yosh = int(yosh)
        if yosh < 7:
            print('Sizga kirish narhi 2000 so\'m')
        elif yosh > 6 and yosh < 19:
            print('sizga kirish narhi 3000 so\'m ')
        elif yosh > 18 and yosh < 66:
            print('sizga kirish narhi 10 000 so\'m ')
        elif yosh == 66 or yosh > 66 :
            print('sizga kirish bepul ')
    elif yosh == 'exit' or 'quit':
        break
print("Dastur tugadi! ")

## ustozning kodi
savol = '\nYoqtirgan kitoblaringiz nomini kiriting'
savol+=' (barcha kitoblarni kiritgach "exit" deb yozing)\n>>>'
while 1:
    kitob = input(savol)
    if kitob == 'exit':
        break
print("Raxmat")







