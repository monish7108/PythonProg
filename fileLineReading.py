#import sys

""" This program takes every filename you included in commandline

    except the script name and asks which line to print from that corresponding file

    conditions : file must be present."""
def filereading(argv,line_num):
	#for i in range(1,len(sys.argv),1):
	try:
		data=open(argv)

	except IOError:
		print("file not found")

	else:
		#line_num = input("Enter the line number you want to print:  ")

		try:
			type(int(line_num))==int
		except ValueError:
			print("entered number is not integer")
		else:
			#print("printing line from "+ argv)
			list=data.readlines()
			#x=list[int(line_num)]
			#if x==list[0]:
			x=list[line_num]
			return x
	return "error in file opening"

#def fileclosed(filename):
 #   filename.close()
  #  return file.closed()