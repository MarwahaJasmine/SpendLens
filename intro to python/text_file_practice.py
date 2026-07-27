# write
file = open("my_info.txt", "w")
file.write("Name: Jasmine\n")
file.write("Favorite Food: Thai food\n")
file.close()

# read
file = open("my_info.txt", "r")
contents = file.read()
print(contents)
file.close()

# append
file = open("my_info.txt", "a")
file.write("\nFavorite Color: Blue")
file.close()


# story
file = open("story.txt", "r")
count = 0
for line in file:
    count += 1
print("Number of lines:", count)
file.close()


# with statement
with open("my_info.txt", "r") as file:
    contents = file.read()
    print(contents)
