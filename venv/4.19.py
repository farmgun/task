y1 = input ("y1=")
x1 = input ("x1=")
y2 = input ("y2=")
x2 = input ("x2=")
l1: str=input("длинна1=")
l2=input("длинна2=")
w1=input("висота1")
w2=input("висота2")
y1 = float (y1)
y2 = float (y2)
x1 = float (x1)
x2 = float (x2)
l1=float(l1)
l2=float(l2)
w1=float(w1)
w2=float(w2)

x3=x1+w1
y3=y1+l1
x4=x2+w2
y4=y2+l2

NumbersX = [x1, x2, x3, x4]
print(min(NumbersX), max(NumbersX))


NumbersY = [y1, y2, y3, y4]
print(min(NumbersY), max(NumbersY))