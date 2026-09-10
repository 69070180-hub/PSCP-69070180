"""ไพ่ 44 ใบ"""

def main():
    """ตรวจสอบอักษรทุกตัวที่ไม่ใช่ตัวท้ายของสตริง และแปลงเป็นตัวที่กำหนด
    หลังจากนั้นตรวจสอบตัวท้ายของสตริงเพื่อแปลงเป็นกลุ่มไพ่ที่ถูกต้อง"""
    n = input().upper()

    if n[:-1] == "A":
        a = "ace"
    elif n[:-1] == "J":
        a = "jack"
    elif n[:-1] == "Q":
        a = "queen"
    elif n[:-1] == "K":
        a = "king"
    else:
        a = n[:-1]

    if n[-1] == "D":
        b = "diamonds"
    elif n[-1] == "H":
        b = "hearts"
    elif n[-1] == "S":
        b = "spades"
    elif n[-1] == "C":
        b = "clubs"
    else:
        b = "nothing"

    print(a + " of " + b)
main()
