# Task 5
CORRECT_USER = "python"
CORRECT_PASS = "rules"

attempts = 0
max_attempts = 5

while attempts < max_attempts:
    username = input("Username: ")
    password = input("Password: ")
    
    if username == CORRECT_USER and password == CORRECT_PASS:
        print("Welcome")
        break
    else:
        attempts += 1
        remaining_attempts = max_attempts - attempts
        
        if remaining_attempts > 0:
            print(f"Wrong information! You still have {remaining_attempts} time(s) to try.\n")

if attempts == max_attempts:
    print("Access denied")