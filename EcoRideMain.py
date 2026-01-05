class Vehicle:
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
    def battery_percentage(self,battery_percentage):
        if 0 < battery_percentage <= 100:
            self.__battery_percentage=battery_percentage
        else:
            print(f"Battery percentage must be 0 and 100 {battery_percentage}")
        
    @property
    def maintenance_status(self):
        return self.__maintenance_status
    
    @maintenance_status.setter
    def maintenance_status(self,maintenance_status):
        self.__maintenance_status=maintenance_status
    
    @property    
    def rental_price(self):
        return self.__rental_price
    
    @rental_price.setter
    def rental_price(self,rental_price):
        if rental_price > 0:
            self.__rental_price=rental_price
        else:
            print(f"Rental price should be not negative {rental_price}")
            
    def display(self):
        print(self.vehicle_id)
        print(self.model)
        print(self.battery_percentage)
        print(self.maintenance_status)
        print(self.rental_price)
        
class ElectricCar(Vehicle):
    def __init__(self, vehicle_id, model, battery_percentage,seating_capacity):
        super().__init__(vehicle_id, model, battery_percentage)
        self.seating_capacity = seating_capacity
    
    @property  
    def seating_capacity(self):
        return self.__seating_capacity
    
    @seating_capacity.setter
    def seating_capacity(self, seating_capacity):
        if seating_capacity>0:
            self.__seating_capacity = seating_capacity
        else:
            print("Seating capacity not less than 1")

class ElectricScooter(Vehicle):
    def __init__(self, vehicle_id, model, battery_percentage,max_speed_limit):
        super().__init__(vehicle_id, model, battery_percentage)
        self.max_speed_limit = max_speed_limit
    
    @property  
    def max_speed_limit(self):
        return self.__max_speed_limit
    
    @max_speed_limit.setter
    def max_speed_limit(self,max_speed_limit):
        if max_speed_limit > 10:
            self.__max_speed_limit = max_speed_limit
        else:
            print(f"Max speed limit should 10km {max_speed_limit}")
            
def display(self):
    print(self.vehicle_id)
    print(self.model)
    print(self.battery_percentage)
    print(self.maintenance_status)
    print(self.rental_price)
    print(self.seating_capacity)

# v = Vehicle("Dhi01","Tesla", 93)
# v.rental_price = 500
# v.maintenance_status = "Good to goo"

e = ElectricCar("1","teslaaa", 90, 2)
e.rental_price = 500
e.maintenance_status = "Good to goo"
e.display()
        