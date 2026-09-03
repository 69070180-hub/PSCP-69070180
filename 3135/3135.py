"""ของขวัญและขโมย"""

def main():
    """ให้ทำการวนไปจนกว่าจะเจอของขวัญไปอยู่กับขโมย
    หรือกลับไปที่จุดเริ่มต้น โดยหากมีคนที่เคยตรวจไปแล้วก็ไม่ต้อง
    นับคนคนนั้นเข้า set อีก"""
    N, K, T = map(int, input().split())
    a = 1
    num = {1}

    if T == 1:
        print(1)
        return
    else:
        while True:
            a = ((a - 1 + K) % N) + 1

            num.add(a)

            if a == T or a == 1:
                break

    print(len(num))
main()
