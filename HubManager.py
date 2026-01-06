from EcoRideMain import ElectricCar
from EcoRideMain import ElectricScooter

Fleet_hubs = {}

def add_hub():
    hub_name = input("Enter hub Name:\n ")
    hub_name = hub_name.strip().title()
    
    if hub_name not in Fleet_hubs:
        Fleet_hubs[hub_name] = []
        print("hub added successfully..")
        
    else:
        print("Already hub is there so create new hub..")
        
def add_vehicles_hub():
    hub_name = input("Enter hub Name:\n ")
    hub_name = hub_name.strip().title()
    
    if hub_name not in Fleet_hubs:
        print("hub name does not exist")
        return
        
    print("1.Electric Car")
    print("2.Electric Scooter")
    
    choice = int(input("Enter your Vehicle:\n"))
    
    if choice == 1:
        print("Your Electric Car-->")
    elif choice ==2:
        print("Your Electric Scooter-->")
    
    vehicle_id = int(input("Enter vehicle id: "))
    model = input("Enter Model: ")
    battery = int(input("Enter Battery Percentage: "))
    
    if choice == 1:
        seats = int(input("Enter Seating Capacity: "))
        electric_car = ElectricCar(vehicle_id, model, battery, seats)
        rental_price = int(input("Enter Rental Price: "))
        electric_car.rental_price = rental_price
        electric_car.maintenance_status = "OK"
        
        duplicate_found = False

        for v in Fleet_hubs[hub_name]:
            if v == electric_car:
                duplicate_found = True
                break
            
        if duplicate_found:
            print("Duplicate Vehicle ID...Vehicle already exists in this hub..")
            return
        
        Fleet_hubs[hub_name].append(electric_car)
        print("Electric car is added")

        
        
        
    elif choice == 2:
        speed = int(input("Enter Max Speed Limit: "))
        electric_scooter = ElectricScooter(vehicle_id, model, battery, speed)
        
        rental_price = int(input("Enter Rental Price: "))
        electric_scooter.rental_price = rental_price
        electric_scooter.maintenance_status = "OK"

        duplicate_found = False

        for v in Fleet_hubs[hub_name]:
            if v == electric_scooter:
                duplicate_found = True
                break

        if duplicate_found:
            print("Duplicate Vehicle ID..Vehicle already exists in this hub..")
            return

        Fleet_hubs[hub_name].append(electric_scooter)
        print("Electric scooter is added")

        
    else:
        print("Invalid_choice")
        return
    
def show_all_hubs():
    if not Fleet_hubs:
        print("No hubs available")
        return

    for hub_name in Fleet_hubs:
        print("Hub:", hub_name)

        for vehicle in Fleet_hubs[hub_name]:
            vehicle.display()
            
def search_by_hub():
    hub_name = input("Enter hub name to search: ")
    hub_name = hub_name.strip().title()

    if hub_name not in Fleet_hubs:
        print("Hub not found")
        return

    print(f"\nVehicles in hub: {hub_name}")

    if not Fleet_hubs[hub_name]:
        print("No vehicles in this hub")
        return

    for vehicle in Fleet_hubs[hub_name]:
        vehicle.display()

def search_by_battery():
    all_vehicles=[]
    for hub in Fleet_hubs:
        for vehicle in Fleet_hubs[hub]:
            all_vehicles.append(vehicle)
            
    high_battery_vehicles = list(filter(lambda v : v.battery_percentage > 80, all_vehicles))
    
    if not high_battery_vehicles:
        print("No vehicles found with battery > 80%")
        return

    for vehicle in high_battery_vehicles:
        vehicle.display()

def view_by_vehicle_type():
    catergorized = {"Electric Car": [], "Electric Scooter": []}

    for hub in Fleet_hubs:
        for vehicle in Fleet_hubs[hub]:
            if isinstance(vehicle, ElectricCar):
                catergorized["Electric Car"].append(vehicle)
            elif isinstance(vehicle, ElectricScooter):
                catergorized["Electric Scooter"].append(vehicle)

    print("Electric Cars...")
    if not catergorized["Electric Car"]:
        print("No Electric Cars available")
    else:
        for car in catergorized["Electric Car"]:
            car.display()

    print("Electric Scooters...")
    if not catergorized["Electric Scooter"]:
        print("No Electric Scooters are available")
    else:
        for scooter in catergorized["Electric Scooter"]:
            scooter.display()


def main():
    while True:
        print("\nEco-Ride Fleet Management")
        print("1. Add Hub")
        print("2. Add Vehicle to Hub")
        print("3. View All Hubs")
        print("4. Search Vehicles by Hub")
        print("5. Search Vehicles with Battery > 80%")
        print("6. View Vehicles by Type")
        print("7. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            add_hub()

        elif choice == 2:
            add_vehicles_hub()

        elif choice == 3:
            show_all_hubs()

        elif choice == 4:
            search_by_hub()

        elif choice == 5:
            search_by_battery()
        
        elif choice == 6:
            view_by_vehicle_type()

        elif choice == 7:
            print("Exit...")
            break

        else:
            print("Invalid option, try again")


if __name__ == "__main__":
    main()