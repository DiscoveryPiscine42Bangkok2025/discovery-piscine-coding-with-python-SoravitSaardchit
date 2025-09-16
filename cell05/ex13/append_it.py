a = input(" ")
if a == " ":
  print("none")
else:
  for i in a.split() :
    if not i.endswith("ism"):
        i = i+"ism"
        print(i)
    else:
      continue
