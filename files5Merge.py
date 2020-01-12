f=open("sample3.txt",'r')
f1=open("sample4.txt",'w')
"""Python Program which reads lines from two files and writes into the third file"
"""If there are any digits present in any of the files,their sum will be printed at the end of the file"""
s=f.readline()
a=0
while s:
    l=s.split()
    l1=[]
    for i in range(len(l)):
        if l[i].isdigit():
            a+=int(l[i])
        else:
            l1.append(l[i])
    p=" ".join(l1)
    f1.write(p)
    f1.write(" ")
    s=f.readline()
f1.write(str(a))
f1.close()
f.close()
            