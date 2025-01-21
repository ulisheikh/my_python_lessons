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
    
    print("Dastur tugadi!")
    return taxmin_user
def sontop_USER(x):
    """Bu funksiyada User 1 dan x gacha son o'ylaydi 
    kompyuter esa u sonni topishi kerak.Argument sifatida 
    x ga 10 standart qiymati berilgan
    uni o'zgartirishingiz mumkin.
    Masalan: sontop_USER(50) " bu yerda 
    1 dan 50 gacha sonlar o'ynaladi "
    """
    print(f"\nEndi siz 1 dan {x} gacha sonlar ichidan birini o'ylang men topaman")
    print("\nAgar men aytgan son siznikidan katta bo'lsa < - > ,\n"
          "kichik bo'lsa < + > ni kiriting\n"
          "Agar tog'ri topgan bo'lsam ,< ok > deb yozing")
    taxmin_pc = 0
    max = x
    min = 1
    while True:
        taxmin_pc+=1
        if min != max:
            son = r.randint(min,max)
        elif min == max:
            son = min
        javob = input(f"Siz {son} sonini o'yladingiz\n>>> ")
        if javob == "-":
            max = son-1
        elif javob == "+":
            min = son+1
        elif javob == "ok":
            print(f"Men topdim.\n")
            break
    return taxmin_pc
def hisobla(x=10):
    """Bu funksiyaning maqsadi < sontop_PC() & sontop_USER() > 
       funksiyalari uchun play vazifasini bajaradi va
       natijalarni ko'rsatib beradi"""
    while True:
        taxmin_user = sontop_PC(x)
        taxmin_pc = sontop_USER(x)
        javob = input("\nSiz yana o'ynashni hohlaysizmi? (yes/no)\n        ")

        if javob == "no":
            break
    print(f"\nUmumiy taxminlar soni:\n"
    f"USER: {taxmin_user}\nPC:{taxmin_pc}")
    if taxmin_pc > taxmin_user:
        print("Tabriklayman siz O'yinimiz g'olibisiz!")
    elif taxmin_pc < taxmin_user:
        print("\nKaminai kamtarin o'yinda g'olib chiqdi")
    else:
        print("\nDuppa durrang bo'ldi")
hisobla()  
