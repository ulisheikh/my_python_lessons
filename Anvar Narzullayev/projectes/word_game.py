import random as r
from rich.console import Console
from rich.table import Table
from rich.text import Text

def sontop_PC(x):
    """Bu funksiyada kompyuter 1 dan x gacha son o'ylaydi 
    user esa u sonni topishi kerak.Argument sifatida 
    x ga 10 standart qiymati berilgan
    uni o'zgartirishingiz mumkin.
    Masalan: sontop_PC(50) " bu yerda 
    1 dan 50 gacha sonlar o'ynaladi "
    """
    
    # O'yinni boshlaymiz, kompyuter son o'yladi
    print(f"\nMen 1 dan {x} gacha bir son o'yladim"
          " topishga harakat qilib ko'ring")
    
    # Son esa tasodifiy bo'lib tanlanadi
    son = r.randint(1,x)

    # Siklni to'xtatish uchun flag dan foydalanamiz
    flag = 1

    # Taxminlarni 0 dan boshlab hisoblaymiz
    taxmin_user = 0
    
    # Start
    while flag:
        taxmin_user+=1
        # print(son)
        javob =input(">>>\n")
        
        # Javob raqamligini tekshirib olamiz
        if javob.isdigit():

            javob = int(javob)
            if javob < son:
                print(f"Men o'ylagan son {javob} dan katta")
            elif javob > son:
                print(f"Men o'ylagan son {javob} dan kichik")
            elif javob == son:
                print("Siz topdingiz")
                flag = 0 

        # Raqam bo'lmasa...
        else:
            print("Iltimos butun son kiriting")

    # funksiya tuggaydi va bizga foydalanuvchining taxminlar sonini qaytaradi
    return taxmin_user

def sontop_USER(x):
    """Bu funksiyada User 1 dan x gacha son o'ylaydi 
    kompyuter esa u sonni topishi kerak.Argument sifatida 
    x ga 10 standart qiymati berilgan
    uni o'zgartirishingiz mumkin.
    Masalan: sontop_USER(50) " bu yerda 
    1 dan 50 gacha sonlar o'ynaladi "
    """

    # Endi kopyuter son o'ylaydi
    print(f'\nEndi siz 1 dan {x} gacha sonlar ichidan birini o\'ylang men topaman')
    print('\nAgar men aytgan son siznikidan katta bo\'lsa "-",\n'
        'kichik bo\'lsa "+" ni kiriting\n'
          'Agar tog\'ri topgan bo\'lsam ,"ok" deb yozing')

    taxmin_pc = 0

    # Yuqori va quyi nuqtani belgilab olamiz
    max = x
    min = 1
    while True:
        input("Son o'ylagan bo'lsangiz Enterni bosing")
        # Yuqori va quyi nuqta teng emasligini aniqlaymiz
        if min != max:
            son = r.randint(min,max)
        # Agar teng bo'lib qolsa quyi chegarani son ga yuklaymiz
        else:
            son = min

        # javobni foydalanuvchidan qabul qilib olamiz
        javob = input(f"Siz {son} sonini o'yladingiz\n>>> ").lower()
        
        # Agar javob bo'lsa kod ishlaydi bo'lmasa else qismi ishlaydi
        if javob:
            if javob == "-":
                max = son-1
                # Quyi chegarani manfiy songa aylanib ketishidan himoyalaymiz
                if min>max:
                    print("Siz notog'ri ma'lumot kiritdingiz")
                    # Birinchi taxmin qilgan sonidan ayirib ayirib \
                    # oxiri qayta qayta bir sonni chiqaradi
                    max = son

                # Taxminni aniqligini ta'minlaymiz
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
                taxmin_pc+=1
                break
        else:
            print("Iltimos ma'lumot kiriting!")

    # Dasturni tugatamiz va bizga dastur kompyuterning taxminlar sonini qaytaradi
    return taxmin_pc

def play(x=10):
    """Bu funksiyaning maqsadi < sontop_PC() & sontop_USER() > 
       funksiyalari uchun play vazifasini bajaradi va
       natijalarni ko'rsatib beradi"""
    
    # While yordamida sikl yaratamiz
    while True:
        # WINNER bizga g'olibni aniqlab beradi
        WINNER = ""

        # O'yinlar start oladi
        taxmin_user = sontop_PC(x)
        taxmin_pc = sontop_USER(x)
        
        # Natijani oddiy qilib chiqaramiz
        print(f"\nNatija:\n================\n"
        f" USER: {taxmin_user}\n PC: {taxmin_pc}\n================")
        
        # G'olibni aniqlaymiz taxmin sonlari yordamida
        if taxmin_pc > taxmin_user:
            WINNER = "USER"
        
            print("Tabriklayman siz o'yinimizda go'lib chiqdingiz!")
        elif taxmin_pc < taxmin_user:
            WINNER = "PC"

            print("Kompyuter o'yinda g'olib chiqdi!")
        else:
            print("\nDraw\n")
            WINNER = "Draw"

        # winner bizga rich jadvalida yutgan va yutqazganni backgroundini rangini beradi
        winner_pc = "on blue "
        winner_user = "on blue "
        if WINNER == "PC":
            winner_user = "on red"
        elif WINNER == "USER":
            winner_pc = "on red"

        # Jadval tuzishni boshladik
        console = Console()
        table = Table(title="WordGameResults",show_lines=0,style="bold blue")

        # Jadvalga ikta ustun qo'shamiz
        table.add_column("Players")
        table.add_column(" Guesses and Results")

        # Jadvalga uchta qator qo'shamiz
        table.add_row(
                    Text("PC: ",justify='center'),
                    Text(str(taxmin_pc),justify='center'),
                    style=f'{winner_pc}')

        table.add_row(
                    Text("USER: ",justify='center'),
                    Text(str(taxmin_user),justify='center'),
                    style=f"{winner_user}")

        table.add_row(
                    Text("WINNER:",justify='center'),
                    Text(str(WINNER),justify='center'),
                    style="bold red on yellow")
        
        # Jadvalni print qilamiz
        console.print(table)
        
        
        # Foydalanuvchidan o'yinni davom etish yoki to'xtatishini so'raymiz
        javob = input('\nYana o\'ynashni hohlaysizmi \n       '
                      'Ha uchun: 1\n       Yo\'q uchun: 0\n>>> ').lower()
        if javob:
            if javob.isdigit:
                javob = int(javob)
                if javob == 0:
                    break
            else:
                print("Iltimos faqat butun son 0 va 1 ni kiriting")
        else:
            print("Iltimos 0 yoki 1 ni kiritib javob bering!")
    # Dasturni tugatamiz
    print("\nDastur tugadi.Foydalanganingiz uchun tashakkur!\n")




    
play()  
