s = input().strip()   
if not s:
    print("none")
else:
    count = sum(1 for ch in s.lower() if ch == 'z')
    if count == 0:
        print("none")
    else:
        print('z' * count)
