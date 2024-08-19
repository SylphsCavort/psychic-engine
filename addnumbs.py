# This is v1.2

def adds_numbs(num_1, num_2):
    result = num_1 + num_2
    print(result)

def combineit(num_1, num_2):
    result = str(num_1) + str(num_2)
    print(result)

user_input = input('Type "add" or "combine" > ')

num_1 = int(input("First number > "))
num_2 = int(input("Second number> "))

# Output based on first user choice
if user_input == "add":
    adds_numbs(num_1,num_2)

elif user_input == "combine":
    combineit(num_1,num_2)
