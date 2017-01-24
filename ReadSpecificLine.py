
try:
    data=open("sample2.txt")

except IOError:
    print("file not found")

else:
    line_num = input("Enter the line number you want to print:  ")

    try:
        type(int(line_num))==int
    except ValueError:
        print("entered number is not integer")
    else:
       list=data.readlines()
       x=list[int(line_num)]
       print(x)

        #print("\n".join("%s" %lines for lines in list))