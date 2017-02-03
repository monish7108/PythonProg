import string
allChars = "BCDFGJKLMNPQRSTVXZbcdfgjklmnpqrstvxz"
charToSoundex = string.maketrans(allChars, "123122245512623122123122245512623122")
remchar="AEIOUHWYaeiouhwy"
def soundex(string):
    #string=string.upper()
    #print(string)
    for ch in string:
        if ch not in allChars and ch not in remchar:
            return "0000"

    digit=string[0].upper()
    #for ch in string[1:]:
      #  if ch in charToSoundex.keys():
    #digit = string[0].upper() + string[1:].translate(charToSoundex)
    for i in string[1:]:
	if i in allChars:
	    digit+=i.translate(charToSoundex)
	
 
    while len(digit)<4:
        digit+="0"

    return digit[:4]


if __name__== "__main__":
    from timeit import Timer

    name ="MonishLALCHANDANI"

    statement = "soundex('%s')" % name
    t = Timer(statement, "from __main__ import soundex")
    print(soundex(name),t.repeat())


    #print(soundex("monish"))


"""==========================OUTPUT============================

/usr/bin/python3.4 "/home/monish/WEEK-5[MONISH]/UnitTesting Python/soundex_moreoptimized.py"

first time:
('M524', [3.8532049655914307, 3.8461790084838867, 3.8483519554138184])

second time:
('M524', [3.8381969928741455, 3.8174428939819336, 3.8166558742523193])

Process finished with exit code 0

"""
