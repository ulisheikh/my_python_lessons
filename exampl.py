gap = "Bu gapda faqat shu so'z rangli bo'ladi."
soz = "shu"

# ANSI escape kodidan foydalanamiz
qizil = "\033[31m"
tugat = "\033[0m"

# Gapni bo'lib, rangni qo'llaymiz
qismlar = gap.split(soz)
print(f"{qismlar[0]}{qizil}{soz}{tugat}{qismlar[1]}")
