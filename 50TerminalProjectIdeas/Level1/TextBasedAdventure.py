name = input("Enter your character's name:   ")
print("Welcome", name, "to this adventure!")
print("You are in a dark, dingy, and humid cave searching for the lost treasure of Captain Skullbeard.")
print("You are disoriented, lost, hungry, and thirsty.")
print("You see a speck of light in the distance ahead of you, something shimmering to your right, and the sound of running water to your left.")
print("Which direction would you like to head? (Type 'forward', 'right', or 'left')")
direction = input("Direction:   ")

if direction == "forward":
    print("You move forward cautiously, the light growing brighter.")
    print("As you approach, you realize it's the exit of the cave leading to a beautiful beach!")
    print("You have successfully escaped the cave and found the treasure on the beach!")
elif direction == "right":
    print("You head right towards the shimmering object.")
    print("You walk for what feels like hours.")
    print("Suddenly, you encounter a ferocious dragon blocking your path!")
    print("Do you choose to (1) fight the dragon, (2) befriend the dragon, or (3) run away?")
    action = input("Action (1, 2, or 3):   ")
    if action == "1":
        print("You bravely fight the dragon and emerge victorious!")
        print("You find the treasure behind the dragon's lair.")
        print("Congratulations",name)
    elif action == "2":
        print("You offer the dragon some food, and it becomes your ally.")
        print("With the dragon's help, you find the treasure easily!")
        print("Congratulations",name)
    elif action == "3":
        print("You run away safely, but miss out on the treasure.")
    else:
        print("Invalid action. Please choose 1, 2, or 3.")
elif direction == "left":
    print("You follow the sound of running water.")
    print("You find a beautiful underground river with sparkling water.")
    print("You drink the water and feel rejuvenated.")
    print("As you explore further, you find a hidden passage leading to the treasure!")
    print("A wild dragon appears!")
    print("Do you choose to (1) fight the dragon, (2) befriend the dragon, or (3) run away?")
    action = input("Action (1, 2, or 3):   ")
    if action == "1":   
        print("You bravely fight the dragon and emerge victorious!")
        print("You find the treasure behind the dragon's lair.")
        print("Congratulations",name)
    elif action == "2":
        print("You offer the dragon some food, and it becomes your ally.")
        print("With the dragon's help, you find the treasure easily!")
        print("Congratulations",name)
    elif action == "3":
        print("You run away safely, but miss out on the treasure.")
    else:
        print("Invalid action. Please choose 1, 2, or 3.")
else:
    print("Invalid direction. Please choose 'forward', 'right', or 'left'.")


