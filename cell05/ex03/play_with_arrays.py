from array import array
c = array('i', [10,11,50,10,24])
c_unique = array(c.typecode, set(c))   
print(c_unique.tolist())
