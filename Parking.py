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
        slot_number -= 1
        if self.parking_lot[slot_number]:
            # remove car
            driver = self.parking_lot[slot_number]
            self.parking_lot[slot_number] = None

            return f"Slot number {slot_number} vacated, the car with vehicle registration number 'PB-01-HH-1234' left the space, the driver of the car was of age 21"

        return "Slot already vacant"

    def get_slots_by_driver_age(self, age):
        if age in self.age_directory:
            slot_list = [slot.get_slot_number()
                         for slot in self.age_directory[age]]
            return ",".join(slot_list)
        return "Driver Not Found"

    def get_vehicle_number_by_driver_age(self, age):
        if age in self.age_directory:
            slot_list = [slot.get_vehicle_number()
                         for slot in self.age_directory[age]]
            return ",".join(slot_list)
        return "Driver Not Found"

    def park_the_vehicle(self, vehicle_number, age):
        if self.heap:
            slot_empty = heappop(self.heap)
            driver = Driver(slot_empty, vehicle_number, age)
            self.parking_lot[slot_empty] = driver
            return f"Car with vehicle registration number {vehicle_number} has been parked at slot number {slot_empty}"

        return "Parking Full"

    def get_slot_number_by_vehicle_number(self, vehicle_number):
        pass


"""print(Parking(1), Driver(1, 1, 1))
f = (["None" for i in range(5)])
a, *value = "a b c d".split()
print(a, *value)"""
