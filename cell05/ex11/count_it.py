s = input()
if not s.strip():
    print("none")
else:
    words = [w.strip('"\'') for w in s.split()]  
    print(f"parameters: {len(words)}")
    for w in words:
        print(f"{w} : {len(w)}")
