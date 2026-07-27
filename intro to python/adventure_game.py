print("WELCOME TO THE ADVENTURE!")

# Player inventory (list)
#inventory = []

# Game world (dictionary)
locations = {
    "forest": {
        "description": "You are standing in a forest. You see a cave and a river."
    },
    "cave": {
        "description": "The cave is dark. You see a treasure chest."
    },
    "river": {
        "description": "A fast river blocks your path."
    }
}

print(locations["forest"]["description"])

# First choice
choice = input("Where do you want to go? (cave/river): ").lower().strip()

# CAVE

if choice == "cave":

    print(locations["cave"]["description"])

    choice = input("Do you take the flashlight? (yes/no): ").lower().strip()

    if choice == "yes":
        inventory.append("flashlight")
        print("You picked up the flashlight!")
    else:
        print("You leave the flashlight behind.")

    print("You open the treasure chest.")

    if "flashlight" in inventory:
        print("You can see inside the chest.")
        print("🎉 You found the treasure!")
        print("YOU WIN!")
    else:
        print("It is too dark to see.")
        print("You fall into a hole.")
        print("GAME OVER!")

# RIVER

elif choice == "river":

    print(locations["river"]["description"])

    choice = input("Do you swim or go back? (swim/back): ").lower().strip()

    if choice == "swim":
        print("The river is too strong.")
        print("GAME OVER!")

    elif choice == "back":
        print("You safely return to the forest.")
        print("Maybe try exploring the cave next time!")

    else:
        print("That is not a valid choice.")

# INVALID CHOICE

else:
    print("You didn't go to the cave or river.")
    print("You got lost in the forest.")
    print("GAME OVER!")

# FINAL INVENTORY

#print("\nInventory:")
#print(inventory)

print("\nThanks for playing!")