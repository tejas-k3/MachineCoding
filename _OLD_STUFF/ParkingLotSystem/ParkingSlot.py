from ParkingLotSystem.Vehicle import Vehicle
from ParkingLotSystem.VehicleType import VehicleType


class ParkingSlot:
    def __init__(self, floor: int, slotNumber: int):
        self.floor = floor  # 1 to n
        self.slotNumber = slotNumber  # 1 to n
        self.filled = False  # True or False represent filled or not
        self.ticketId = None  # on True add ticketId
        self.vehicle = None
        if (slotNumber == 0):
            self.supportType = VehicleType.TRUCK
        elif (slotNumber <= 2):
            self.supportType = VehicleType.BIKE
        else:
            self.supportType = VehicleType.CAR

    def fillVehicle(self, ticketId: str, vehicleType: VehicleType, vehicleRegNo: str, vehicleColor: str):
        self.filled = True
        self.ticketId = ticketId
        self.vehicle = Vehicle(vehicleType, vehicleRegNo, vehicleColor)
