def check_zander():
    length = float(input("Enter the length of the zander (cm): "))
    limit = 42
    
    if length < limit:
        difference = limit - length
        print("The fish does not meet the size limit. Please release it back into the lake!")
        print(f"The fish is {difference:.1f} cm below the size limit.")
    else:
        print("The zander meets the size limit!")
        
check_zander()