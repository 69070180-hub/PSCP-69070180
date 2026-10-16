"""Duplicate I"""

def main():
    """นำเลขนักศึกษาใส่ list แยกทั้งสองกลุ่มแล้วตรวจสอบว่ามีเลขซ้ำกันหรือไม่
    ถ้ามีให้แสดงเลขนั้นออกมา ถ้าไม่มีเลยให้แสดงข้อความ Nope"""
    m = int(input())
    n = int(input())

    g1 = []
    g2 = []

    for i in range(m):
        g1.append(int(input()))

    for i in range(n):
        g2.append(int(input()))

    count = 0
    dup = []

    for i in g1:
        if i in g2:
            dup.append(i)
            count += 1

    dup.sort(reverse=True)

    if not count:
        print("Nope")
    else:
        for i in dup:
            print(i)
main()
