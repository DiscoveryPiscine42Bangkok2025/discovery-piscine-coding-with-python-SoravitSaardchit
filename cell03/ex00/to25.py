a = input("Enter a number less than 25 \n")
b = int(a)
if b > 25:
    print("Error")
else:
    for i in range(b,26):
        print("Inside the loop, my variable is ",i)
