"""BigFrame"""

def  main():
    """ตรวจคำที่ยาวที่สุดเพื่อสร้างกรอบ และพิมพ์ออกมา"""
    a = input()
    b = input()
    c = input()
    d = input()
    e = input()

    Main = [a, b, c, d, e]
    longest = len(max(Main, key=len))
    Line = longest + 4

    print("*" * Line)
    for i in Main:
        print("* " + i + " " * (longest - len(i)) + " *")
    print("*" * Line)
main()
