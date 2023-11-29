import random

def initialize_boxes():
    return {
        "box1": {"distance": random.randint(1, 10), "weight": random.randint(1, 10)},
        "box2": {"distance": random.randint(1, 10), "weight": random.randint(1, 10)},
        "box3": {"distance": random.randint(1, 10), "weight": random.randint(1, 10)}
    }

def check_cargo(boxes, marks):
    total_weight = 0

    for mark in marks:
        if mark in boxes:
            total_weight += boxes[mark]["weight"]
            print(f"Box at {boxes[mark]['distance']} km found with {boxes[mark]['weight']} kg")

            
            boxes[mark]["distance"] = random.randint(1, 10)
            boxes[mark]["weight"] = random.randint(1, 10)
        else:
            print(f"No box at {mark} km")

    return total_weight

def main():
    print("Hello, This is the helping the Martians Programm!")
    print("Mars boxes have been scattered along the path. Your mission is to find them.")

    boxes = initialize_boxes()
    correct_weight = False

    while not correct_weight:
        marks = [int(input("Enter the kilometer mark: ")) for _ in range(3)]
        total_weight = check_cargo(boxes, marks)

        if total_weight == 713:
            correct_weight = True
            print("Hooray!!! All boxes with the correct weight was founded.")
        else:
            print(f"ERROR!Total weight is {total_weight} kg. Try again!")

if __name__ == "__main__":
    main()
