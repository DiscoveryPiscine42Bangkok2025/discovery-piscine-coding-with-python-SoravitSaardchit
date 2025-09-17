s = input().strip()        
if not s:
    print("none")
else:
    for w in s.split():
        if not w.endswith("ism"):
            print(w + "ism")
