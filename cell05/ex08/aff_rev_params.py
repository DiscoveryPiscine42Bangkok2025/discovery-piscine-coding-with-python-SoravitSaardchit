import shlex
try:
    line = input().strip()
except EOFError:
    line = ""

if not line:
    print("none")
else:
    parts = shlex.split(line)
    if len(parts) < 2:
        print("none")
    else:
        for p in reversed(parts):
            print(p)
