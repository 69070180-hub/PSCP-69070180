"""หาร 10"""

def main():
    """ปรับให้เลขเป็นจำนวนที่หาร 10 ลงตัวแล้วทำการแสดงผลลัพธ์ลดลงทีละ 10 จนถึง 0"""
    num = int(input())

    a = num % 10
    N = num - a

    for i in range(N , -1 , -10):
        print(i, end=" ")

main()
