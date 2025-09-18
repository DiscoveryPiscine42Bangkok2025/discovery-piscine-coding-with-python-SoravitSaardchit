from array import array
a = array('i', [2, 8, 9, 48, 8, 22, -12, 2])
c = array('i', (x + 2 for x in a if x > 5))
unique = set(c)
print(a.tolist())  
print(unique)     
