import json
import os

path = "/home/ulee/Desktop/my_python_lessons/MY_PROJECTS/SonTopGame/lang_pack.json"

# Katalog mavjudligini tekshirish va yaratish
os.makedirs(os.path.dirname(path), exist_ok=True)

lang_packages = {
    
    "uz": {
        "T1 ": "Men 1 dan {x} gacha bir son o'yladim, topishga harakat qilib ko'ring.",
        "T2 ": "Men o'ylagan son {javob} dan katta",
        "T3 ": "Men o'ylagan son {javob} dan kichik",
        "T4 ": "Siz topdingiz!",
        "T5 ": "Iltimos butun son kiriting",
        "T6 ": "Endi siz 1 dan {x} gacha sonlar ichidan birini o'ylang men topaman",
        "T7 ": "Agar men aytgan son siznikidan katta bo'lsa '-', kichik bo'lsa '+' ni kiriting. Agar tog'ri topgan bo'lsam, 'ok' deb yozing",
        "T8 ": "Son o'ylagan bo'lsangiz Enterni bosing",
        "T9 ": "Siz {son} sonini o'yladingiz",
        "T10": "Iltimos faqat butun son kiriting!",
        "T11": "Siz notog'ri ma'lumot kiritdingiz",
        "T12": "Siz notog'ri ma'lumot kiritdingiz",
        "T13": "Ment topdim!",
        "T14": "Iltimos ma'lumot kiriting!",
        "T15": "Iltimos ismingizni kiriting >>> ",
        "T16": "Assalomu aleykum",
        "T17": "Tabriklayman siz o'yinimizda go'lib chiqdingiz!",
        "T18": "Kompyuter o'yinda g'olib chiqdi!",
        "T19": "Yana o'ynashni hohlaysizmi?",
        "T20": "Ha uchun: 1 Yo'q uchun: 0 >>> ",
        "T21": "Iltimos faqat 1 yoki 0 ni kiriting",
        "T22": "Dastur tugadi. Foydalanganingiz uchun tashakkur!"
    },
    "en": {
        "T1 ": "I thought of a number between 1 and {x}, try to guess it.",
        "T2 ": "The number I thought of is greater than {answer}",
        "T3 ": "The number I thought of is smaller than {answer}",
        "T4 ": "You guessed it!",
        "T5 ": "Please enter a whole number.",
        "T6 ": "Now think of a number between 1 and {x}, I will guess it.",
        "T7 ": "If the number I guessed is greater than yours, type '-', if it is smaller, type '+', and type 'ok' if I guessed correctly.",
        "T8 ": "Press Enter when you have thought of a number.",
        "T9 ": "You thought of the number {number}",
        "T10": "Please enter a valid integer!",
        "T11": "You entered incorrect data.",
        "T12": "You entered incorrect data.",
        "T13": "I found it!",
        "T14": "Please enter the data!",
        "T15": "Please enter your name >>> ",
        "T16": "Hello",
        "T17": "Congratulations, you won the game!",
        "T18": "The computer won the game!",
        "T19": "Would you like to play again?",
        "T20": "Press 1 for Yes, 0 for No >>> ",
        "T21": "Please enter only 1 or 0",
        "T22": "The program has ended. Thank you for using it!"
    },
    "ko": {
        "T1 ": "저는 1부터 {x}까지 숫자를 생각했습니다, 그것을 추측해보세요.",
        "T2 ": "제가 생각한 숫자는 {answer}보다 큽니다.",
        "T3 ": "제가 생각한 숫자는 {answer}보다 작습니다.",
        "T4 ": "맞췄습니다!",
        "T5 ": "정수를 입력해 주세요.",
        "T6 ": "이제 1부터 {x}까지의 숫자 중 하나를 생각해 주세요, 제가 그 숫자를 맞히겠습니다.",
        "T7 ": "제가 추측한 숫자가 더 크면 '-', 더 작으면 '+', 정확하게 맞히면 'ok'를 입력해 주세요.",
        "T8 ": "숫자를 생각했다면 엔터키를 눌러주세요.",
        "T9 ": "당신은 {number} 숫자를 생각했습니다.",
        "T10": "유효한 정수를 입력해 주세요!",
        "T11": "잘못된 데이터를 입력하셨습니다.",
        "T12": "잘못된 데이터를 입력하셨습니다.",
        "T13": "찾았습니다!",
        "T14": "데이터를 입력해 주세요!",
        "T15": "이름을 입력해 주세요 >>> ",
        "T16": "안녕하세요",
        "T17": "축하합니다! 게임에서 이겼습니다!",
        "T18": "컴퓨터가 게임에서 이겼습니다!",
        "T19": "다시 게임을 하시겠습니까?",
        "T20": "예는 1, 아니오는 0을 입력하세요 >>> ",
        "T21": "1 또는 0만 입력해 주세요.",
        "T22": "프로그램이 종료되었습니다. 사용해 주셔서 감사합니다!"
    },
    
    "ru": {
        "T1 ": "Я загадал число от 1 до {x}, попробуйте угадать.",
        "T2 ": "Загаданное мной число больше {answer}",
        "T3 ": "Загаданное мной число меньше {answer}",
        "T4 ": "Вы угадали!",
        "T5 ": "Пожалуйста, введите целое число.",
        "T6 ": "Теперь загадайте число от 1 до {x}, я постараюсь угадать.",
        "T7 ": "Если мое число больше вашего, введите '-', если меньше, введите '+', а если я угадал правильно, введите 'ok'.",
        "T8 ": "Когда вы загадаете число, нажмите Enter.",
        "T9 ": "Вы загадали число {number}",
        "T10": "Пожалуйста, введите только целое число!",
        "T11": "Вы ввели неправильные данные.",
        "T12": "Вы ввели неправильные данные.",
        "T13": "Я нашел его!",
        "T14": "Пожалуйста, введите данные!",
        "T15": "Пожалуйста, введите ваше имя >>> ",
        "T16": "Здравствуйте",
        "T17": "Поздравляю, вы выиграли в игре!",
        "T18": "Компьютер выиграл в игре!",
        "T19": "Хотите сыграть еще раз?",
        "T20": "Для да введите 1, для нет введите 0 >>> ",
        "T21": "Пожалуйста, вводите только 1 или 0",
        "T22": "Программа завершена. Спасибо, что воспользовались ей!"
    }
}





with open(path,"w",encoding="utf-8") as file:
    json.dump(lang_packages,file,ensure_ascii=False,indent=4)

print("Json file saqlandi /home/ulee/Desktop...")