from Driver import Driver
from heapq import heapify, heappush, heappop
from collections import defaultdict


class Parking:
    def __init__(self, size):
        self.size = size
        self.parking_lot = [None for _ in range(self.size)]
        self.age_directory = defaultdict(list)
        self.make_heap()
        print(f"Created parking of {size} slots")

    def make_heap(self):
        self.heap = [i+1 for i in range(self.size)]
        heapify(self.heap)

    def leave(self, slot_number):
        slot = int(slot_number) - 1
        if self.parking_lot[slot]:
            # remove car
            driver = self.parking_lot[slot]
            self.parking_lot[slot] = None
            heappush(self.heap, int(slot_number))
            self.age_directory[driver.get_driver_age()].remove(driver)
            return f'Slot number {slot_number} vacated, the car with vehicle registration number "{driver.get_vehicle_number()}" left the space, the driver of the car was of age {driver.get_driver_age()}'

        return "Slot already vacant"

    def get_slots_by_driver_age(self, age):
        if age in self.age_directory:
            slot_list = [str(slot.get_slot_number())
                         for slot in self.age_directory[age]]
            return ",".join(slot_list)
        return "Driver Not Found"

    def get_vehicle_number_by_driver_age(self, age):
        if age in self.age_directory:
            slot_list = [slot.get_vehicle_number()
                         for slot in self.age_directory[age]]
            return ",".join(slot_list)
        return "Vehicle Not Found"

    def park_the_vehicle(self, vehicle_number, age):
        if self.heap:
            slot_empty = heappop(self.heap)
            driver = Driver(slot_empty, vehicle_number, age)
            self.parking_lot[slot_empty - 1] = driver
            self.age_directory[age].append(driver)
            return f'Car with vehicle registration number "{vehicle_number}" has been parked at slot number {slot_empty}'

        return "Parking Full"

    def get_slot_number_by_vehicle_number(self, vehicle_number):
        for slot, driver in enumerate(self.parking_lot):
            if driver and driver.get_vehicle_number() == vehicle_number:
                return slot + 1

        return "Vehicle Not Found"


"""print(Parking(1), Driver(1, 1, 1))
f = (["None" for i in range(5)])
a, *value = "a b c d".split()
print(a, *value)"""
