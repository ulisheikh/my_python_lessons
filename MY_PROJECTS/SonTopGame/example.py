# import json
# with open("language_packages.json",'r',encoding='utf-8') as file:
#     language_packages = json.load(file)

# def get_var(var_name,var_num,full_var):
#     return f'{var_name}{var_num} = "{full_var}"'

# til = input("Tilni tanlang: ")
# i = 1
# var_list = []
# if til in language_packages:
#     qiymat = language_packages[til]
#     for text in qiymat:
#         qiymat2 = get_var("T",i,text)
#         var_list.append(qiymat2)
#         i+=1
#     with open("variables.py","a+",encoding="utf-8") as file2:
#         file2.write("\n".join(var_list) + "\n")
#         file2.write("\n")
# else:
#     print("Bunday til mavjud emas!")

from FUNCTIONS import language_pack
# import language_pack

for lang, translations in language_pack.lang_pack.items():
    print(f"\nTil: {lang.upper()}")
    for key, text in translations.items():
        print(f"{key}: {text}")
