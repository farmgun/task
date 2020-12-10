def odd_even(x):
    while x>=0:
        if x%2==0:
            print(x,"even")
        else:
            print(x,"odd")
        x-=1
odd_even(5)
