charToSoundex = {"A": "9",
                 "B": "1",
                 "C": "2",
                 "D": "3",
                 "E": "9",
                 "F": "1",
                 "G": "2",
                 "H": "9",
                 "I": "9",
                 "J": "2",
                 "K": "2",
                 "L": "4",
                 "M": "5",
                 "N": "5",
                 "O": "9",
                 "P": "1",
                 "Q": "2",
                 "R": "6",
                 "S": "2",
                 "T": "3",
                 "U": "9",
                 "V": "1",
                 "W": "9",
                 "X": "2",
                 "Y": "9",
                 "Z": "2"}

def soundex(string):

    string=string.upper()
    #print(string)
    for ch in string:
        if ch not in charToSoundex.keys():
            return "0000"

    digit=string[0]
    for ch in string[1:]:
        if charToSoundex[ch] !="9":
            digit+=charToSoundex[ch]

    while len(digit)<4:
        digit+="0"

    return digit[:4]


if __name__== "__main__":
    from timeit import Timer

    name ='MonishLALCHANDANI'

    statement = "soundex('%s')" % name
    t = Timer(statement, "from __main__ import soundex")
    print(soundex(name), t.repeat())



"""==========================OUTPUT============================

/usr/bin/python3.4 "/home/monish/WEEK-5[MONISH]/UnitTesting Python/soundexDataProcessing.py"

first time:
M524 [4.082136162000097, 4.0862981530008256, 4.076315599999361]

second time:
M524 [3.9338647260010475, 3.941941727000085, 4.11428501899718]

Process finished with exit code 0

"""