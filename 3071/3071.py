"""จำนวนในช่วง [A,B]"""

def main():
    """ให้เลขตั้งแต่ A หาร d ไปเรื่อยๆ จนถึง B
    และถ้าหารออกมาแล้วเศษเท่ากับ r ให้เก็บจำนวนไว้"""
    A = int(input())
    B = int(input())
    d = int(input())
    r = int(input())

    count = 0

    for x in range(A, B + 1):
        if x % d == r:
            count += 1

    print(count)
main()
