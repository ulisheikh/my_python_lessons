import json
import os

path = "/home/ulee/Desktop/my_python_lessons/MY_PROJECTS/SonTopGame/lang_pack.json"

# Katalog mavjudligini tekshirish va yaratish
os.makedirs(os.path.dirname(path), exist_ok=True)

lang_packages = {
    
    "uz": {
        "PC_docstring": "Bu funksiyada kompyuter 1 dan x gacha son o'ylaydi, user esa u sonni topishi kerak. Argument sifatida x ga 10 standart qiymati berilgan, uni o'zgartirishingiz mumkin. Masalan: sontop_PC(50) - bu yerda 1 dan 50 gacha sonlar o'ynaladi.",
        "text1": "Men 1 dan {x} gacha bir son o'yladim, topishga harakat qilib ko'ring.",
        "text2": "Men o'ylagan son {javob} dan katta",
        "text3": "Men o'ylagan son {javob} dan kichik",
        "text4": "Siz topdingiz!",
        "text5": "Iltimos butun son kiriting",
        "User_docstring": "Bu funksiyada User 1 dan x gacha son o'ylaydi, kompyuter esa u sonni topishi kerak. Argument sifatida x ga 10 standart qiymati berilgan, uni o'zgartirishingiz mumkin. Masalan: sontop_USER(50) - bu yerda 1 dan 50 gacha sonlar o'ynaladi.",
        "text6": "Endi siz 1 dan {x} gacha sonlar ichidan birini o'ylang men topaman",
        "text7": "Agar men aytgan son siznikidan katta bo'lsa '-', kichik bo'lsa '+' ni kiriting. Agar tog'ri topgan bo'lsam, 'ok' deb yozing",
        "text8": "Son o'ylagan bo'lsangiz Enterni bosing",
        "text9": "Siz {son} sonini o'yladingiz",
        "text10": "Iltimos faqat butun son kiriting!",
        "text11": "Siz notog'ri ma'lumot kiritdingiz",
        "text12": "Siz notog'ri ma'lumot kiritdingiz",
        "text13": "Ment topdim!",
        "text14": "Iltimos ma'lumot kiriting!",
        "Play_docstring": "Bu funksiyaning maqsadi sontop_PC() & sontop_USER() funksiyalari uchun play vazifasini bajaradi va natijalarni ko'rsatib beradi",
        "text15": "Iltimos ismingizni kiriting >>> ",
        "text16": "Assalomu aleykum",
        "text17": "Tabriklayman siz o'yinimizda go'lib chiqdingiz!",
        "text18": "Kompyuter o'yinda g'olib chiqdi!",
        "text19": "Yana o'ynashni hohlaysizmi?",
        "text20": "Ha uchun: 1 Yo'q uchun: 0 >>> ",
        "text21": "Iltimos faqat 1 yoki 0 ni kiriting",
        "text22": "Dastur tugadi. Foydalanganingiz uchun tashakkur!"
    },
    "en": {
        "PC_docstring": "In this function, the computer thinks of a number between 1 and x, and the user needs to guess it. The default value for x is 10, but it can be changed. For example: sontop_PC(50) will let the computer choose a number between 1 and 50.",
        "text1": "I thought of a number between 1 and {x}, try to guess it.",
        "text2": "The number I thought of is greater than {answer}",
        "text3": "The number I thought of is smaller than {answer}",
        "text4": "You guessed it!",
        "text5": "Please enter a whole number.",
        "User_docstring": "In this function, the user thinks of a number between 1 and x, and the computer needs to guess it. The default value for x is 10, but it can be changed. For example: sontop_USER(50) will let the user think of a number between 1 and 50.",
        "text6": "Now think of a number between 1 and {x}, I will guess it.",
        "text7": "If the number I guessed is greater than yours, type '-', if it is smaller, type '+', and type 'ok' if I guessed correctly.",
        "text8": "Press Enter when you have thought of a number.",
        "text9": "You thought of the number {number}",
        "text10": "Please enter a valid integer!",
        "text11": "You entered incorrect data.",
        "text12": "You entered incorrect data.",
        "text13": "I found it!",
        "text14": "Please enter the data!",
        "Play_docstring": "This function plays the game between sontop_PC() & sontop_USER() and displays the results.",
        "text15": "Please enter your name >>> ",
        "text16": "Hello",
        "text17": "Congratulations, you won the game!",
        "text18": "The computer won the game!",
        "text19": "Would you like to play again?",
        "text20": "Press 1 for Yes, 0 for No >>> ",
        "text21": "Please enter only 1 or 0",
        "text22": "The program has ended. Thank you for using it!"
    },
    "ko": {
        "PC_docstring": "이 함수에서는 컴퓨터가 1부터 x까지의 숫자를 생각하고, 사용자는 그 숫자를 추측해야 합니다. 기본값으로 x는 10이고, 이 값을 변경할 수 있습니다. 예를 들어: sontop_PC(50)은 컴퓨터가 1부터 50까지의 숫자 중 하나를 선택하도록 합니다.",
        "text1": "저는 1부터 {x}까지 숫자를 생각했습니다, 그것을 추측해보세요.",
        "text2": "제가 생각한 숫자는 {answer}보다 큽니다.",
        "text3": "제가 생각한 숫자는 {answer}보다 작습니다.",
        "text4": "맞췄습니다!",
        "text5": "정수를 입력해 주세요.",
        "User_docstring": "이 함수에서는 사용자가 1부터 x까지의 숫자를 생각하고, 컴퓨터는 그 숫자를 추측해야 합니다. 기본값으로 x는 10이고, 이 값을 변경할 수 있습니다. 예를 들어: sontop_USER(50)은 사용자가 1부터 50까지의 숫자 중 하나를 생각하도록 합니다.",
        "text6": "이제 1부터 {x}까지의 숫자 중 하나를 생각해 주세요, 제가 그 숫자를 맞히겠습니다.",
        "text7": "제가 추측한 숫자가 더 크면 '-', 더 작으면 '+', 정확하게 맞히면 'ok'를 입력해 주세요.",
        "text8": "숫자를 생각했다면 엔터키를 눌러주세요.",
        "text9": "당신은 {number} 숫자를 생각했습니다.",
        "text10": "유효한 정수를 입력해 주세요!",
        "text11": "잘못된 데이터를 입력하셨습니다.",
        "text12": "잘못된 데이터를 입력하셨습니다.",
        "text13": "찾았습니다!",
        "text14": "데이터를 입력해 주세요!",
        "Play_docstring": "이 함수는 sontop_PC() & sontop_USER() 게임을 실행하고 결과를 출력합니다.",
        "text15": "이름을 입력해 주세요 >>> ",
        "text16": "안녕하세요",
        "text17": "축하합니다! 게임에서 이겼습니다!",
        "text18": "컴퓨터가 게임에서 이겼습니다!",
        "text19": "다시 게임을 하시겠습니까?",
        "text20": "예는 1, 아니오는 0을 입력하세요 >>> ",
        "text21": "1 또는 0만 입력해 주세요.",
        "text22": "프로그램이 종료되었습니다. 사용해 주셔서 감사합니다!"
    },
    
    "ru": {
        "PC_docstring": "В этой функции компьютер загадывает число от 1 до x, а пользователь должен угадать его. Значение x по умолчанию равно 10, но его можно изменить. Например: sontop_PC(50) позволит компьютеру выбрать число от 1 до 50.",
        "text1": "Я загадал число от 1 до {x}, попробуйте угадать.",
        "text2": "Загаданное мной число больше {answer}",
        "text3": "Загаданное мной число меньше {answer}",
        "text4": "Вы угадали!",
        "text5": "Пожалуйста, введите целое число.",
        "User_docstring": "В этой функции пользователь загадывает число от 1 до x, а компьютер должен его угадать. Значение x по умолчанию равно 10, но его можно изменить. Например: sontop_USER(50) позволит пользователю загадать число от 1 до 50.",
        "text6": "Теперь загадайте число от 1 до {x}, я постараюсь угадать.",
        "text7": "Если мое число больше вашего, введите '-', если меньше, введите '+', а если я угадал правильно, введите 'ok'.",
        "text8": "Когда вы загадаете число, нажмите Enter.",
        "text9": "Вы загадали число {number}",
        "text10": "Пожалуйста, введите только целое число!",
        "text11": "Вы ввели неправильные данные.",
        "text12": "Вы ввели неправильные данные.",
        "text13": "Я нашел его!",
        "text14": "Пожалуйста, введите данные!",
        "Play_docstring": "Эта функция выполняет игру между sontop_PC() и sontop_USER() и выводит результаты.",
        "text15": "Пожалуйста, введите ваше имя >>> ",
        "text16": "Здравствуйте",
        "text17": "Поздравляю, вы выиграли в игре!",
        "text18": "Компьютер выиграл в игре!",
        "text19": "Хотите сыграть еще раз?",
        "text20": "Для да введите 1, для нет введите 0 >>> ",
        "text21": "Пожалуйста, вводите только 1 или 0",
        "text22": "Программа завершена. Спасибо, что воспользовались ей!"
    }
}





with open(path,"w",encoding="utf-8") as file:
    json.dump(lang_packages,file,ensure_ascii=False,indent=4)

print("Json file saqlandi /home/ulee/Desktop...")