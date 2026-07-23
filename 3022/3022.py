"""Temperature"""

def main():
    """ทำการรับค่าอุณหภูมิที่ได้มา แล้วเปลี่ยนเป็นหน่วยเซลเซียสก่อน แล้วค่อยเปลี่ยนเป็นหน่วยที่ต้องการ"""

    num = float(input())
    a = input()
    b = input()

    if a == "C":
        c = num
    elif a == "F":
        c = (num - 32) * 5 / 9
    elif a == "K":
        c = num - 273.15
    elif a == "R":
        c = (num - 491.67) * 5 / 9

    if b == "C":
        print(f"{c:.2f}")
    elif b == "F":
        print(f"{c * 9 / 5 + 32:.2f}")
    elif b == "K":
        print(f"{c + 273.15:.2f}")
    elif b == "R":
        print(f"{c * 9 / 5 + 491.67:.2f}")

main()
