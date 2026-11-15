class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def start(self):
        print("The car is starting.")


# Create an object
car1 = Car("Toyota", "Black")

# Call the method
car1.start()