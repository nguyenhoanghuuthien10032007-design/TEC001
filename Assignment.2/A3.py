def check_hemoglobin():
    sex = input("Enter the hemoglobin sex (female/male): ")
    value = float(input("enter the hemoglobin value (g/l): "))

    if sex == "female":
        if value < 117:
            print("Hemoglobin status: Low")
        elif value <= 155:
            print("Hemoglobin status: Normal")
        else:
            print("Hemoglobin status: High")

    if sex == "male":
        if value < 134:
            print("Hemoglobin status: Low")
        elif value <= 167:
            print("Hemoglobin status: Normal")
        else:
            print("Hemoglobin status: High")

check_hemoglobin()


                