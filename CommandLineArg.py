import sys

""" This program takes every filename you included in commandline

    except the script name and asks which line to print from that corresponding file

    conditions : file must be present."""

for i in range(1,len(sys.argv),1):
    try:
        data=open(sys.argv[i])

    except IOError:
        print("file not found")

    else:
        line_num = input("Enter the line number you want to print:  ")

        try:
            type(int(line_num))==int
        except ValueError:
            print("entered number is not integer")
        else:
            print("printing line from "+ sys.argv[i])
            list=data.readlines()
            x=list[int(line_num)]
            print(x)