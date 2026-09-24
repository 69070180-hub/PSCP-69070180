"""แปลงดอกไม้"""

def main():
    """ไล่ไปที่ละเส้นโดยให้ band เป็นแถบปัจจุบัน
    line เป็นเส้นที่เท่าไหร่ในแถบ
    current เป็นเส้นปัจจุบัน
    tatal จำนวนช่องที่ใช้ไปในปัจจุบัน"""
    L, N=  map(int, input().split())

    band = 1
    line = 1
    current = 1
    total = 1

    while N > total:
        if line < L:
            line += 1
            current += 1
            total += current
        else:
            line = 1
            current += 1
            band += 1
            total += current

    print(band)
main()
