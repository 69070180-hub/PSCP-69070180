"""เกมสะสมแต้ม"""

def main():
    """รับเลขจำนวนรอบและตรวจคำสั่ง + หรือ - 
    เพื่อคำนวณคะแนนสะสม"""
    num = int(input())
    count = 0

    for _ in range(num):
        n = input()
        if n == "+":
            count += 10
        elif n == "-":
            count -= 5

    print(count)
main()
