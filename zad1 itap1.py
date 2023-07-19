f=open('24.txt','r')
s=f.readline()
k=0
for i in range(1,len(s)-1):
    if s[i-1]=='S' and s[i]=='O' and s[i+1]=='S':
        k+=1
print(k)
    
