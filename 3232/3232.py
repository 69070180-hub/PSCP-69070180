"""กบน้อยกระโดด"""

def main():
    """ให้นับระยะทางและจำนวนครั้งที่กบกระโดด
    ลูป while จะทำงานจนกว่ากบจะกระโดดถึงระยะทางที่กำหนดหรือกระโดดไม่ไหว
    หากกบกระโดดไม่ถึงระยะทางที่กำหนดให้แสดงผล -1"""
    x, y = map(int, input().split())
    way = 0
    count = 0

    while x > 0 and way < y:
        way += x
        count += 1
        x -= 2

    if way < y:
        print(-1)
    else:
        print(count)
main()
