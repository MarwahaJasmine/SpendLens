
# DIGITAL PET GAME

print("Welcome to the Digital Pet Game!")

# Pet setup
pet_name = input("What is your pet's name? ")

pet_type = input("Choose a pet type (dog / cat / dragon / other): ").lower()

# validate pet type
while pet_type not in ["dog", "cat", "dragon", "other"]:
    pet_type = input("Invalid choice. Please enter dog, cat, dragon, or other: ").lower()

# assign emoji
if pet_type == "dog":
    pet_emoji = "🐶"
elif pet_type == "cat":
    pet_emoji = "🐱"
elif pet_type == "dragon":
    pet_emoji = "🐉"
else:
    pet_emoji = "🐾"

# starting stats 
hunger = 80
happiness = 80
health = 100
energy = 80

print("\nYour pet is " + pet_name + " the " + pet_type + " " + pet_emoji + "!\n")

# game loop - 5 turns
turn = 1

for turn in range(1, 6):

    print("TURN", turn)
    # stat bars 
    hunger_bar = "X" * (hunger // 10)
    happiness_bar = "X" * (happiness // 10)
    health_bar = "X" * (health // 10)

    # mood
    if happiness >= 80:
        mood = "Ecstatic"
    elif happiness >= 60:
        mood = "Happy"
    elif happiness >= 40:
        mood = "Okay"
    elif happiness >= 20:
        mood = "Sad"
    else:
        mood = "Miserable"

    print("Hunger:     ", hunger_bar)
    print("Happiness:  ", happiness_bar)
    print("Health:     ", health_bar)
    print("Mood:       ", mood)

    # menu 
    print("\nChoose an action:")
    print("1. Feed")
    print("2. Play")
    print("3. Sleep")

    choice = input("Enter 1, 2, or 3: ")

    # validate input
    while choice not in ["1", "2", "3"]:
        choice = input("Invalid choice. Enter 1, 2, or 3: ")

    # actions 
    if choice == "1":
        print("You fed your pet!")
        hunger += 25
        happiness += 10
        health -= 5

    elif choice == "2":
        print("You played with your pet!")
        happiness += 25
        hunger -= 15
        health += 5

        if pet_type == "dog":
            print("Dog bonus! Extra happiness +10")
            happiness += 10

    else:
        print("You put your pet to sleep!")
        health += 20
        happiness += 10
        hunger -= 10

        if pet_type == "cat":
            print("Cat bonus! Extra health +10")
            health += 10

    # natural decay 
    hunger -= 10
    happiness -= 5

    if pet_type == "dragon":
        hunger -= 10  # extra decay

    # starvation penalty 
    if hunger <= 0:
        health -= 15
        hunger = 0

    # safety checks 
    if hunger > 100:
        hunger = 100
    if happiness > 100:
        happiness = 100
    if health > 100:
        health = 100

    if hunger < 0:
        hunger = 0
    if happiness < 0:
        happiness = 0
    if health < 0:
        health = 0

    # warnings 
    if hunger < 20:
        print("Warning: Your pet is very hungry!")
    if happiness < 20:
        print("Warning: Your pet is very sad!")
    if health < 20:
        print("Warning: Your pet is very unhealthy!")

    # game over 
    if health == 0:
        print("\nGAME OVER! Your pet could not survive.")
        break

# FINAL SCORE
average = (hunger + happiness + health) // 3
score = average * turn

print("FINAL SCORE:", score)

if score >= 400:
    print("Legendary Owner!")
elif score >= 300:
    print("Great Owner")
elif score >= 200:
    print("Good Owner")
else:
    print("Keep Practicing")