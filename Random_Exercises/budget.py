""" Assignment: Create budgets for flight, car, hotel, and base, which should be inherited by the others.
 Base should have a method called generate that takes no parameters and returns a budget.
 First Step: Flight should return 500, Hotel should return 400, Car should return 300
 Second Step: Flight constructor gets number_of_legs and returns 500 * numer_of_legs
              Hotel constructor gets number_of_nights and returns 400 * number_of_nights
              Car constructor gets number_of_days and returns 300 * number_of_days """


class Budget:
    def generate(self):
        return self


class Flight(Budget):
    def __init__(self, number_of_legs):
        self.price_per_leg = 500
        self.number_of_legs = number_of_legs
        self.budget = self.price_per_leg * number_of_legs


class Hotel(Budget):
    def __init__(self, number_of_nights):
        self.price_per_night = 400
        self.number_of_nights = number_of_nights
        self.budget = self.price_per_night * number_of_nights


class Car(Budget):
    def __init__(self, number_of_days):
        self.price_per_day = 300
        self.number_of_days = number_of_days
        self.budget = self.price_per_day * number_of_days


if __name__ == '__main__':

    number_of_legs = int(input("How many legs is your flight? "))
    flight_budget = Flight(number_of_legs)
    print(f"Your flight budget is: {flight_budget.generate}\n")

    number_of_nights = int(input("How many nights are you staying? "))
    hotel_budget = Hotel(number_of_nights)
    print(f"Your hotel budget is: {hotel_budget.budget}\n")

    number_of_days = int(input("How many days are you renting the car for? "))
    car_budget = Car(number_of_days)
    print(f"Your car budget is: {car_budget.budget}\n")
