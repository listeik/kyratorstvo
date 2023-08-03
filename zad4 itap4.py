def pr(n):
    d=2
    while d*d<=n:
        if n%d==0:
            return False
        d+=1
    return True
    
for i in range(5000000,1000000,-1):
    s=str(i)
    if (pr(i)==True) and ('228' in s) and (s.count('7')==3):
        print(i,'итоговая сумма->',i+100000)
        break
    
    
    
