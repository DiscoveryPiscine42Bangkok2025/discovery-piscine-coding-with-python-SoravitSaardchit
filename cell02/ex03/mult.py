a = input("Enter the first number: ")
print(a)
b = input("Enter the second number: ")
print(b)
c = int(a)*int(b)
print(a," x ",b," = ",c)
if c > 0:
    print("The result is positive. ")
elif c < 0:
    print("The result is negative. ")
else:
    print("The result is positive and negative. ")
