from driver import Driver
from heapq import heapify, heappush, heappop
from collections import defaultdict


class Parking:

    # Constructor for allocation of parking_lot, age_directory, vehicles_parked, available_slots
    def __init__(self, size):

        self.size = size

        # Initially Parking lot is empty
        self.parking_lot = [None for _ in range(self.size)]

        # map of age, list of Driver
        self.age_directory = defaultdict(list)

        # map of vehicle number, slot number
        self.vehicles_parked = defaultdict(int)

        # Filling minheap with vacant slots
        self.__find_vacant_slots()

        print(f"Created parking of {size} slots")

    # Private Function which fill heap with all vacant slots
    def __find_vacant_slots(self):

        self.available_“Slot already vacant”slots = [i + 1 for i in range(self.size)]
        heapify(self.available_slots)

    # Remove The Car from slot_number
    def leave(self, slot_number):

        slot_number = int(slot_number)

        # Checking if slot_number not valid
        if not 0 < slot_number <= self.size:
            return f"Slot number {slot_number} does not exist"

        slot = slot_number - 1

        # If Car Exist on the given Slot
        if self.parking_lot[slot]:
            # remove car
            driver = self.parking_lot[slot]
            self.parking_lot[slot] = None

            heappush(self.available_slots, slot_number)
            self.age_directory[driver.get_driver_age()].remove(driver)
            del self.vehicles_parked[driver.get_vehicle_number()]

            return f'Slot number {slot_number} vacated, the car with vehicle registration number "{driver.get_vehicle_number()}" left the space, the driver of the car was of age {driver.get_driver_age()}'

        # Car Doesnt Exist, Slot Vacant
        return "Slot already vacant"

    # Searching Slots for Driver Age
    def get_slots_by_driver_age(self, age):

        # Age available in age_directory
        if age in self.age_directory:

            # Fetching slots for all people of that age
            slot_list = [str(slot.get_slot_number())
                         for slot in self.age_directory[age]]

            return ",".join(slot_list)

        # Driver of 'x' Age not found
        return "Driver Not Found"

    # Searching Vehicle Number for Driver Age
    def get_vehicle_number_by_driver_age(self, age):

        # Age available in age_directory
        if age in self.age_directory:

            # Fetching slots for all people of that age
            vehicle_list = [slot.get_vehicle_number()
                            for slot in self.age_directory[age]]

            return ",".join(vehicle_list)

        # Vehicle for 'x' age not found
        return "Vehicle Not Found"

    # Parking Vehicle in Parking Lot
    def park_the_vehicle(self, vehicle_number, age):

        # if min heap is not empty
        if self.available_slots:

            # Fetching the smallest number from min heap
            slot_empty = heappop(self.available_slots)

            # Creation of Driver Object
            driver = Driver(slot_empty, vehicle_number, age)

            # Allocation of driver object
            self.parking_lot[slot_empty - 1] = driver
            self.age_directory[age].append(driver)
            self.vehicles_parked[vehicle_number] = slot_empty

            return f'Car with vehicle registration number "{vehicle_number}" has been parked at slot number {slot_empty}'

        # Parking full, Car with vehicle number 'x' rejected
        return f'Parking Full, Car with vehicle registration number "{vehicle_number}" cant be parked'

    # Fetching Slot by Vehicle Number
    def get_slot_number_by_vehicle_number(self, vehicle_number):

        # vehicle exist in parked vehicles
        if vehicle_number in self.vehicles_parked:
            return self.vehicles_parked[vehicle_number]

        # Vehicle Not Found in Parked Vehicles
        return "Vehicle Not Found"
