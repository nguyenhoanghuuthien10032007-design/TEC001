while True:
    inches = float(input("Enter converts inches to centimeters: "))
    if inches < 0:
        print("Exit to program")
        break
    cm = inches * 2.54
    print(f"{inches} inches = {cm:.2f}")