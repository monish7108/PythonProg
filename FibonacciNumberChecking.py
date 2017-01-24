import sys

"""This programs check every number from command line
    and tells whether number is in fibbonacci series or not.

    Math:   Instead of producing loop and checking the number there is a mathematical formula.

            If (5*x*x)+4  or (5*x*x)-4   or both are perfect squares,

            then the number is in fibonacci."""

def square(x):
    # if the number is not having decimal part then dividing it from int type of same num  gives 0
    return (x**0.5) % int(x**0.5) ==0


for i in range(1,len(sys.argv),1):
    try:
        type(int(sys.argv[i])) == int
    except ValueError:
        print(sys.argv[i]," is not a number")
    else:
        num=int(sys.argv[i])
        x=square(((5*num*num)-4))
        y=square(((5*num*num)+4))

        if x or y:
            print("The number %d is in Fibonacci series." % num)
        else:
            print("The number %d is not in fib series." % num)