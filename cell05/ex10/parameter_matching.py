a = input().strip()               
a = a.strip('"\'')              
if not a:
    print("none")
else:
    ans = input("What was the parameter? ").strip()
    ans = ans.strip('"\'')
    if a == ans:
        print("Good job!")
    else:
        print("Nope, sorry...")
