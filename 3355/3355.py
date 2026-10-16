"""Shorten"""

def main():
    """ตรวจสอบว่าเลขใหม่มีค่าห่างจากเลขก่อนหน้าหรือไม่ 
    ถ้าใช่ให้บันทึกช่วงตัวเลขและเริ่มช่วงใหม่"""
    num = []
    start = None
    end = None

    while True:
        n = int(input())

        if n == -1:
            break

        if start is None:
            start = n
            end = n
        elif n == end + 1:
            end = n
        else:
            if start == end:
                num.append(str(start))
            else:
                num.append(str(start) + "-" + str(end))

            start = n
            end = n

    if start is not None:
        if start == end:
            num.append(str(start))
        else:
            num.append(str(start) + "-" + str(end))

    print(", ".join(num))
main()
