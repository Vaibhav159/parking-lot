from parking import Parking
import re


class allocation:

    def __init__(self):
        self.parking_lot = None

    def check_driver_details(self, value):
        regex_for_number_plate = "[A-Z]{2}-[\d]{2}-[A-Z]{2}-[\d]{4}"
        state = re.search(regex_for_number_plate, value[0])
        if state and value[1] == "driver_age" and int(value[2]) > 1:
            return True

        return False

    def start(self):
        while True:
            try:
                operation, *value = input().split()

                if operation == "Create_parking_lot":
                    self.parking_lot = Parking(int(value[0]))
                elif operation == "Park":
                    if not self.check_driver_details(value):
                        print("Incorrect Values")
                        continue
                    print(self.parking_lot.park_the_vehicle(
                        value[0], value[2]))
                elif operation == "Slot_numbers_for_driver_of_age":
                    print(self.parking_lot.get_slots_by_driver_age(value[0]))
                elif operation == "Slot_number_for_car_with_number":
                    print(
                        self.parking_lot.get_slot_number_by_vehicle_number(value[0]))
                elif operation == "Leave":
                    print(self.parking_lot.leave(value[0]))
                elif operation == "Vehicle_registration_number_for_driver_of_age":
                    print(
                        self.parking_lot.get_vehicle_number_by_driver_age(value[0]))
                else:
                    print("Invalid operation")
                    break

            except EOFError:
                break


aa = allocation()
aa.start()
