from ParkingLotSystem.ParkingFloor import ParkingFloors
from ParkingLotSystem.Vehicle import Vehicle
from ParkingLotSystem.VehicleType import VehicleType


class ParkingLot:

    def __init__(self, parking_lot_id, no_of_floors, no_of_slots_per_floor):
        self.id = parking_lot_id
        self.floors = int(no_of_floors)
        self.slots = int(no_of_slots_per_floor)
        self.parkingLot = ParkingFloors(self.floors, self.slots)

    # def freeSlots(self):
    #     for floor in range(0, self.floors):
    #         slots = []
    #         if (floor not in self.parkingLot.floors):
    #             print("Error: Floor doest not exist in system")
    #             return
    #         for slot in range(0, self.slots):
    #             ## supported vehicle type and slot unfilled
    #             if (self.parkingLot.floors[floor][slot].supportType == vehicleType and not
    #             self.parkingLot.floors[floor][slot].filled):
    #                 slots.append(slot)
    #         print("Free slots for " + vehicleType + " on Floor " + str(floor) + ": ", end="")
    #         for i in range(0, len(slots) - 1):
    #             print(slots[i], end=",")
    #         print(slots[-1])

    def display(self, displayType, vehicleType: VehicleType):

        for floor in range(0, self.floors):
            count = 0
            freeSlots = []
            occupiedSlots = []

            if (floor not in self.parkingLot.floors):
                print("Error: Floor doest not exist in system")
                return

            for slot in range(0, self.slots):
                if (self.parkingLot.floors[floor][slot].supportType == vehicleType and not
                self.parkingLot.floors[floor][slot].filled):
                    count += 1
                    freeSlots.append(slot)
                elif (self.parkingLot.floors[floor][slot].supportType == vehicleType and self.parkingLot.floors[floor][
                    slot].filled):
                    occupiedSlots.append(slot)

            if (displayType == "free_count"):
                print("No. of free slots for " + vehicleType + " on Floor " + str(floor + 1) + ": " + str(count))
            elif (displayType == "free_slots"):
                print("Free slots for " + vehicleType + " on Floor " + str(floor + 1) + ": ", end="")
                for i in range(0, len(freeSlots) - 1):
                    print(freeSlots[i] + 1, end=",")
                if (len(freeSlots) - 1 >= 0):
                    print(freeSlots[len(freeSlots) - 1] + 1)
                else:
                    print("")
            elif (displayType == "occupied_slots"):
                print("Occupied slots for " + vehicleType + " on Floor " + str(floor + 1) + ": ", end="")
                for i in range(0, len(occupiedSlots) - 1):
                    print(occupiedSlots[i] + 1, end=",")
                if (len(occupiedSlots) - 1 >= 0):
                    print(occupiedSlots[len(occupiedSlots) - 1] + 1)
                else:
                    print("")
            else:
                print("Unsupported DisplayType")

    def Park(self, vehicleType, vehicleRegNo, vehicleColor):
        if (vehicleType == "CAR"):
            for floor in range(0, self.floors):
                for slot in range(3, self.slots):
                    if (floor in self.parkingLot.floors and not self.parkingLot.floors[floor][slot].filled):
                        print("Parked vehicle. Ticket ID: " + self.id + "_" + str(floor + 1) + "_" + str(slot + 1))
                        self.parkingLot.floors[floor][slot].fillVehicle(self.id + "_" + str(floor) + "_" + str(slot),
                                                                        vehicleType, vehicleRegNo, vehicleColor)
                        return
            print("Parking Lot Full")
        elif (vehicleType == "BIKE"):
            for floor in (0, self.floors):
                maxSlot = max(self.parkingLot.floors[floor].keys())
                for slot in (1, min(3, maxSlot)):
                    if (floor in self.parkingLot.floors and slot in self.parkingLot.floors[floor] and not
                    self.parkingLot.floors[floor][slot].filled):
                        print("Parked vehicle. Ticket ID: " + self.id + "_" + str(floor + 1) + "_" + str(slot + 1))
                        self.parkingLot.floors[floor][slot].fillVehicle(self.id + "_" + str(floor) + "_" + str(slot),
                                                                        vehicleType, vehicleRegNo, vehicleColor)
                        return
            print("Parking Lot Full")
        elif (vehicleType == "TRUCK"):
            for floor in (0, self.floors):
                if (floor in self.parkingLot.floors and 0 in self.parkingLot.floors[floor] and not
                self.parkingLot.floors[floor][0].filled):
                    print("Parked vehicle. Ticket ID: " + self.id + "_" + str(floor + 1) + "_" + str(1))
                    self.parkingLot.floors[floor][0].fillVehicle(self.id + "_" + str(floor) + "_" + str(0), vehicleType,
                                                                 vehicleRegNo, vehicleColor)
                    return
            print("Parking Lot Full")
        else:
            print("Unsupported Vehicle Type")

    def unPark(self, ticketId):
        parkingLotId, floor, slot = list(map(str, ticketId.split("_")))
        floor = int(floor) - 1
        slot = int(slot) - 1
        if (self.id != parkingLotId):
            print("Incorrect Parking Lot")
            return
        if (floor not in self.parkingLot.floors or slot not in self.parkingLot.floors[floor]):
            print("Invalid Ticket")
            return
        else:
            if (self.parkingLot.floors[floor][slot].filled):
                print("Unparked vehicle with Registration Number: " + str(
                    self.parkingLot.floors[floor][slot].vehicle.reg_number) + " and Color: " + str(
                    self.parkingLot.floors[floor][slot].vehicle.color))
                self.parkingLot.floors[floor][slot].filled = False
                self.parkingLot.floors[floor][slot].ticketId = None
                self.parkingLot.floors[floor][slot].vehicle = None
            else:
                print("Invalid Ticket")
                return

    ## no need
    def printParkingLot(self):
        print(self.parkingLot.floors)
