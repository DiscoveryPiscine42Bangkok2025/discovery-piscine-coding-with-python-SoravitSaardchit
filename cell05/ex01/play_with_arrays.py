from array import array
a = array('i',[2, 8, 9, 48, 8, 22, -12, 2])
print("Original array: ",a.tolist())
for idx in range(len(a)):
    a[idx] += 2
print("New array: ",a.tolist())
