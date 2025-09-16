def shrink(a):
  print(a[0:8])

def enlarge(b):
  for i in range(0,(8-len(b))-1):
    b = b+"z"
  print(b)
a = input(" ")
for i in a.split():
  if len(i) > 8:
    shrink(i)
  elif len(i) < 8:
    enlarge(i)
  else:
    print(i)
