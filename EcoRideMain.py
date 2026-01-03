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

v = Vehicle("Dhi01","Tesla", 93)
v.rental_price = 500
v.maintenance_status = "Good to goo"

v.display()
        