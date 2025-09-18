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
    if '"' in line or "'" in line:
        try:
            parts = shlex.split(line)
        except ValueError:
            parts = []
        first = parts[0] if parts else line
    else:
        first = line
    print(first.upper())
