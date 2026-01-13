print("hello")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

user_fruit = input("Enter your favorite fruit: ")
if user_fruit in fruits:
    print("I like that fruit too!") 
else:
    print("That's not a fruit I know. There are only " + ", ".join(fruits))