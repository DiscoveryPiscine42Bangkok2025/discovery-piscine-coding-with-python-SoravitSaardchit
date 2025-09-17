s = input().strip()   
if not s:
    print("none")
else:
    count = s.count('z')   
    if count == 0:
        print("none")
    else:
        print('z' * count)
