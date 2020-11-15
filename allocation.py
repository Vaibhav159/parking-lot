from parking import Parking
import re


class allocation:

    def __init__(self):
        # Parking lot is not yet created
        self.parking_lot = None

    # Checking The Number plate of vehicle
    def check_driver_details(self, value):
        regex_for_number_plate = "[A-Z]{2}-[\d]{2}-[A-Z]{2}-[\d]{4}"
        state = re.search(regex_for_number_plate, value[0])
        if state and value[1] == "driver_age":
            return True

        return False

    # Runner Class
    def start(self):
        # True until EOF
        while True:
            try:
                # Operation stores command, and value stores tuple of remaining values
                operation, *value = input().split()

                # Creating a object of Parking of size 'n'
                if operation == "Create_parking_lot":
                    self.parking_lot = Parking(int(value[0]))

                # Parks the car in Parking
                elif operation == "Park":
                    if not self.check_driver_details(value):
                        print("Incorrect Values")
                        continue

                    print(self.parking_lot.park_the_vehicle(
                        value[0], value[2]))

                # Search for Slot numbers by driver age
                elif operation == "Slot_numbers_for_driver_of_age":
                    print(self.parking_lot.get_slots_by_driver_age(value[0]))

                # Search for Slot numbers by car number
                elif operation == "Slot_number_for_car_with_number":
                    print(
                        self.parking_lot.get_slot_number_by_vehicle_number(value[0]))

                # Removes Car From Parking
                elif operation == "Leave":
                    print(self.parking_lot.leave(value[0]))

                # Search for Vehicle Number by driver age
                elif operation == "Vehicle_registration_number_for_driver_of_age":
                    print(
                        self.parking_lot.get_vehicle_number_by_driver_age(value[0]))

                # Breaks code for any other output
                else:
                    print("Invalid operation")
                    break

            # Terminated While on EOF
            except EOFError:
                break


if __name__ == '__main__':
    system = allocation()
    system.start()
