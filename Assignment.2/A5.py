import math

def calculate_unit_price(diameter_cm, price_usd):
    # Convert diameter (cm) to radius (m)
    radius_m = (diameter_cm / 2) / 100
    # Calculate area in square meters
    area_m2 = math.pi * (radius_m ** 2)
    # Calculate unit price (USD / m2)
    unit_price = price_usd / area_m2
    return unit_price

def main():
    print("--- Pizza 1 Details ---")
    d1 = float(input("Enter diameter of pizza 1 (cm): "))
    p1 = float(input("Enter price of pizza 1 (USD): "))
    
    print("\n--- Pizza 2 Details ---")
    d2 = float(input("Enter diameter of pizza 2 (cm): "))
    p2 = float(input("Enter price of pizza 2 (USD): "))
    
    price_per_m2_1 = calculate_unit_price(d1, p1)
    price_per_m2_2 = calculate_unit_price(d2, p2)
    
    print(f"\nPizza 1 unit price: {price_per_m2_1:.2f} USD/m²")
    print(f"Pizza 2 unit price: {price_per_m2_2:.2f} USD/m²")
    
    if price_per_m2_1 < price_per_m2_2:
        print("\n=> Pizza 1 provides better value for money.")
    elif price_per_m2_2 < price_per_m2_1:
        print("\n=> Pizza 2 provides better value for money.")
    else:
        print("\n=> Both pizzas have the same unit price.")

main()