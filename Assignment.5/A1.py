numbers = []
print("Enter numbers (press Enter without typing anything to quit):")
while True:
    user_input = input("Enter a number: ")
    if user_input == "":
        break
    numbers.append(float(user_input))
numbers.sort(reverse=True)
five_greatest = numbers[:5]
print("The five greatest numbers in descending order:")
for num in five_greatest:
    print(num)