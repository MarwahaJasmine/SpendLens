
# 1. Create and Print a List
print("\n--- 1. Create and Print a List ---")
favorite_foods = ["pizza", "sushi", "tacos", "ramen", "mango"]
print(favorite_foods)

# Advanced: ask the user to enter their five favorite foods
# user_foods = []
# for i in range(5):
#     food = input(f"Enter favorite food #{i + 1}: ")
#     user_foods.append(food)
# print(user_foods)

# 2. Accessing Elements in a List
print("\n2. Accessing Elements in a List")
colors = ["red", "blue", "green", "yellow", "purple"]
print("First color:", colors[0])
print("Last color:", colors[-1])


# 3. Modifying a List
print("\n--- 3. Modifying a List ---")
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
fruits.remove("banana")
print(fruits)


# 4. List Slicing
print("\n--- 4. List Slicing ---")
numbers = [2, 4, 6, 8, 10, 12]
print("First three:", numbers[0:3])


# 5. Sorting a List
print("\n--- 5. Sorting a List ---")
marks = [87, 45, 78, 92, 66]
marks.sort()
print("Sorted marks:", marks)

# Advanced: calculate and print the average of the marks
average = sum(marks) / len(marks)
print("Average mark:", average)


print("\n" + "=" * 50)
print("PRACTICE WITH TUPLES")
print("=" * 50)

# 1. Creating a Tuple
print("\n--- 1. Creating a Tuple ---")
subjects = ("Math", "Science", "History", "Art")
print(subjects)

# Advanced: loop through and print subjects with more than 5 letters
print("Subjects with more than 5 letters:")
for subject in subjects:
    if len(subject) > 5:
        print(subject)

# 2. Accessing Tuple Items
print("\n--- 2. Accessing Tuple Items ---")
animals = ("cat", "dog", "rabbit", "hamster")
print("Second animal:", animals[1])

# Advanced: count how many animals contain the letter 'a'
count_a = 0
for animal in animals:
    if "a" in animal:
        count_a += 1
print("Animals containing 'a':", count_a)

# 3. Tuple Immutability
print("\n--- 3. Tuple Immutability ---")
try:
    animals[0] = "lion"
except TypeError as e:
    print("Error:", e)
    print("Tuples are immutable, so you can't change an item directly.")

# 4. Tuple Length and Properties
print("\n--- 4. Tuple Length and Properties ---")
print("Number of items in animals tuple:", len(animals))


# 1. Creating a Dictionary
print("\n--- 1. Creating a Dictionary ---")
birthdays = {
    "Maya": "March 4",
    "Leo": "July 19",
    "Sam": "November 2"
}
print(birthdays)


# 2. Access and Update Dictionary Items
print("\n--- 2. Access and Update Dictionary Items ---")
student = {"name": "Alex", "grade": 8, "school": "Sunrise Middle"}
print("Name:", student["name"])
student["grade"] = 9
print("Updated dictionary:", student)


# 3. Adding Items to a Dictionary
print("\n--- 3. Adding Items to a Dictionary ---")
student["hobby"] = "painting"
print("With hobby added:", student)


# 4. Looping Through a Dictionary
print("\n--- 4. Looping Through a Dictionary ---")
person = {"name": "Ravi", "age": 14, "city": "Seattle"}
for key, value in person.items():
    print(key, ":", value)



print("\n" + "=" * 50)
print("PRACTICE WITH SETS")
print("=" * 50)

# 1. Creating and Printing a Set
print("\n--- 1. Creating and Printing a Set ---")
favorite_numbers_set = {4, 8, 15, 16}
print(favorite_numbers_set)


# 2. Adding and Removing Elements in a Set
print("\n--- 2. Adding and Removing Elements in a Set ---")
my_set = {1, 2, 3}
my_set.add(4)
my_set.remove(2)
print(my_set)


# 3. Set Operations
print("\n--- 3. Set Operations ---")
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print("Union:", set1 | set2)
print("Intersection:", set1 & set2)


# 4. Handling Duplicates in Sets
print("\n--- 4. Handling Duplicates in Sets ---")
duplicate_test = {1, 2, 3}
duplicate_test.add(2)  # adding a duplicate
print("After adding a duplicate:", duplicate_test)
print("Explanation: sets automatically ignore duplicates, so the set stays the same.")
