from Contact import Contact


class ContactSystem:
    def __init__(self):
        """
        Initializing dictionary to save contacts
        """
        self.contacts = dict()

    def addContact(self, firstName: str, lastName: str, phoneNumber: str):
        """
        Method to add contact with provided values
        :param firstName: String
        :param lastName: String
        :param phoneNumber: String
        :return: None
        """
        self.contacts[phoneNumber] = Contact(firstName, lastName, phoneNumber)
        print("Contact added successfully")

    # def deleteContact(self, phoneNumber):
    #     del self.contacts[phoneNumber]
    #     pass

    # Total count & Search Result
    def searchContact(self, searchValueType: str, value: str):
        """
        Method to search contact on the basis of either NAME or PHONENUMBER with provided value.
        :param searchValueType: String
        :param value: String
        :return: List of contacts
        """
        searchResult = []
        # Will be replaced by SearchAlgorithm class
        match searchValueType:
            case 'NAME':
                for contact in self.contacts:
                    # Case-insensitive lookup in firstname and lastname of the contact
                    if value.lower() in [name.lower() for name in [self.contacts[contact].getFirstName(),
                                                               self.contacts[contact].getLastName()]]:
                        searchResult.append(self.contacts[contact])
            case 'PHONENUMBER':
                searchResult = [self.contacts[contact] for contact in self.contacts if value in contact]
        if len(searchResult) > 0:
            print("Contacts found with lookup type {}".format(type))
        return searchResult

    def updateContact(self, phoneNumber, updateValueType: str, value: str):
        """
        Method to Update contact for existing phonenumber
        :param phoneNumber: String
        :param updateValueType: String
        :param value: String
        :return: None
        """
        if phoneNumber in self.contacts:
            match updateValueType:
                case "FIRSTNAME":
                    self.contacts[phoneNumber].updateFirstName(value)
                    print("Updated first name successfully for {}".format(phoneNumber))
                case "LASTNAME":
                    self.contacts[phoneNumber].updateLastName(value)
                    print("Updated last name successfully for {}".format(phoneNumber))
                case "PHONENUMBER":
                    self.contacts[value] = self.contacts[phoneNumber]
                    self.contacts[value].updatePhoneNumber(value)
                    del self.contacts[phoneNumber]
                    print("Updated phone number successfully for {}".format(value))
