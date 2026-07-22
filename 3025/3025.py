"""Season"""

def main():
    """รับค่าเลขมาสองตัวตัวแรกคือเดือน ตัวที่สองคือวัน จากนั้นให้แสดงผลฤดูกาลของวันนั้น 
    ไตรมาสแรกคือ winter ไตรมาสสองคือ spring ไตรมาสสามคือ summer ไตรมาสสี่คือ fall 
    โดยให้พิจารณาวันที่ 21 ของเดือนมีนาคม มิถุนายน กันยายน และธันวาคมเป็นวันเปลี่ยนฤดูกาล"""

    month = int(input())
    day = int(input())

    if month == 1 or month == 2 or month == 3:
        if month == 3 and day >= 21:
            print("spring")
        else:
            print("winter")
    elif month == 4 or month == 5 or month == 6:
        if month == 6 and day >= 21:
            print("summer")
        else:
            print("spring")
    elif month == 7 or month == 8 or month == 9:
        if month == 9 and day >= 21:
            print("fall")
        else:
            print("summer")
    elif month == 10 or month == 11 or month == 12:
        if month == 12 and day >= 21:
            print("winter")
        else:
            print("fall")
    
main()
