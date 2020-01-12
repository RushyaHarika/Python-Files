f=open("C:\\Users\\Harika\\python Programs\\continent.txt","r")
line=f.readline()
i=1
while line:
    """Printing with line nummbers"""
    print(i,".",line)
    line=f.readline()
    i+=1
f.close()