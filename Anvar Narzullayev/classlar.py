from datetime import datetime
bugun = datetime.today()
yil = bugun.year
class Talaba:
    def __init__(self,ism,familiya,tyil):
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil
talaba1 = Talaba('Olim','Olimov',2001)
talaba2 = Talaba('Anvar','Salimov',1986)
talaba3 = Talaba('husan','sotimov',2004)
talaba4 = Talaba('otabek','husanov',2002)
students = [talaba1,talaba2,talaba3,talaba4]
for talaba in students:
    name = talaba.ism.title()
    family = talaba.familiya.title()
    year = talaba.tyil
    print("{} {} {} - yilda tug'ilgan.Hozir "
          "{} yosh".format(name,family,year,yil-year))

# Bir qatorli kod
# ismlar = [talaba.ism.title() for talaba in students]
# print(','.join(ismlar))
