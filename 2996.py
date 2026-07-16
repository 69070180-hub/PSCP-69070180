"""สลับตัวอักษร"""

def main():
    """ทำให้คำที่ in put เข้าไปกลับหลังก่อน แล้วค่อย print ออกมาเป็นตัวอักษรตัวเล็ก"""
    text = input()
    real = text[::-1]

    print(real.lower())

main()
