for a in range(-1000,1000):
    for x in range(1,1000):
        if ((72%x!=0) or (120%x!=0) or (a-x>100))==False:
            break
    else:
        print(a)
        break
