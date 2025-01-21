import turtle
# #fanlarning bahosi
# python = 5
# exel = 4
# mobile = 3

# #fanlarning kriditi
# a = 4.5
# a0 = 4.0
# b = 3

# avr_score = ((python * a) + (exel * a0) + (mobile * b)) / (python + exel + mobile)
# print(avr_score)

while 1:
    turtle.shape("turtle")
    
    angle = int(input("Toshbaqa burilishi kerak  bo'lgan gradusni kiriting\n>>> "))
    distence = int(input("Toshbaqa yurishi kerak  bo'lgan masofani kiriting\n>>> "))
    
    turtle.right(angle)
    turtle.forward(distence)

turtle.done()