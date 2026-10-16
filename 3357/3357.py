"""Giraffe"""

def main():
    """นำความสูงทุกตัวใส่ใน list และตรวจสอบว่าทั้งสองข้างสูงกว่าหรือไม่"""
    n = int(input())
    Giraffe = []
    count = 0

    Giraffe.append(0)

    for i in range(n):
        h = int(input())
        Giraffe.append(h)

    Giraffe.append(0)
    num = len(Giraffe)

    for i in range(num):
        if Giraffe[i] > Giraffe[i - 1] and Giraffe[i] > Giraffe[i + 1]:
            count += 1

    print(count)
main()
