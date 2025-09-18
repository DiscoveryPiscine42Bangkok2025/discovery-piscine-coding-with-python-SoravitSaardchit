<<<<<<< HEAD
s = input().strip()   
if not s:
    print("none")
else:
    count = s.count('z')   
    if count == 0:
        print("none")
    else:
        print('z' * count)
=======
a = input(" ")
if a == " ":
  print("none")
else:
  count =  0
  for i in a:
    if i == 'z':
        count = count+1
  if count == 0:
      print("none")
  else:
      print(count)
>>>>>>> main
