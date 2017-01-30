import os
path="/home/monish/WEEK-4[MONISH]/Python Sample Programs" #sample path

osSeperator=os.sep

list=os.listdir(path)

file=[]
dir=[]

def listing(path1,list1):
    for i in list1:
        if os.path.isfile("%s/%s"%(path1,i)):
            file.append(path1+osSeperator+i)
        else:
            dir.append(path1+osSeperator+i)
            newpath=path1+osSeperator+i
            newlist=os.listdir(newpath)
            listing(newpath,newlist)


listing(path,list)

print(len(dir))


for d in dir:
    print(d)

print(len(file))

for f in file:
    print(f)