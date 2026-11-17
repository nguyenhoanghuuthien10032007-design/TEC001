import random

class Car:
    def __init__(self, registration_number: str, maximum_speed: float):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0.0
        self.travelled_distance = 0.0

    def accelerate(self, change: float):
        self.current_speed += change
        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        if self.current_speed < 0:
            self.current_speed = 0

    def drive(self, hours: float):
        self.travelled_distance += self.current_speed * hours
if __name__ == "__main__":
    cars = []
    for i in range(1, 11):
        reg_num = f"ABC-{i}"
        max_speed = random.randint(150, 200)
        cars.append(Car(reg_num, max_speed))
    race_finished = False
    hours_passed = 0
    while not race_finished:
        hours_passed += 1
        for car in cars:
            speed_change = random.randint(-10, 15)
            car.accelerate(speed_change)
            car.drive(1)
            if car.travelled_distance >= 10000:
                race_finished = True
    print(f"\nCuộc đua kết thúc sau {hours_passed} giờ!\n")
    print(f"{'Registration':<15} | {'Max Speed (km/h)':<18} | {'Final Speed (km/h)':<20} | {'Distance (km)':<15}")
    print("-" * 78)
    for car in cars:
        print(f"{car.registration_number:<15} | {car.maximum_speed:<18} | {car.current_speed:<20} | {car.travelled_distance:<15.2f}")