from bs4 import BeautifulSoup
import urllib

#soup=BeautifulSoup(urllib.request.urlopen("https://www.google.co.in"),"html.parser")
soup=BeautifulSoup(open('sample.html'),'html.parser')
tagname=input("enter the name of the tag: ")
attr=input("enter the name of the attr: ")
attrvalue=input("enter the value of the attribute: ")

#soup.find(tagname, {attr : attrvalue})
print(soup.find(tagname, {attr : attrvalue}).text)
#tag.string.replace_with("this is the replaced string")
#print(tag.string)