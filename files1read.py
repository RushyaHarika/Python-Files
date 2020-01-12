f=open("C:\\Users\\Harika\\python Programs\\sample.txt")
c=f.read(1)
while c:
    print(c)
    c=f.read(1)
f.close()