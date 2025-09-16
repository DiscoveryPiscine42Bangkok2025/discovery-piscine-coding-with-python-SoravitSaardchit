s = input("")  
words = s.split() 
if s == " ":
 print("none")
else:
  print(f"parameters: {len(words)}")
  for i in words:
    print(f"{i} : {len(i)}")
