import sys
#print(sys.version)
#it is of version 2.7.6 go to line 34

"""This program takes a particular file input and gives you the word count

    of every word present in that file"""
for i in range(1,len(sys.argv)):
    try:
        data = open(sys.argv[i],"r")


    except IOError:
        print("file not found")

    else:
        print("printing from file %s"% sys.argv[i])
        count=1
        d = {}
        line1 = data.read()
        #print(line1) : checking if data is complete present in line1

        list=line1.split()


        #print(list) : making list of words from line1
        #print(len(list))

        for item in list:
            if item in d.keys():
                d[item]+=1
            else:
                d[item]=count
        #sys is of version 2.7.6 hence using raw_input instead of input
        inp = raw_input ( "enter the word you want to check frequency of: " )
        if inp in d.keys():
            print("%s => %d\n" % (inp,d[inp]))
        else:
            print("This word is not in the file\n")
        #print(d["+++"]) : checking if its counting particular word correctly
        print("\t".join(["%s => %d" % (k,v) for (k,v) in d.items()]))



