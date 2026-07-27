# 5
def build_reinforced_wall():

    for block in range(1, 21):

        if block % 4 == 0:
            block_type = "COBBLESTONE"
        else:
            block_type = "PLANK"

        print("Block", block, ":", block_type)

        if block % 5 == 0:
            print("Defense checkpoint reached!")

build_reinforced_wall()
# 6
def night_patrol():

    energy = 100
    minute = 1

    while minute <= 10:

        print("Minute", minute)
        print("Patrolling...")

        energy = energy - 12

        print("Energy:", energy)

        if minute % 3 == 0:
            print("Scanning area for mobs...")

        if energy < 30:
            print("Warning: Low power!")

        if energy <= 0:
            print("Shutdown...")
            break

        minute = minute + 1