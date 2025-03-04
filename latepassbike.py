class Bike:
    def __init__(self, brand, model, gear_count):
        self.brand = brand
        self.model = model
        self.gear_count = gear_count
        self.speed = 0  
        self.distance_travelled = 0  

    def ride(self, time, speed):

        self.speed = speed
        self.distance_travelled += speed * time
        print(f"Riding for {time} hours at {speed} km/h")

    def stop(self):
        self.speed = 0
        print("Bike stopped")

    def display_info(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Gears: {self.gear_count}")
        print(f"Current Speed: {self.speed} km/h")
        print(f"Total Distance Travelled: {self.distance_travelled} km")

my_bike = Bike(brand="Trek", model="X-Caliber", gear_count=18)

my_bike.display_info()

my_bike.ride(time=2, speed=20)

my_bike.display_info()

my_bike.stop()

my_bike.display_info()