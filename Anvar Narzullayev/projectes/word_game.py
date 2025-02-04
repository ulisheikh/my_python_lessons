import random as r
def sontop_PC(x):
    """Bu funksiyada kompyuter 1 dan x gacha son o'ylaydi 
    user esa u sonni topishi kerak.Argument sifatida 
    x ga 10 standart qiymati berilgan
    uni o'zgartirishingiz mumkin.
    Masalan: sontop_PC(50) " bu yerda 
    1 dan 50 gacha sonlar o'ynaladi "
    """
    print(f"\nMen 1 dan {x} gacha bir son o'yladim"
          " topishga harakat qilib ko'ring")
    son = r.randint(1,x)
    flag = 1
    taxmin_user = 0
    while flag:
        taxmin_user+=1
        print(son)
        javob =input(">>>\n")
        if javob.isdigit():
            javob = int(javob)
            if javob < son:
                print(f"Men o'ylagan son {javob} dan katta")
            elif javob > son:
                print(f"Men o'ylagan son {javob} dan kichik")
            elif javob == son:
                print("Siz topdingiz")
                flag = 0          
        else:
            print("Iltimos butun son kiriting")
    return taxmin_user
def sontop_USER(x):
    """Bu funksiyada User 1 dan x gacha son o'ylaydi 
    kompyuter esa u sonni topishi kerak.Argument sifatida 
    x ga 10 standart qiymati berilgan
    uni o'zgartirishingiz mumkin.
    Masalan: sontop_USER(50) " bu yerda 
    1 dan 50 gacha sonlar o'ynaladi "
    """
    print(f'\nEndi siz 1 dan {x} gacha sonlar ichidan birini o\'ylang men topaman')
    print('\nAgar men aytgan son siznikidan katta bo\'lsa "-",\n'
        'kichik bo\'lsa "+" ni kiriting\n'
          'Agar tog\'ri topgan bo\'lsam ,"ok" deb yozing')
    taxmin_pc = 0
    max = x
    min = 1
    while True:
        if min != max:
            son = r.randint(min,max)
        else:
            son = min
        javob = input(f"Siz {son} sonini o'yladingiz\n>>> ")
        if javob:
            if javob == "-":
                max = son-1
                if min>max:
                    print("Siz notog'ri ma'lumot kiritdingiz")
                    max = son
                else:
                    taxmin_pc+=1 
            elif javob == "+":
                min = son+1
                if min>max:
                    print("Siz noto'g'ri ma'lumot kiritdingiz")
                    min = son
                else:
                    taxmin_pc+=1
            elif javob == "ok":
                print(f"Men topdim.\n")
                break
        else:
            print("Iltimos ma'lumot kiriting!")
    return taxmin_pc
def play(x=10):
    """Bu funksiyaning maqsadi < sontop_PC() & sontop_USER() > 
       funksiyalari uchun play vazifasini bajaradi va
       natijalarni ko'rsatib beradi"""
    while True:
        
        taxmin_user = sontop_PC(x)
        taxmin_pc = sontop_USER(x)
        
        print(f"\nNatija:\n================\n"
        
        f" USER: {taxmin_user}\n PC: {taxmin_pc}\n================")
        if taxmin_pc > taxmin_user:
            print("Tabriklayman siz o'yinimizda go'lib chiqdingiz!")
        elif taxmin_pc < taxmin_user:
            print("Kompyuter o'yinda g'olib chiqdi!")
        else:
            print("\nDurrang\n")

        javob = input('\nYana o\'ynashni hohlaysizmi \n       '
                      'Ha uchun: 1\n       Yo\'q uchun: 0\n>>> ').lower()
        if javob:
            javob = int(javob)
            if javob == 0:
                break
    print("\nDastur tugadi.Foydalanganingiz uchun tashakkur!")
play()  
