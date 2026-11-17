def remove_uneven_numbers(numbers_list):
    even_list = [num for num in numbers_list if num % 2 == 0]
    return even_list
if __name__ == "__main__":
    original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    cut_down_list = remove_uneven_numbers(original_list)
    
    print(f"Original list: {original_list}")
    print(f"Cut-down list (without uneven numbers): {cut_down_list}")