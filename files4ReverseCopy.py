f=open("C:\\Users\\Harika\\python Programs\\continent.txt","r")
f1=open("sample2.txt","w")
"""Copying the contents from one file to the other by reversing each word"""
s=f.readline()
while s:
    l=s.split()
    for i in range(len(l)):
        l[i]=l[i][::-1]
    p=" ".join(l)
    f1.write(p)
    f1.write('\n')
    s=f.readline()
f.close()
f1.close()       
