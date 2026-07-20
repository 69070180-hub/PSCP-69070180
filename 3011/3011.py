"""Colors"""

def main():
    """รับค่าสีมาสองสี และตั้ง if else ตามเงื่อนไขโดยถ้าเป็นแดงผสมเหลืองได้ส้ม, แดงผสมฟ้าได้ม่วง, เหลืองผสมฟ้าได้เขียว
    และถ้าหากเป็นสีเดี่ยวกันผสมกันเองก็จะได้เดิม และถ้าเกิดมีการให้สีนอกเหนือจากสามสีนี่ก็จะ Error"""

    A = input()
    B = input()

    if (A == "Red" and B == "Yellow") or (A == "Yellow" and B == "Red"):
        print("Orange")
    elif (A == "Red" and B == "Blue") or (A == "Blue" and B == "Red"):
        print("Violet")
    elif (A == "Yellow" and B == "Blue") or (A == "Blue" and B == "Yellow"):
        print("Green")
    elif A == B and A in ("Red", "Yellow", "Blue"):
        print(A)
    else:
        print("Error")

main()
