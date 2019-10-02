from car import Car

if __name__== "__main__":
    print("Hola Fer")
    car = Car()
    car.license = "AMS234"
    car.driver = "Andres Herrera"
    print(vars(car))

    car2 = Car()
    car2.license = "ABC123"
    car2.driver = "Andrea Herrera"
    print(vars(car2))

