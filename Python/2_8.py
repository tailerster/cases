import random
names = 'Иван Петр Семен Илья Максим Олег'.split()
ends = 'енко ов ев ив ий ич ак ян идзе'.split()
consonants = 'б в г д ж з к л м н п р с т'.split()
vowes = 'а е и о у я'.split()

def syllable_generator():
    return random.choice(consonants) + \
           random.choice(vowes)

def lastname_generator():
    size = random.randint(1,3)
    lastname = ''
    for i in range(size):
        lastname+=syllable_generator()
    lastname+=random.choice(consonants)
    return  lastname + random.choice(ends)

def username_generator():
    firstname = ''
    firstname+=random.choice(names)
    return firstname

def task_8():
    for i in range(20):
        print(username_generator() + ' ' + lastname_generator().capitalize())
