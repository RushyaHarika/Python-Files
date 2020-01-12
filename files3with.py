"""when we use with, there is no need of closing the file"""
with open("C:\\Users\\Harika\\python Programs\\continent.txt") as f:
    for lineno,line in enumerate(f,1):
        print(lineno,".",line,end=" ")