s='>'+20*'2'+30*'3'+40*'4'
while '>2' in s or '>3' in s or '>4' in s:
    if '>2' in s:
        s=s.replace('>2','33>',1)
    if '>3' in s:
        s=s.replace('>3','4>',1)
    if '>4' in s:
        s=s.replace('>4','2>',1)
print(s.count('2')*2+s.count('3')*3+s.count('4')*4)
