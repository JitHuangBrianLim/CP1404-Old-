# 1
output_file = open('name.txt', 'w')
name = input("Enter name: ")
print(name, file=output_file)
output_file.close()

# 2
input_file = open("name.txt", "r")
name = input_file.read()
input_file.close()
print("Your name is", name)

# 3
input_file = open("numbers.txt", "r")
first_number = int(input_file.readline())
second_number = int(input_file.readline())
input_file.close()
print(first_number + second_number)

# 4
input_file = open("numbers.txt", "r")
total = 0
for i in input_file:
    number = int(i)
    total += number
input_file.close()
print(total)