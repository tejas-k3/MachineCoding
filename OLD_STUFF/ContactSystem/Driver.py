from ContactSystem import ContactSystem


def main():
    contactSystem = ContactSystem()
    while True:
        command = input()
        commands = command.split()
        commandType = commands[0]
        match commandType:
            # Input format example :- ADD T K 9812312
            case "ADD":
                contactSystem.addContact(commands[1], commands[2], commands[3])
            # Input format example :- UPDATE 9812312 FIRSTNAME Abhi
            case "UPDATE":
                contactSystem.updateContact(commands[1], commands[2], commands[3])
            # Input format example :- SEARCH NAME AN
            case "SEARCH":
                searchResult = contactSystem.searchContact(commands[1], commands[2])
                count = len(searchResult)
                if count > 0:
                    print("Number of contacts found :", count)
                    for result in searchResult:
                        print("FirstName :", result.getFirstName())
                        print("LastName :", result.getLastName())
                        print("Phone Number :", result.getPhoneNumber())
                else:
                    print("No contacts!")

if __name__ == "__main__":
    main()
