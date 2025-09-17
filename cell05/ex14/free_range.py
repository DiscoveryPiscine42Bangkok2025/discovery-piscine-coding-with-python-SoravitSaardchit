a = input().strip()
b = input().strip()
if not a or not b:
    print("none")
else:
    try:
        start = int(a)
        end = int(b)
    except ValueError:
        print("none")
    else:
        if start > end:
            print("none")
        else:
            print(list(range(start, end + 1)))
