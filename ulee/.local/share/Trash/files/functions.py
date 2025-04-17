import random as r
from rich.console import Console
from rich.table import Table
from rich.text import Text
import json
import variables

console = Console()





def sontop_PC(x):
    """Bu funksiyada kompyuter 1 dan x gacha son o'ylaydi
    user esa u sonni topishi kerak.Argument sifatida
    x ga 10 standart qiymati berilgan
    uni o'zgartirishingiz mumkin.
    Masalan: sontop_PC(50) " bu yerda
    1 dan 50 gacha sonlar o'ynaladi "
    """
    

    

    # O'yinni boshlaymiz, kompyuter son o'yladi
    console.print(f"\n{T1.format(x=x)}",style='bold yellow')
    # console.print(f"\nMen 1 dan {x} gacha bir son o'yladim topishga harakat qilib ko'ring",style='bold yellow')
    # Son esa tasodifiy bo'lib tanlanadi
    son = r.randint(1, x)

    # Siklni to'xtatish uchun flag dan foydalanamiz
    flag = 1

    # Taxminlarni 0 dan boshlab hisoblaymiz
    taxmin_user = 0

    # Start
    while flag:
        print(son)
        javob = input(">>>\n")

        # Javob raqamligini tekshirib olamiz
        if javob.isdigit():

            javob = int(javob)
            if javob < son:
                console.print(f"{T2.format(javob=javob)}",style='bold yellow')
                taxmin_user += 1
            elif javob > son:
                console.print(f"{T3.format(javob=javob)}",style='bold yellow')
                taxmin_user += 1
            elif javob == son:
                console.print(f"{T4}",style='rgb(0,255,0) bold')
                taxmin_user += 1
                flag = 0

        # Raqam bo'lmasa...
        else:
            print(f"{T5}")

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
    print(f"\n{T6}")
    print(T7)

    taxmin_pc = 0

    # Yuqori va quyi nuqtani belgilab olamiz
    max = x
    min = 1
    input(f"\n{T8}\n>>> ")

    while True:
        # Yuqori va quyi nuqta teng emasligini aniqlaymiz
        if min != max:
            son = r.randint(min, max)
        # Agar teng bo'lib qolsa quyi chegarani son ga yuklaymiz
        else:
            son = min

        # javobni foydalanuvchidan qabul qilib olamiz
        javob = input(f"{T9}\n>>> ").lower()

        # Agar javob bo'lsa kod ishlaydi bo'lmasa else qismi ishlaydi
        if javob:
            if not javob.isdigit():
                print("\n{T10}}")
            if javob == "-":
                max = son - 1
                # Quyi chegarani manfiy songa aylanib ketishidan himoyalaymiz
                if min > max:
                    print("{T11}}")
                    # Birinchi taxmin qilgan sonidan ayirib ayirib \
                    # oxiri qayta qayta bir sonni chiqaradi
                    max = son

                # Taxminni aniqligini ta'minlaymiz
                else:
                    taxmin_pc += 1
            elif javob == "+":
                min = son + 1
                if min > max:
                    print("{T12}}")
                    min = son
                else:
                    taxmin_pc += 1
            elif javob == "ok":
                print(f"{T13}\n")
                taxmin_pc += 1
                break
        else:
            print("\n{T14}}")

    # Dasturni tugatamiz va bizga dastur kompyuterning taxminlar sonini qaytaradi
    return taxmin_pc

def play(x=10):
    """Bu funksiyaning maqsadi < sontop_PC() & sontop_USER() >
    funksiyalari uchun play vazifasini bajaradi va
    natijalarni ko'rsatib beradi"""

    while True:
        name = input(f"\n{T15} \n>>> ").lower()
        if name:
            print(f"\n                    {T16} {name.upper()} ")
            break
    # While yordamida sikl yaratamiz
    flag2 = True
    part = 0
    part_winner_user = 0
    part_winner_pc = 0
    draw = 0

    while flag2:
        part += 1
        # WINNER bizga g'olibni aniqlab beradi
        WINNER = ""

        # O'yinlar start oladi
        taxmin_user = sontop_PC(x)
        taxmin_pc = sontop_USER(x)

        # # Natijani oddiy qilib chiqaramiz
        # print(f"\nNatija:\n================\n"
        # f" USER: {taxmin_user}\n PC: {taxmin_pc}\n================")

        # G'olibni aniqlaymiz taxmin sonlari yordamida
        if taxmin_pc > taxmin_user:
            WINNER = "USER"
            print("{T17}")
        elif taxmin_pc < taxmin_user:
            WINNER = "PC"
            print("{T18}\n")
        else:
            WINNER = "Draw"
            # Draw bizga  durrangni aniqlab beradi
            draw += 1


        # winner_pc va user bizga rich jadvalida yutgan va yutqazganni backgroundini rangini beradi
        winner_pc = "bold blue "
        winner_user = "bold blue "
        if WINNER == "PC":
            winner_user = "bold red"

            # part_winner bizga partiyadagi g'olibni aniqlab beradi
            part_winner_pc += 1

        elif WINNER == "USER":
            winner_pc = "bold red"

            # part_winner bizga partiyadagi g'olibni aniqlab beradi
            part_winner_user += 1

        # Jadval tuzishni boshladik
        console = Console()
        table = Table(title="WordGame", show_lines=False, style="bold blue")

        # Jadvalga ikta ustun qo'shamiz
        table.add_column(Text(r"  \_\_R_E_S_U_L_T_S_/_/  ", style="cyan"), style="white")
        # table.add_column()

        # Jadvalga uchta qator qo'shamiz
        table.add_row(Text("", justify="center"))  # Bo'sh qator uchun
        table.add_row(Text(f"| P a r t |", justify="center"), style="bold blue")
        table.add_row(Text(f"[{str(part)}]", justify="center"), style="bold red")
        table.add_row(Text("", justify="center"))  # Bo'sh qator uchun
        table.add_row(
            Text(f"PC:  guesses: {str(taxmin_pc)}", justify="center", style="italic"),
            style=f"{winner_pc}",
        )
        table.add_row(
            Text(f"{name.upper()}: guesses:{str(taxmin_user)}", style="italic", justify="center"),
            style=f"{winner_user}",
        )
        table.add_row(Text("", justify="center"))  # Bo'sh qator uchun
        table.add_row(
            Text(f"WINNER: {str(WINNER)}", justify="center"), style="bold red on blue"
        )

        # Jadvalni print qilamiz
        console.print(table)

        # Foydalanuvchidan o'yinni davom etish yoki to'xtatishini so'raymiz
        # while True:
        #     javob2 = input('\nYana o\'ynashni hohlaysizmi? \n       '
        #                   'Ha uchun: 1\n       Yo\'q uchun: 0\n>>> ').lower()
        #     if javob2.isdigit():
        #         javob2 = int(javob2)
        #         if javob2 == 1:
        #             break
        #         elif javob2 == 0:
        #             flag2 = False
        #             break
        #     else:
        #         print("\nIltimos faqat 1 yoki 0 ni kiriting")
        while True:
            javob2 = input(
                "\n{T19} \n       "
                "{T20}\n"
            ).strip()
            if javob2 in ["0", "1"]:
                flag2 = javob2 == "1"
                break
        print("\n{T21}")

    table2 = Table(title="\nTotal score in the game", style="bold")

    table2.add_column(
        Text("WordGameResults", justify="center", style="red reverse"), style="reverse"
    )
    table2.add_row(Text("Total part", justify="center"))
    table2.add_row(Text(str(part), justify="center"))
    table2.add_row(Text("", justify="center"))  # Bo'sh qator uchun
    table2.add_row(
        Text(f"{name.upper()} won the game [{str(part_winner_user)}] times", justify="center")
    )
    table2.add_row(Text("", justify="center"))  # Bo'sh qator uchun
    table2.add_row(
        Text(f"PC won the game [{str(part_winner_pc)}] times", justify="center")
    )
    table2.add_row(Text("", justify="center"))  # Bo'sh qator uchun
    table2.add_row(Text(f"DRAW: [{str(draw)}]", justify="center"))
    table2.add_row(Text("", justify="center"))  # Bo'sh qator uchun

    console.print(table2)

    # Dasturni{ tugatamiz
    print("\n{T22}\n")


