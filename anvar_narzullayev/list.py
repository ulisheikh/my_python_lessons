# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 09:06:21 2023

@author: uli
"""
liked_fruits = []
mevalar = ['anor','anjir','shaftoli','olma','banan']

# listning ichidagi elemntlarga ularning index raqami orqali to'rtburchak qavslar yordamida murojaat qilishi mumkin 
meva0 = mevalar[0]
print(meva0)

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
print(f"Mening mevalar ro'yxatim: {mevalar}\nMening yoqtirgan mevalarim: {liked_fruits} ")
