"""Ink"""

import math

def main():
    """รับค่า s และ n จากนั้นรับค่า x และ y n ครั้ง แล้วคำนวณพื้นที่ของ
    วงกลมที่มีรัศมี x และ y จากนั้นหารด้วย s และปัดขึ้นเป็นจำนวนเต็ม"""
    s , n = map(int, input().split())
    answer = []

    for i in range(n):
        x , y = map(int, input().split())

        t = 3.1416*(x**2 + y**2)/s

        answer.append(math.ceil(t))

    for i in answer:
        print(i)

main()
