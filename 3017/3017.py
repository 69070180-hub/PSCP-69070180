"""Bill"""

def main():
    """ทำการรับราคามา และนำไปคูณกับ 10% เพื่อหาค่าบริการ หากค่าบริการน้อยกว่า 50 ให้ใช้ 50 หากมากกว่า 1000 ให้ใช้ 1000 
    จากนั้นนำไปบวกกับราคาสินค้า และคำนวณ VAT 7% และหาผลรวมทั้งหมด"""

    price = float(input())

    S = price * 0.1
    if S < 50:
        S = 50
    elif S > 1000:
        S = 1000

    sub_now = price + S
    VAT = sub_now * 0.07
    total = sub_now + VAT

    print(f"{total:.2f}")

main()
