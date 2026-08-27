"""A-E-I-O-U"""

def main():
    """ให้ตรวจจับจำนวนสระในคำที่ผู้ใช้ป้อนเข้ามา"""
    word = input().lower()

    vowels = ["a", "e", "i", "o", "u"]

    for i in vowels:
        count = word.count(i)

        if count > 0:
            print(f"{i} : {count}")
main()
