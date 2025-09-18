import shlex
def read_line():
    try:
        return input().strip()
    except EOFError:
        return ""
line = read_line()
if not line:
    print("none")
else:
    try:
        parts = shlex.split(line)
    except ValueError:
        parts = line.split()   
    if not parts:
        print("none")
    else:
        print(parts[0].lower())
