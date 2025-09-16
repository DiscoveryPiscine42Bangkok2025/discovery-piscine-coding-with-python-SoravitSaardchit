s = input("")  
words = s.split()   
if s == " ":
 print("none")
else:
  for a in words:
    print(a.lower(),end = " ")
