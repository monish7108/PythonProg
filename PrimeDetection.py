import sys
""" This program takes every number you included in commandline

    except the script name and tell whether number is prime or not."""

for i in range(1,len(sys.argv),1):
    try:
        type(int(sys.argv[i])) == int
    except ValueError:
        print(sys.argv[i], " is not a number")
    else:
        num=int(sys.argv[i])
        if num==1:print("%d is neither prime nor composite." % num)
        else:
            max=(int(sys.argv[i]))/2
            flag=False
            for j in range(2,max,1):
                if num%j==0:
                    print("%d is not a Prime Number." % num)
                    flag=True
                    break
            if flag==False:print("%d is a Prime Number." % num)

