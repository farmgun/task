def fizz_bizz(x):
    if x % 5 == 0 and x % 3 == 0:
        return "Fizz_Bizz"
    elif x%5==0:
        return "Bizz"
    elif x % 3 == 0:
        return "Fizz"
    else:
        return x
print(fizz_bizz(1))
