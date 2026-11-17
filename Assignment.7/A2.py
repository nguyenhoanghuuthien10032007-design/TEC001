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
if __name__ == "__main__":
    car = Car(registration_number="ABC-123", maximum_speed=142)
    
    car.accelerate(30)
    car.accelerate(70)
    car.accelerate(50)
    print(f"Current speed: {car.current_speed} km/h")
    
    car.accelerate(-200)
    print(f"Final speed: {car.current_speed} km/h")