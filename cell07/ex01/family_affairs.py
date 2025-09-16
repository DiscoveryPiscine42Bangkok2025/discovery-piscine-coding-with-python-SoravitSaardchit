def find_the_redheads(a):
  x = []
  for i,j in a.items():
    if j == "red":
      x.append(i)
  return x
dupont_family = {
"florian": "red",
"marie": "blond",
"virginie": "brunette",
"david": "red",
"franck": "red"
}
print(find_the_redheads(dupont_family))
