f1=open("sample3.txt",'r')
f2=open("continent.txt",'r')
f=open("sample5.txt",'w')
"""Merging the contents of two files into other file"""
l1=f1.readlines()
l2=f2.readlines()
if len(l1)<len(l2):
    l=len(l1)
else:
    l=len(l2)
for i in range(l):
    if i%2==0:
        f.write(" ".join(l1[i]))
        f.write('\n')
    else:
        f.write(" ".join(l2[i]))
        f.write('\n')
if len(l1)==l:
    for i in range(l+1,len(l2)):
        f.write(" ".join(l2[i]))
        f.write('\n')
else:
    for i in range(l+1,len(l1)):
        f.write(" ".join(l1[i]))
        f.write('\n')
f1.close()
f2.close()
f.close()