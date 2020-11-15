class Driver:
    def __init__(self, slot_number, vehicle_number, age):
        self.slot_number = slot_number
        self.vehicle_number = vehicle_number
        self.age = age

    def get_slot_number(self):
        return self.slot_number

    def get_vehicle_number(self):
        return self.vehicle_number

    def get_driver_age(self):
        return self.age
