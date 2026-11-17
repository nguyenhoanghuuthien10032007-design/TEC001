def calculate_sum(numbers_list):
    return sum(numbers_list)
if __name__ == "__main__":
    my_list = [10, 25, 30, 45, 50]
    total = calculate_sum(my_list)
    print(f"Original list: {my_list}")
    print(f"The sum of all numbers is: {total}")