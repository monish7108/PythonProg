charToSoundex = {
                 "B": "1",
                 "C": "2",
                 "D": "3",

                 "F": "1",
                 "G": "2",

                 "J": "2",
                 "K": "2",
                 "L": "4",
                 "M": "5",
                 "N": "5",

                 "P": "1",
                 "Q": "2",
                 "R": "6",
                 "S": "2",
                 "T": "3",

                 "V": "1",

                 "X": "2",

                 "Z": "2"}

allChars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

def soundex(string):

    string=string.upper()
    #print(string)
    for ch in string:
        if ch not in allChars:
            return "0000"

    digit=string[0]
    for ch in string[1:]:
        if ch in charToSoundex.keys():
            digit+=charToSoundex[ch]

    while len(digit)<4:
        digit+="0"

    return digit[:4]


if __name__== "__main__":
    from timeit import Timer

    name =input("enter a word to proceed: ")

    statement = "soundex('%s')" % name
    t = Timer(statement, "from __main__ import soundex")
    print(soundex(name),t.repeat())


    #print(soundex("monish"))


"""==========================OUTPUT============================

/usr/bin/python3.4 "/home/monish/WEEK-5[MONISH]/UnitTesting Python/soundex_moreoptimized.py"

first time:
M524 [4.013876016000722, 4.009777249000763, 4.019670795998536]

second time:
M524 [3.865629689000343, 3.857217402997776, 3.8570503769988136]

Process finished with exit code 0

"""