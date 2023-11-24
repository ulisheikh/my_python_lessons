# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 19:15:23 2023

@author: uli
"""
#birinchi topshiriq
# shaxs_0 = {'Ism':'Ilon Musk',
#            'Davlati':'AQSH',
#            'Kompany':['Tesla','SpaceXStarlink','Neurelong']
#            }
# shaxs_1 = {'Ism':'Jeff Bezos',
#            'Davlati':'Aqsh',
#            'Kompany':['Amazon','Blue orign']
#            }
# shaxs_2 = {'Ism':'Jek Ma',
#            'Davlati':'China',
#            'Kompany':['Alibaba','Taobao Marketplace','Tmall']
#            }
# shaxslar = [shaxs_0,shaxs_1,shaxs_2]
# for shaxs in shaxslar:
#     ism = shaxs['Ism']
#     dav = shaxs['Davlati']
#     print(f"\n{ism.title()} {dav.title()} davlatida tug'ilgan u asos solgan kompaniyalar: ",end=" ")        
#     print(', '.join(shaxs['Kompany']))

#ikkinchi topshiriq

davlatlar = {
    'O\'zbekiston':{'poytaxt':'tashkent',
                 'language':'uzbek',
                 'phone_code': '+998',
                 'pul_birlik':'so\'m',
                 'population':'36 mln'},
    
    'Rossiya':{'poytaxt':'moskva',
                 'language':'rus',
                 'phone_code': '+7',
                 'pul_birlik':'rubl',
                 'population':'128 mln'},
    
    'Qozog\'iston':{'poytaxt':'astana',
                 'language':'qozoq',
                 'phone_code': '+997',
                 'pul_birlik':'tenge',
                 'population':'18 mln'},
    
    'Aqsh':{'poytaxt':'new york',
                 'language':'ingliz',
                 'phone_code': '+1',
                 'pul_birlik':'dollar',
                 'population':'332 mln'},
    
}

promt = input("Davlat nomini kiriting: ").capitalize()
if promt:
    natija = davlatlar.get(promt,0)
    if natija:
        print(f"\n{promt}ning davlat tili: {natija['language'].title()} tili"
              f"\nPoytaxti: {natija['poytaxt'].title()}"
              f"\nTelefon kodi: {natija['phone_code']}"
              f"\nPul birligi: {natija['pul_birlik'].title()}"
              f"\nAholi soni: {natija['population']}")
    else:
        print(f"Bizda {promt} haqida ma'lumot yo'q")

        
    

    
    



    



# for country,info in davlatlar.items():
#         print(f"\n{country.capitalize()}ning poytaxti {info['poytaxt'].title()}"
#           f"\nDavlat tili: {info['language'].title()} tili"
#           f"\nTelefon kodi: {info['phone_code']}"
#           f"\nAholi soni: {info['population']}")














