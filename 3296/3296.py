"""RGB Mixed"""

def main():
    """นำสี RGB มาผสมกัน โดยการหาค่าเฉลี่ยของแต่ละสี"""
    R1, G1, B1 = map(int, input().split())
    R2, G2, B2 = map(int, input().split())

    R = (R1 + R2) // 2
    G = (G1 + G2) // 2
    B = (B1 + B2) // 2
    print(R, G, B)
main()
