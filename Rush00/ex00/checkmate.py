def checkmate(board: str) -> None:
    try:
        rows = board.splitlines()
        n = len(rows)
        # บอร์ดต้องเป็นสี่เหลี่ยมจัตุรัสและไม่ว่าง
        if n == 0 or any(len(r) != n for r in rows):
            print("error")
            return  # undefined -> ไม่พิมพ์อะไร

        # หา King ให้ได้ "ตัวเดียว"
        kpos = [(r, c) for r in range(n) for c, ch in enumerate(rows[r]) if (ch == 'K' or ch == 'k')]
        if len(kpos) != 1:
            print("error")
            return  # undefined -> ไม่พิมพ์อะไร
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
        # 1) Pawn โจมตีทแยง "ขึ้นด้านบน" (หมากเดินขึ้นบอร์ด):
        #    หมายความว่า ถ้ามี Pawn ที่ตำแหน่ง (kr+1, kc±1) จะเช็คได้
        for dc in (-1, 1):
            r, c = kr + 1, kc + dc
            if 0 <= r < n and 0 <= c < n and rows[r][c] == 'P':
                print("Success")
                return

        # 2) Rook / Queen แนวตรง
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            ch = first_in_dir(dr, dc)
            if ch in ("R", "Q"):
                print("Success")
                return

        # 3) Bishop / Queen แนวทแยง
        for dr, dc in ((1, 1), (1, -1), (-1, 1), (-1, -1)):
            ch = first_in_dir(dr, dc)
            if ch in ("B", "Q"):
                print("Success")
                return

        # ไม่โดนเช็ค
        print("Fail")

    except Exception:
        print("error")
        # undefined behavior -> เงียบและคืน control
        return