from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, vehicle_id, model, battery_percentage):
        self.vehicle_id = vehicle_id
        self.model = model
        self.battery_percentage = battery_percentage
        self.__maintenance_status = "OK"
        self.__rental_price = 0

    @property
    def battery_percentage(self):
        return self.__battery_percentage

    @battery_percentage.setter
    def battery_percentage(self, value):
        if 0 <= value <= 100:
            self.__battery_percentage = value
        else:
            raise ValueError("Battery percentage must be between 0 and 100")

    @property
    def maintenance_status(self):
        return self.__maintenance_status

    @maintenance_status.setter
    def maintenance_status(self, value):
        self.__maintenance_status = value

    @property
    def rental_price(self):
        return self.__rental_price

    @rental_price.setter
    def rental_price(self, value):
        if value >= 0:
            self.__rental_price = value
        else:
            raise ValueError("Rental price cannot be negative")

    @abstractmethod
    def calculate_trip_cost(self, value):
        pass

    def process_rental(self, value):
        cost = self.calculate_trip_cost(value)
        print("Trip Cost:", cost)

    def display(self):
        print("Vehicle ID:", self.vehicle_id)
        print("Model:", self.model)
        print("Battery %:", self.battery_percentage)
        print("Maintenance Status:", self.maintenance_status)
        print("Rental Price:", self.rental_price)

class ElectricCar(Vehicle):
    def __init__(self, vehicle_id, model, battery_percentage, seating_capacity):
        super().__init__(vehicle_id, model, battery_percentage)
        self.seating_capacity = seating_capacity

    @property
    def seating_capacity(self):
        return self.__seating_capacity

    @seating_capacity.setter
    def seating_capacity(self, value):
        if value > 0:
            self.__seating_capacity = value
        else:
            raise ValueError("Seating capacity must be greater than 0")

    def calculate_trip_cost(self, distance_km):
        return 5.00 + (0.50 * distance_km)

    def display(self):
        super().display()
        print("Seating Capacity:", self.seating_capacity)


class ElectricScooter(Vehicle):
    def __init__(self, vehicle_id, model, battery_percentage, max_speed_limit):
        super().__init__(vehicle_id, model, battery_percentage)
        self.max_speed_limit = max_speed_limit

    @property
    def max_speed_limit(self):
        return self.__max_speed_limit

    @max_speed_limit.setter
    def max_speed_limit(self, value):
        if value > 10:
            self.__max_speed_limit = value
        else:
            raise ValueError("Max speed must be greater than 10 km/h")

    def calculate_trip_cost(self, minutes):
        return 1.00 + (0.15 * minutes)

    def display(self):
        super().display()
        print("Max Speed Limit:", self.max_speed_limit)
