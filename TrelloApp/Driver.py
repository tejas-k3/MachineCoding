from TrelloApp.Trello import Trello


def main(self, Card):
    fakeTrello = Trello()
    userInput = []
    while True:
        temp = list(map(str, input().strip().split()))
        # Exit case
        if(temp[0] == "exit"):
            break
        userInput.append(temp)
    for rawInput in userInput:
        # Cases
        if(rawInput[0] == "BOARD"):
            if(rawInput[1] == "CREATE"):
                fakeTrello.addBoard(rawInput[2])
                print("Board Added")
                continue
            elif(rawInput[1] == "DELETE"):
                fakeTrello.removeBoard(rawInput[2])
                print("Board DELETED")
                continue
            else:
                boardId = rawInput[1]
                if(not fakeTrello.validateBoard(boardId)):
                    print("No such board exists in system")
                    continue
                if(rawInput[2] == "ADD_MEMBER"):
                    userId = rawInput[3]
                    if(fakeTrello.validateUser(userId)):
                        fakeTrello.boards[boardId].addMember(userId)
                    else:
                        print("No such user exists for addtition")
                    continue
                elif(rawInput[2] == "REMOVE_MEMBER"):
                    userId = rawInput[3]
                    if(fakeTrello.validateUser(userId)):
                        fakeTrello.boards[boardId].removeMember(userId)
                    else:
                        print("No such user exists for removal")
                    continue
                elif(rawInput[2] == "name"):
                    fakeTrello.boards[boardId].updateName(rawInput[3])
                    print( {
                        "id": fakeTrello.boards[boardId].id,
                        "name": fakeTrello.boards[boardId].name,
                        "privacy": fakeTrello.boards[boardId].privacy
                    } )
                    continue
                elif(rawInput[2] == "privacy"):
                    fakeTrello.boards[boardId].updatePrivacy(rawInput[3])
                    print( {
                        "id": fakeTrello.boards[boardId].id,
                        "name": fakeTrello.boards[boardId].name,
                        "privacy": fakeTrello.boards[boardId].privacy
                    } )
                    continue
                else:
                    print("Unsupported Action for board")
                    continue
        elif(rawInput[0] == "LIST"):
            if(rawInput[1] == "CREATE"):
                boardId = rawInput[2]
                if(not fakeTrello.validateBoard(boardId)):
                    print("No such board exists in system")
                    continue
                listName = " ".join(rawInput[3:])
                fakeTrello.boards[boardId].addList(listName)
            elif(rawInput[1] == "DELETE"):
                # worst case of no boardId given so we search
                listId = rawInput[2]
                Flag = False
                for board in fakeTrello.boards:
                    if (listId in board.lists):
                        board.removeList(listId)
                        Flag = True
                        break
                if(not Flag):
                    print("List does not exist in system to delete")
                    continue
                else:
                    print("List deleted sucessfully")
            else:
                if(rawInput[2] == "ADD_CARD"):
                    if(rawInput[3] not in self.freeCards):
                        print("Requested addition of card is not free")
                        continue
                    # we have to search for addition
                    listId = rawInput[1]
                    Flag = False
                    for board in fakeTrello.boards:
                        if(listId in board.lists):
                            card = self.freeCards[rawInput[3]]
                            board.lists[listId].addCard(card)
                            Flag = True
                            break
                    if(not Flag):
                        print("Card can't be added as we cant find the list in system")
                        continue
                    else:
                        print("Card added successfully")
                        continue
                elif(rawInput[2] == "REMOVE_CARD"):
                    # we have to search for deletion
                    listId = rawInput[1]
                    Flag = False
                    for board in fakeTrello.boards:
                        if(listId in board.lists):
                            board.lists[listId].removeCard(rawInput[3])
                            Flag = True
                            break
                    if(not Flag):
                        # if free card is there to delete
                        if(rawInput[3] in fakeTrello.freeCards):
                            del fakeTrello.freeCards[rawInput[3]]
                            continue
                        print("Card can't be deleted as we cant find the list in system")
                        continue
                    else:
                        print("Card deleted successfully")
                        continue
                elif(rawInput[2] == "name"):
                    # we have to search for updation
                    listId = rawInput[1]
                    Flag = False
                    for board in fakeTrello.boards:
                        if(listId in board.lists):
                            board.lists[listId].updateName(rawInput[3])
                            Flag = True
                            break
                    if(not Flag):
                        print("List name can't be updated as we cant find the list in system")
                        continue
                    else:
                        print("List name updated successfully")
                        continue
                else:
                    print("Unsupported Action for List")
                    continue
        elif(rawInput[0] == "CARD"):
            if(rawInput[1] == "CREATE"):
                cardName = rawInput[2]
                userEmail = rawInput[3]
                user = None
                for user in fakeTrello.users:
                    if(fakeTrello.users[user].email == userEmail):
                        user = fakeTrello.users[user]
                        break
                if(user is None):
                    print("cant create user as no assigned user exists")
                    print("overriding creation by no assigned user")
                    newCard = Card(cardName)
                else:
                    newCard = Card(cardName)
                    newCard.addAssignedUser(user)
                    print("Card created and assigned to user with email provided")
                fakeTrello.freeCards[newCard.id] = newCard
                continue
            elif(rawInput[1] == "DELETE"):
                cardId = rawInput[2]
                # first search in free cards
                if(cardId in fakeTrello.freeCards):
                    del fakeTrello.freeCards[cardId]
                    print("Deleted from free cards")
                    continue
                else:
                    megaFlag = False
                    for board in fakeTrello.boards:
                        Flag = False
                        for List in fakeTrello.boards[board].lists:
                            if(cardId in fakeTrello.boards[board].lists[List]):
                                del fakeTrello.boards[board].lists[List].cards[cardId]
                                print("deleted card successfully")
                                Flag = True
                                megaFlag = True
                                break
                        if(Flag):
                            break
                    if(not megaFlag):
                        print("Card not Found hence can't be deleted")
                    continue
            else:
                if(rawInput[2] == "ASSIGN"):
                    cardId = rawInput[1]
                    userId = rawInput[4]
                    if(userId not in fakeTrello.users):
                        print("Assigned to be user does not exist in system")
                        continue
                    user = fakeTrello.users[userId]
                    # first search in free cards
                    if(cardId in fakeTrello.freeCards):
                        fakeTrello.freeCards[cardId].addAssignedUser(user.id)
                        print("User assigned to free card")
                        continue
                    else:
                        megaFlag = False
                        for board in fakeTrello.boards:
                            Flag = False
                            for List in fakeTrello.boards[board].lists:
                                if(cardId in fakeTrello.boards[board].lists[List]):
                                    fakeTrello.boards[board].lists[List].cards[cardId].addAssignedUser(user.id)
                                    print("user assigned to card in specific board and list")
                                    Flag = True
                                    megaFlag = True
                                    break
                            if(Flag):
                                break
                        if(not megaFlag):
                            print("Card not Found hence can't be assigned with user")
                        continue
                elif(rawInput[2] == "UNASSIGN"):
                    cardId = rawInput[1]
                    # first search in free cards
                    if(cardId in fakeTrello.freeCards):
                        fakeTrello.freeCards[cardId].removeAssignedUser()
                        print("User unassigned to free card")
                        continue
                    else:
                        megaFlag = False
                        for board in fakeTrello.boards:
                            Flag = False
                            for List in fakeTrello.boards[board].lists:
                                if(cardId in fakeTrello.boards[board].lists[List]):
                                    fakeTrello.boards[board].lists[List].cards[cardId].removeAssignedUser()
                                    print("user unassigned to card in specific board and list")
                                    Flag = True
                                    megaFlag = True
                                    break
                            if(Flag):
                                break
                        if(not megaFlag):
                            print("Card not Found hence can't be unassigned")
                        continue
                elif(rawInput[2] == "MOVE"):
                    cardId = rawInput[1]
                    # first search in free cards
                    if(cardId in fakeTrello.freeCards):
                        card = fakeTrello.freeCards[cardId]
                        del fakeTrello.freeCards[cardId]
                    else:
                        megaFlag = False
                        for board in fakeTrello.boards:
                            Flag = False
                            for List in fakeTrello.boards[board].lists:
                                if(cardId in fakeTrello.boards[board].lists[List]):
                                    card = fakeTrello.boards[board].lists[List].cards[cardId]
                                    del fakeTrello.boards[board].lists[List].cards[cardId]
                                    Flag = True
                                    megaFlag = True
                                    break
                            if(Flag):
                                break
                        if(not megaFlag):
                            print("Card not Found hence can't be moved")
                            continue
                    listId = rawInput[3]
                    for board in fakeTrello.boards:
                        if(listId in fakeTrello.boards[board].lists):
                            fakeTrello.boards[board].lists[listId].cards[cardId] = card
                            break
                    print("Card moved successfully")
                    continue
                elif(rawInput[2] == "DELETE"):
                    cardId = rawInput[2]
                    # first search in free cards
                    if(cardId in fakeTrello.freeCards):
                        del fakeTrello.freeCards[cardId]
                        print("Deleted from free cards")
                        continue
                    else:
                        megaFlag = False
                        for board in fakeTrello.boards:
                            Flag = False
                            for List in fakeTrello.boards[board].lists:
                                if(cardId in fakeTrello.boards[board].lists[List]):
                                    del fakeTrello.boards[board].lists[List].cards[cardId]
                                    print("deleted card successfully")
                                    Flag = True
                                    megaFlag = True
                                    break
                            if(Flag):
                                break
                        if(not megaFlag):
                            print("Card not Found hence can't be deleted")
                        continue
                elif(rawInput[2] == "name"):
                    cardId = rawInput[1]
                    newName = " ".join(rawInput[3:])
                    # first search in free cards
                    if(cardId in fakeTrello.freeCards):
                        fakeTrello.freeCards[cardId].updateName(newName)
                        print("Card name updated in free cards")
                        continue
                    else:
                        megaFlag = False
                        for board in fakeTrello.boards:
                            Flag = False
                            for List in fakeTrello.boards[board].lists:
                                if(cardId in fakeTrello.boards[board].lists[List]):
                                    fakeTrello.boards[board].lists[List].cards[cardId].updateName(newName)
                                    print("Card name updated in list and board")
                                    Flag = True
                                    megaFlag = True
                                    break
                            if(Flag):
                                break
                        if(not megaFlag):
                            print("Card not Found hence can't be updated for name")
                        continue
                elif(rawInput[2] == "description"):
                    cardId = rawInput[1]
                    newDescription = " ".join(rawInput[3:])
                    # first search in free cards
                    if(cardId in fakeTrello.freeCards):
                        fakeTrello.freeCards[cardId].updateDescription(newDescription)
                        print("Card nadescriptionme updated in free cards")
                        continue
                    else:
                        megaFlag = False
                        for board in fakeTrello.boards:
                            Flag = False
                            for List in fakeTrello.boards[board].lists:
                                if(cardId in fakeTrello.boards[board].lists[List]):
                                    fakeTrello.boards[board].lists[List].cards[cardId].updateDescription(newDescription)
                                    print("Card description updated in list and board")
                                    Flag = True
                                    megaFlag = True
                                    break
                            if(Flag):
                                break
                        if(not megaFlag):
                            print("Card not Found hence can't be updated for description")
                        continue
                else:
                    print("Unsupported Action for Card")
        elif(rawInput[0] == "SHOW"):
            if(len(rawInput) == 1):
                # show all
                res = []
                for board in fakeTrello.boards:
                    res.append( {
                        "id": fakeTrello.boards[board].id,
                        "name": fakeTrello.boards[board].name,
                        "privacy": fakeTrello.boards[board].privacy
                    } )
                if(len(res) == 0):
                    print("No board")
                else:
                    print(res)
                continue
            if(rawInput[1] == "BOARD"):
                boardId = rawInput[2]
                if(boardId in fakeTrello.boards):
                    board = fakeTrello.boards[boardId]
                    print({
                        "id": board.id,
                        "name": board.name,
                        "privacy": board.privacy
                    })
                    continue
                else:
                    print("Board does not exist in system to show")
                    continue
            elif(rawInput[1] == "LIST"):
                listId = rawInput[2]
                for board in fakeTrello.boards:
                    if(listId in fakeTrello.boards[board].lists):
                        List = fakeTrello.boards[board].lists[listId]
                        print( {
                            "id": List.id,
                            "name": List.name,
                            "cards": [ {
                                "id": card.id,
                                "name": card.name,
                                "description": card.description,
                                "assignedTo": card.assignedUser
                            } for card in List.cards]
                        } )
                        break
                continue
            elif(rawInput[1] == "CARD"):
                cardId = rawInput[2]
                if(cardId in fakeTrello.freeCards):
                    card = fakeTrello.freeCards[cardId]
                    print( {
                        "id": card.id,
                        "name": card.name
                    } )
                    continue
                else:
                    megaFlag = False
                    for board in fakeTrello.boards:
                        Flag = False
                        for listId in fakeTrello.boards[board].lists:
                            if(cardId in fakeTrello.boards[board].lists[listId].cards):
                                card = fakeTrello.boards[board].lists[listId].cards[cardId]
                                print( {
                                    "id": card.id,
                                    "name": card.name
                                } )
                                Flag = True
                                megaFlag = True
                                break
                        if(Flag):
                            break
                    if(not megaFlag):
                        print("Card not found")
                    continue
            else:
                print("Unsupprted action for showing things in system")
        else:
            print("Unsupported Action Type")
            continue

if __name__=="__main__":
    main()