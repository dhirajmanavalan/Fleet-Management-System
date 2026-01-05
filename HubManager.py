from EcoRideMain import ElectricCar
from EcoRideMain import ElectricScooter

Fleet_hubs = {}

def add_hub():
    hub_name = input("Enter hub Name:\n ")
    
    if hub_name not in Fleet_hubs:
        Fleet_hubs[hub_name] = []
        print("hub added successfully..")
        
    else:
        print("Already hub is there so create new hub..")
        
def add_vehicles_hub():
    hub_name = input("Enter hub Name:\n ")
    
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
        Fleet_hubs[hub_name].append(electric_car)
        print("electric car is added")
        
    elif choice == 2:
        speed = int(input("Enter Max Speed Limit: "))
        electric_scooter = ElectricScooter(vehicle_id, model, battery, speed)
        Fleet_hubs[hub_name].append(electric_scooter)
        print("electric scooter is added")
        
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

def main():
    while True:
        print("\nEco-Ride Fleet Management")
        print("1. Add Hub")
        print("2. Add Vehicle to Hub")
        print("3. View All Hubs")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            add_hub()

        elif choice == 2:
            add_vehicles_hub()

        elif choice == 3:
            show_all_hubs()

        elif choice == 4:
            print("Exit...")
            break

        else:
            print("Invalid option, try again")


if __name__ == "__main__":
    main()