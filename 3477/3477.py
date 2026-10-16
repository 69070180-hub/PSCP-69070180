"""Pad Thai"""

def main():
    """ตรวจสอบส่วนผสมและรสชาติของผัดไทย"""
    ingredients = {"Pad Thai Sauce", "Tofu", "Pickle Turnip",
                "Shrimp", "Bean Sprouts", "Noodle", 
                "Chives", "Lime", "Egg", "Oil", "Peanuts"}

    flavors = {"Sweet", "Sour", "Salty"}

    used_ingredients = set()
    used_flavors = set()

    while True:
        item = input()

        if item == "Cook":
            break

        used_ingredients.add(item)

    while True:
        flavor = input()

        if flavor == "End":
            break

        used_flavors.add(flavor)

    if not used_ingredients.issubset(ingredients):
        print("This is not Pad Thai!!!")

    elif used_ingredients != ingredients:
        print("This is bad!")

    elif used_flavors != flavors:
        print("Not Bad...")

    else:
        print("Delicious!")
main()
