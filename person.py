"""
Clasa - este o "reteta" blueprint prin care noi putem sa cream obiecte.
Clasa contine urmatoarele elemente importane:
- numele clasei, unic, concis, sa intelegm ce fel de obiecte putem crea
- constructor = o functie speciala apelata ori de cate ori vrem sa cream un obiect,
    practic, aici se face initializarea obiectului => __init__
- atribute = variabile care apartin unui obiect, si care sunt descriptive pt toate obiectele din acea clasa.
- metode = functii care pot fi apelate pe acele obiecte.
self = parametru care apare in TOATE metodele, si mentine o referinta catre obiectul curent.
"""

"""
Obiectul este o instanta a unei clase, de aceea zicem ca instantiem.
"""

class Person:
  def __init__(self,name,age, gender, nationality = 'RO'):
        self.name = name
        self.age = age
        self.gender = gender
        self.nationality = nationality


  def say_hello(self):
        print('Hello!')
        print(f'Ma numesc {bogdan.name}, am {bogdan.age} ani si sunt {bogdan.nationality}')

bogdan = Person('Bogdan', 24, 'M') #obiectul
bogdan.say_hello()
print(f'Ma numesc {bogdan.name}, am {bogdan.age} ani si sunt {bogdan.nationality}')

kevin = Person('Kevin', 27,'FR')
kevin.say_hello()



