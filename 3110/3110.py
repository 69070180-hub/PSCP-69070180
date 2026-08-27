"""สงคราม...ส่งด่วน"""

def main():
    """ตรวจเส้นทางตามเงื่อนไข และคำนวณราคาน้ำหนักตามเงื่อนไข"""
    start , end = input().split()
    W = float(input())


    if start == "BKK" and end == "CNX":
        price = 10 + W * 30
        print(f"{price:.2f}")
    elif start == "CNX" and end == "UBP":
        price = 15 + W * 40
        print(f"{price:.2f}")
    elif start == "UBP" and end == "BKK":
        price = 20 + W * 40
        print(f"{price:.2f}")
    elif start == "BKK" and end == "PKT":
        price = 25 + W * 50
        print(f"{price:.2f}")
    elif start == "PKT" and end == "CNX":
        price = 30 + W * 60
        print(f"{price:.2f}")
    elif start == "UBP" and end == "PKT":
        price = 40 + W * 70
        print(f"{price:.2f}")
    else:
        print("Error")
main()
