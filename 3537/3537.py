"""Impostor"""

def main():
    """ลบ {} และ " ออกจากข้อมูลผู้เล่น และแยกสีและบทบาทของผู้เล่นออกจากกัน
    จากนั้นเก็บข้อมูลผู้เล่นที่ยังมีชีวิตอยู่และผู้เล่นที่ตายแล้วแยกกัน
    และนับจำนวนผู้เล่นที่เป็น Impostor ที่ยังมีชีวิตอยู่"""
    Alive = []
    Dead = []
    Imposter = []

    while True:
        player = input()

        if player == "Start":
            break

        player = player.replace("{", "").replace("}", "").replace('"', "")
        player = player.split(":")

        color = player[0].strip()
        role = player[1].strip()

        player = color + " : " + role
        Alive.append(player)

        if role == "Impostor":
            Imposter.append(color)

    while True:
        color = input()

        if color == "End":
            break

        for player in Alive:
            kick = player.split(":")[0].strip()

            if kick == color:
                Alive.remove(player)
                Dead.append(player)

                if color in Imposter:
                    Imposter.remove(color)
                break

    Alive.sort()
    Dead.sort()

    print(len(Imposter), "Impostor Remains")

    print("***Alive***")
    for player in Alive:
        print(player)

    print("***Dead***")
    for player in Dead:
        print(player)
main()
