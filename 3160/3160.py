"""หาจำนวนเฉพาะ"""

def main():
    """ให้ทำการหาจำนวนเฉพาะในช่วง a ถึง b โดยให้แสดงผลลัพธ์เป็นจำนวนเฉพาะทั้งหมด
    และจำนวนเฉพาะทั้งหมดที่เจอ"""
    a , b = map(int, input().split())

    def prime(num):
        if num < 2:
            return False

        for i in range(2, num):
            if num % i == 0:
                return False

        return True

    prime_num = []

    for i in range(a, b + 1):
        if prime(i):
            prime_num.append(i)

    if len(prime_num) == 0:
        print(f"Total primes: {len(prime_num)}")
    else:
        print(*prime_num)
        print(f"Total primes: {len(prime_num)}")
main()
