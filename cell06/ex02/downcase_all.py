def downcase_it(a):
  return a.lower()
a = input(" ")
b = input(" ")
if a == " " or b == " ":
  print("none")
else:
  print(downcase_it(a))
  print(downcase_it(b))
