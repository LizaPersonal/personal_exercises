
class Budget:
    def generate(self):
        return self


class Flight(Budget):
    def __init__(self, number_of_legs):
        self.generate = 500 * number_of_legs


class Hotel(Budget):
    def __init__(self, number_of_nights):
        self.generate = 400 * number_of_nights


class Car(Budget):
    def __init__(self, number_of_days):
        self.generate = 300 * number_of_days


if __name__ == '__main__':

    number_of_legs = int(input("How many legs is your flight? "))
    flight_budget = Flight(number_of_legs)
    print(f"Your flight budget is: {flight_budget.generate}\n")

    number_of_nights = int(input("How many nights are you staying? "))
    hotel_budget = Hotel(number_of_nights)
    print(f"Your hotel budget is: {hotel_budget.generate}\n")

    number_of_days = int(input("How many days are you renting the car for? "))
    car_budget = Car(number_of_days)
    print(f"Your car budget is: {car_budget.generate}\n")
