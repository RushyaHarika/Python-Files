f=open("C:\\Users\\Harika\\python Programs\\continent.txt")
"""Printing the contents of each line from 5th character to 8th character"""
line=f.readline(8)
while line:
    print(line[5:])
    line=f.readline(8)
f.close()