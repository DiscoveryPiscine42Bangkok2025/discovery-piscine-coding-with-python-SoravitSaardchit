import shlex
s = input().strip()
if not s:
    print("none")
else:
    try:
        parts = shlex.split(s)   
    except ValueError:
        parts = s.split()     
    if not parts:
        print("none")
    else:
        print(parts[0])
