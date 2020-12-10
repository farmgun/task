def speed_check(x):
    y = (x//5)-14
    i=0
    while y>0:
        y=y-1
        i+=1
    if i>12:
        print("License suspended")
    elif i<12 and i>0:
        print( "Points:",i)
    else:
        print("ok")

speed_check(50) 

