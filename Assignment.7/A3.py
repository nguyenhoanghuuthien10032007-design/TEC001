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
    car = Car(registration_number="ABC-123", maximum_speed=142)
    car.travelled_distance = 2000
    car.current_speed = 60
    
    car.drive(1.5)
    print(f"Travelled distance: {car.travelled_distance} km") # Kết quả: 2090.0 km