a = input(" ")
b = input(" ")
if a.strip() == "" or b.strip() == "":
    print("none")
else:
  words = range(int(a),int(b)+1)
  print(list(words))
