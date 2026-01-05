from EcoRideMain import ElectricCar
from EcoRideMain import ElectricScooter

def main():
    print("Welcome to Eco-Ride Urban Mobility System")
    print("---------------------------------------------")
    print("Please choose a vehicle type:")
    print("1. Electric Car")
    print("2. Electric Scooter")

    user_choice = int(input("Enter your choice (1 or 2): "))

    if user_choice == 1:
        print("\nYou selected Electric Car")

        vehicle_id = input("Enter Vehicle ID: ")
        model_name = input("Enter Car Model: ")
        battery_level = int(input("Enter Battery Percentage: "))
        seat_count = int(input("Enter Seating Capacity: "))
        price_per_km = int(input("Enter Rental Price: "))
        travel_distance = int(input("Enter Distance to Travel (km): "))

        car = ElectricCar(vehicle_id, model_name, battery_level, seat_count)
        car.rental_price = price_per_km
        car.maintenance_status = "Good to go"

        print("\n--- Vehicle Details ---")
        car.display()

        trip_cost = car.calculate_trip_cost(travel_distance)
        print("Total Trip Cost:", trip_cost)

    elif user_choice == 2:
        print("\nYou selected Electric Scooter")

        vehicle_id = input("Enter Vehicle ID: ")
        model_name = input("Enter Scooter Model: ")
        battery_level = int(input("Enter Battery Percentage: "))
        max_speed = int(input("Enter Max Speed Limit: "))
        price_per_km = int(input("Enter Rental Price: "))
        travel_distance = int(input("Enter Distance to Travel (km): "))

        scooter = ElectricScooter(vehicle_id, model_name, battery_level, max_speed)
        scooter.rental_price = price_per_km
        scooter.maintenance_status = "OK"

        print("\n--- Vehicle Details ---")
        scooter.display()

        trip_cost = scooter.calculate_trip_cost(travel_distance)
        print("Total Trip Cost:", trip_cost)

    else:
        print("\nInvalid choice. Please restart and select 1 or 2.")


if __name__ == "__main__":
    main()
