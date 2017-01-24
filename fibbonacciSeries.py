import sys

"""This program takes a number from command line

    and tells whether the number is present in fibonacci or not.

    Works only for one input"""

def nextNum(x,y):
    return x+y

if __name__=="__main__":
    f1,f2=0,1
    list=[f1,f2]
    num=int(sys.argv[1])
    for i in range(2,num,1):
        list.append(
            nextNum(list[i-1],
                    list[i-2]))
    print(list)