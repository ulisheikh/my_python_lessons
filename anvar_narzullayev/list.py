# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 09:06:21 2023

@author: uli
"""
liked_fruits = []
mevalar = ['anor','anjir','shaftoli','olma','banan']
fruits = mevalar[:]

# listning ichidagi elemntlarga ularning index raqami orqali to'rtburchak qavslar yordamida murojaat qilishi mumkin 
meva0 = mevalar[0]
#print(meva0)

# append yordamida list oxiriga element qo'shiladi
mevalar.append("o'rik")

# insert yordamida hohlagan index bo'yicha element qo'shiladi
mevalar.insert(2,'ananas')

# list chidagi elementlarni remove metodi yordamida uning qiymati orqali o'chiriladi
mevalar.remove('olma')

# list ichidagi elementlar del metodi yordamida index bo'yicha o'chiriladi
del(mevalar[1])

# pop metodi yordamida indexlar bo'yicha ro'yxat ichidan element sug'urib olinadi
liked_meva1 = mevalar.pop(3)
liked_meva2 = mevalar.pop(2)


# bo'sh ro'yxat yaratilib unga pop va append orqali element qo'shish mumkin
liked_fruits.append(liked_meva1)
liked_fruits.append(liked_meva2)

#print(mevalar)
#print(liked_fruits)
print(f"Mening mevalar ro'yxatim: {fruits}\nMening yoqtirgan mevalarim: {liked_fruits} ")
print("---------------------------------------------------------------------------------------------")
print('\n2-dars\n')

# list elementlarini alifbo ketma-ketligida tartiblash KATTA HARFLAR HAR DOIM BIRINCHIGA CHIQADI
cars = ['lasetti','malibu','tahoe','gentra','matiz','orlando','captiva']
carsreverse = cars[:]

print('Asl ro\'yxat: ',cars)

#print("\nAsl ro'yxatni sorted() metodi yordamida o'zgaritmagan holatda A-Z ketma-ketligida tartiblash ")
print('\nSorted qaytargan natija: ',sorted(cars))
print('Asl ro\'yxat o\'zgarmadi: ',cars)

#print("\nAsl ro'yxatni sorted() metodi yordamida o'zgaritmagan holatda Z-A ketma-ketligida tartiblash")
print('Sorted qaytargan natija: ',sorted(cars,reverse=True))
print('Asl ro\'yxat o\'zgarmadi: ',cars)

#print("\nEndi ro'yxatni shunchaki boshdan oyoq aylantirib qo'yamiz ")
carsreverse.reverse()
print("\nAsl ro'yxat: ", cars)
print("Ro'yxat shunchaki teskarisiga aylantirildi: ", carsreverse)

# len() metodi yordamida ro'yxat uzunligini o'lchaymiz
print("\nRo'yxat ichida ", len(cars), "ta nmashina bor")

#print("\nSort() metodi yordamida elementlarni tartiblasak asl ro'yxat ham o'zgaribb ketdi !!! ")
print("\nSort yordamida A dan Z ga qarab")
cars.sort()
print('A-Z ketma-ketligida: ',cars)

#print("\nSort reverse yordamida Z dan A ga qarab ")
cars.sort(reverse=True)
print('Z-A ketma-ketligida: ',cars)
print("O'zgargan ro'yxar: ",cars)
print("--------------------------------------------------------------------------------------------------")

# range funksiyasi
numbers = list(range(0,10))
print(numbers)

# Qadamlash bilan sonlarni chiqarish 
juft_sonlar = list(range(0,10,2))
toq_sonlar = list(range(1,10,2))
print(f"{juft_sonlar}\n{toq_sonlar}")
kichik = min(numbers)
katta = max(numbers)
yigindi = sum(numbers)
print(f"\nEng katta son: {katta}\nEng kichin son: {kichik}\nBarcha sonlarning yig'indisi: {yigindi} ga teng ")

print("--------------------------------------------------------------------------------------------------")

# Ro'yxatlarni kesish 
toys = ['barby','kukla','mqquenn','hulk','temir odam']
a = toys[0:3]
b = toys[:4]
c = toys[0:]
print(f"\n{a},\n{b},\n{c}")

print("--------------------------------------------------------------------------------------------------")

# Tuple() o'zgarmas qiymat haqida
ismlar = ('abror',"asadbek","men",'u',"anou",'sen')
names = ismlar[:]
ismlar = list(ismlar)
ismlar[0] = "ahmad"
ismlar.remove('u')
ismlar.append("u")
print(f"Asl ro'yxat: {names}")
print(f"O'zgarishdan so'ng: {ismlar}")















