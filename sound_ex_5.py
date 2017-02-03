import string
allChars = "BCDFGJKLMNPQRSTVXZbcdfgjklmnpqrstvxz"
charToSoundex = string.maketrans(allChars, "123122245512623122123122245512623122")
remchar="AEIOUHWYaeiouhwy"
def soundex(string):
    #string=string.upper()
    #print(string)
    for ch in string:
        if ch in allChars or ch in remchar:pass
	else:return "0000"

    digit=string[0].upper()
    #for ch in string[1:]:
      #  if ch in charToSoundex.keys():
    #digit = string[0].upper() + string[1:].translate(charToSoundex)
    for i in string[1:]:
	if i in allChars:
	    digit+=i.translate(charToSoundex)
	
    digit+="000"

    return digit[:4]


if __name__== "__main__":
    from timeit import Timer

    name ="MonishLALCHANDANI"

    statement = "soundex('%s')" % name
    t = Timer(statement, "from __main__ import soundex")
    print(soundex(name),t.repeat())


    #print(soundex("monish"))


"""==========================OUTPUT============================

monish@tarams-ThinkCentre-Edge72:~$ python sound_ex_5.py

first time:
('M524', [3.7667078971862793, 3.7685577869415283, 3.761254072189331])

second time:
('M524', [3.7766990661621094, 3.7756588459014893, 3.7757740020751953])

monish@tarams-ThinkCentre-Edge72:~$ 


"""
