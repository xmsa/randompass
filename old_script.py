import random
while True:
    try:
        Symbols = int(input("Symbols( @#$% ) Length: "))
        break
    except TypeError:
        print("invalide inport")
while True:
    try:
        Numbers = int(input("Numbers(123456)  Length: "))
        break
    except TypeError:
        print("invalide inport")
while True:
    try:
        Lowercase_Characters = int(input("Lowercase( abcdefgh  Length: "))
        break
    except TypeError:
        print("invalide inport")
while True:
    try:
        Uppercase_Characters = int(input("Uppercase( ABCDEFGH  Length: "))
        break
    except TypeError:
        print("invalide inport")

char = list()
Symbol = '@ # $ %'
_Symbol = Symbol.split()
while 0 < Symbols:
    char.append(random.choice(_Symbol))
    Symbols -= 1

while 0 < Numbers:
    char.append(str(random.randrange(0, 9)))
    Numbers -= 1

latin = 'q w e r t y u i o p a s d f g h j k l z x c v b n m'
_latin = latin.split()
while 0 < Lowercase_Characters:
    char.append(random.choice(_latin))
    Lowercase_Characters -= 1

LATIN = latin.upper()
_LATIN = LATIN.split()
while 0 < Uppercase_Characters:
    char.append(random.choice(_LATIN))
    Uppercase_Characters -= 1


print(''.join(random.sample(char, len(char))))
input()
