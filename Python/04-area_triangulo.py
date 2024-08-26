import math
a = float(input("Lado A (cm): "))
b = float(input("Lado B (cm): "))
c = float(input("Lado C (cm): "))
s = (a+b+c)/2
area = math.sqrt(s*(s-a)*(s-b)*(s-c))
print("Semiperimetro: ",s)
print("Area: ",area, "cm")
