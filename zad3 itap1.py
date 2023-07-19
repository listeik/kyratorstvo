f=open('24.txt')
s=f.readline()
k=1
maxk=0
for i in range(len(s)-1):
    if abs(int(s[i])-int(s[i+1]))>=4:
        k+=1
        maxk=max(maxk,k)
    else:
        k=1
print(maxk)
