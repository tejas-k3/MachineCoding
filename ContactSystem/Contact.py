class Contact:
    def __init__(self, firstName: str, lastName: str, phoneNumber: str):
        """
        Initializing Contact with provided values.
        :param firstName: String
        :param lastName: String
        :param phoneNumber: String
        """
        self.firstName = firstName
        self.lastName = lastName
        self.phoneNumber = phoneNumber

    def getFirstName(self):
        """
        Method to return first name of the contact.
        :return: String
        """
        return self.firstName

    def getLastName(self):
        """
        Method to return last name of the contact.
        :return: String
        """
        return self.lastName

    def getPhoneNumber(self):
        """
        Method to return phone number of the contact.
        :return: String
        """
        return self.phoneNumber

    def updatePhoneNumber(self, phoneNumber: str):
        """
        Method to update phone number
        :param phoneNumber:
        :return: None
        """
        self.phoneNumber = phoneNumber

    def updateFirstName(self, firstName: str):
        """
        Method to update first name
        :param self:
        :param firstName:
        :return: None
        """
        self.firstName = firstName

    def updateLastName(self, lastName: str):
        """
        Method to update last name
        :param self:
        :param lastName:
        :return:
        """
        self.lastName = lastName
