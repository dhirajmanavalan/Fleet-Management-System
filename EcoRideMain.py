from abc import ABC,abstractmethod

class Vehicle(ABC):
    def __init__(self, vehicle_id, model, battery_percentage):
        self.vehicle_id = vehicle_id
        self.model = model
        self.__battery_percentage = battery_percentage
        self.__maintenance_status = "OK"
        self.__rental_price = 0

    @property
    def battery_percentage(self):
        return self.__battery_percentage

    @battery_percentage.setter
    def battery_percentage(self, battery_percentage):
        if 0 < battery_percentage <= 100:
            self.__battery_percentage = battery_percentage
        else:
            print(f"Battery percentage must be 0 and 100 {battery_percentage}")

    @property
    def maintenance_status(self):
        return self.__maintenance_status

    @maintenance_status.setter
    def maintenance_status(self, maintenance_status):
        self.__maintenance_status = maintenance_status

    @property
    def rental_price(self):
        return self.__rental_price

    @rental_price.setter
    def rental_price(self, rental_price):
        if rental_price > 0:
            self.__rental_price = rental_price
        else:
            print(f"Rental price should be not negative {rental_price}")
     
    @abstractmethod       
    def calculate_trip_cost(self):
        pass

    def display(self):
        print("Vehicle_id: ", self.vehicle_id)
        print("Model: ", self.model)
        print("Battery_Percentage: ", self.battery_percentage)
        print("Maintenance_Status: ", self.maintenance_status)
        print("Rental_Price: ", self.rental_price)


class ElectricCar(Vehicle):
    def __init__(self, vehicle_id, model, battery_percentage, seating_capacity):
        super().__init__(vehicle_id, model, battery_percentage)
        self.__seating_capacity = seating_capacity

    @property
    def seating_capacity(self):
        return self.__seating_capacity

    @seating_capacity.setter
    def seating_capacity(self, seating_capacity):
        if seating_capacity > 0:
            self.__seating_capacity = seating_capacity
        else:
            print("Seating capacity not less than 1")
            
    def calculate_trip_cost(self):
        return super().calculate_trip_cost()

    def display(self):
        super().display()
        print("Seating_Capacity: ", self.seating_capacity)


class ElectricScooter(Vehicle):
    def __init__(self, vehicle_id, model, battery_percentage, max_speed_limit):
        super().__init__(vehicle_id, model, battery_percentage)
        self.__max_speed_limit = max_speed_limit

    @property
    def max_speed_limit(self):
        return self.__max_speed_limit

    @max_speed_limit.setter
    def max_speed_limit(self, max_speed_limit):
        if max_speed_limit > 10:
            self.__max_speed_limit = max_speed_limit
        else:
            print(f"Max speed limit should 10km {max_speed_limit}")
            
    def calculate_trip_cost(self):
        return super().calculate_trip_cost()

    def display(self):
        super().display()
        print("Max Speed Limit:", self.max_speed_limit)


def main():
    print("Vehicle")
    vehicle = Vehicle("V1", "Suzuki", 94)
    vehicle.rental_price = 150
    vehicle.maintenance_status = "Average"
    vehicle.display()
    
    print("\n --")
    print("ElectricCar")
    car = ElectricCar("C1", "Tesla", 90, 5)
    car.rental_price = 500
    car.maintenance_status = "Good to go"
    car.display()

    print("\n --")
    print("ElectricScooter")
    scooter = ElectricScooter("S1", "Ola", 80, 25)
    scooter.rental_price = 300
    scooter.maintenance_status = "OK"
    scooter.display()


if __name__ == "__main__":
    main()
