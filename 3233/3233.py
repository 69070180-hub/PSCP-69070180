"""สลากกินแบ่ง"""

def main():
    """ตรวจอักษรก่อนว่าเหมือนกันหรือไม่ แล้วค่อยตรวจตัวเลข
    หลังจากนั้นก็ค่อยให้รางวัลตามเงื่อนไขที่กำหนด"""
    a1, b1 = input().split()
    a2, b2 = input().split()

    if a1 == a2:
        if b1 == b2:
            print(1000000)
        elif b1[-3:] == b2[-3:]:
            print(2000)
        elif b1[-2:] == b2[-2:]:
            print(1000)
        else:
            print(20)
    else:
        if b1 == b2:
            print(100000)
        elif b1[-3:] == b2[-3:]:
            print(200)
        elif b1[-2:] == b2[-2:]:
            print(100)
        else:
            print(0)
main()
