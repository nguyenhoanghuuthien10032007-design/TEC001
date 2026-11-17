import random

def estimate_pi():
    try:
        total_points = int(input("Enter the number of random points to generate: "))
    except ValueError:
        print("Please enter a valid integer.")
        return

    if total_points <= 0:
        print("Number of points must be greater than 0.")
        return

    points_inside_circle = 0

    for _ in range(total_points):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        if x**2 + y**2 < 1:
            points_inside_circle += 1

    approx_pi = 4 * points_inside_circle / total_points

    print(f"Total points generated (N): {total_points}")
    print(f"Points inside circle (n): {points_inside_circle}")
    print(f"Approximate value of pi: {approx_pi}")

if __name__ == "__main__":
    estimate_pi()