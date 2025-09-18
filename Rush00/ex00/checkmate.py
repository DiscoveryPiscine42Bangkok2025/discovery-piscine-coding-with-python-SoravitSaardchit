def checkmate(board: str) -> None:
    try:
        rows = board.splitlines()
        n = len(rows)
        if n == 0 or any(len(r) != n for r in rows):
            print("error")
            return  
        kpos = [(r, c) for r in range(n) for c, ch in enumerate(rows[r]) if (ch == 'K' or ch == 'k')]
        if len(kpos) != 1:
            print("error")
            return 
        kr, kc = kpos[0]

        def first_in_dir(dr, dc):
            r, c = kr + dr, kc + dc
            while 0 <= r < n and 0 <= c < n:
                ch = rows[r][c]
                if ch in "KQRBP":
                    return ch
                r += dr
                c += dc
            return None
        for dc in (-1, 1):
            r, c = kr + 1, kc + dc
            if 0 <= r < n and 0 <= c < n and rows[r][c] == 'P':
                print("Success")
                return

        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            ch = first_in_dir(dr, dc)
            if ch in ("R", "Q"):
                print("Success")
                return
        for dr, dc in ((1, 1), (1, -1), (-1, 1), (-1, -1)):
            ch = first_in_dir(dr, dc)
            if ch in ("B", "Q"):
                print("Success")
                return
        print("Fail")
    except Exception:
        print("error")
        return