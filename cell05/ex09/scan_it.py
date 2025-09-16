a = input(" ").strip()
b = input(" ").strip()
words = b.split() 
if a == " " or b == " ":
 print("none")
else:
  count = 0
  for i in words:
    if i == a:
        count = count+1
  print(count)
  
