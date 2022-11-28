class Driver():
    def __init__(self):
        self.parkingLots = {}
        self.lastParkingSlot = None
        self.instantiate()

    def instantiate(self):
        print("Input Log:")
        rawInput = []
        while(True):
            tempInput = list(map(str,input().strip().split()))
            if(tempInput[0] == "exit"):
                break
            rawInput.append(tempInput)
        print(rawInput)
        for userInput in rawInput:
            if(userInput[0] == "create_parking_lot"):
                newParkingLotId = userInput[1]
                floors = userInput[2]
                slots = userInput[3]
                if(newParkingLotId in self.parkingLots):
                    print("Parking lot already exists")
                    return
                else:
                    print("Created parking lot with " + str(floors) + " floors and " + str(slots) + " slots per floor")
                    self.parkingLots[newParkingLotId] = parkingLot(newParkingLotId,floors,slots)
                    self.lastParkingSlot = newParkingLotId
            elif(userInput[0] == "display"):
                self.parkingLots[self.lastParkingSlot].display(userInput[1],userInput[2])
            elif(userInput[0] == "park_vehicle"):
                self.parkingLots[self.lastParkingSlot].Park(userInput[1],userInput[2],userInput[3])
            elif(userInput[0] == "unpark_vehicle"):
                self.parkingLots[self.lastParkingSlot].unPark(userInput[1])
            else:
                return

if __name__ == "__main__":
    Driver()
