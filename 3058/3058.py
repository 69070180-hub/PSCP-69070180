"""BrickBridge"""

def main():
    """หาจำนวนอิฐใหญ่ที่ต้องใช้ แต่ไม่เกินจำนวนอิฐใหญ่ที่มีอยู่
    และจะได้ขนาดที่เหลืออยู่ หากอิฐเล็กมีน้อยกว่าขนาดที่เหลืออยู่ จะได้ -1"""
    a = int(input())
    b = int(input())
    goal = int(input())

    b_use = min(b , goal // 5)
    left = goal - b_use * 5

    if left > a:
        print(-1)
    else:
        print(left)
main()
