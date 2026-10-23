"""isPrime_large"""

def main():
    """ทำการตรวจสอบจำนวนเฉพาะ 
    โดยใช้วิธีการตรวจสอบตัวหารตั้งแต่ 2 
    จนถึงรากที่สองของจำนวนที่รับเข้ามา"""
    n = int(input())
    i = 2

    if n < 2:
        print("NO")
        return

    while i * i <= n:
        if not n % i:
            print("NO")
            return
        i += 1

    print("YES")
main()
