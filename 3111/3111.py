"""สหกรณ์โรงเรียน"""
import math

def main():
    """ตรวจสอบว่ามีส่วนลดหรือไม่ตามเงื่อนไขที่กำหนด"""
    YN = input()
    num = int(input())
    price = 0

    for _ in range(num):
        price += float(input())

    if YN == "Y":
        de = price * 0.05
        pay = price - de
    elif YN == "N" and price >= 500:
        de = price * 0.03
        pay = price - de
    else:
        pay = price

    pay = math.ceil(pay * 100) / 100
    print(f"{pay:.2f}")
main()
