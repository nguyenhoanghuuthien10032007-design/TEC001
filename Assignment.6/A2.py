seasons = ('spring', 'summer', 'autumn', 'winter')
month = int(input("Enter number of month (1-12): "))
if 1 <= month <= 12:
    if month in (12, 1, 2):
        season = seasons[3]
    elif 3 <= month <= 5:
        season = seasons[0]
    elif 6 <= month <= 8:
        season = seasons[1]
    else:
        season = seasons[2]
    print(f"Month {month} belongs to the season: {season}")
else:
    print("Invalid month! Please enter a number between 1-12")
