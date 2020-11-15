class Driver:
    # Constructor of Driver Class
    def __init__(self, slot_number, vehicle_number, age):
        self.slot_number = slot_number
        self.vehicle_number = vehicle_number
        self.age = age

    # Fetchs slot number
    def get_slot_number(self):
        return self.slot_number

    # Fetchs vehicle number
    def get_vehicle_number(self):
        return self.vehicle_number

    # Fetchs driver age
    def get_driver_age(self):
        return self.age
