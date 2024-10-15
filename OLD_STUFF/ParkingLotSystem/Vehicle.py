from ParkingLotSystem.VehicleType import VehicleType

class Vehicle:
    def __init__(self,vehicleType:VehicleType,reg_number:str,color:str):
        self.type = vehicleType
        self.reg_number = reg_number
        self.color = color
        self.id = str(vehicleType) + "_" + reg_number + "_" + color