class User:
    def __init__(self, id, name, email, phone):
        self.__id = id
        self.__name = name
        self.__email = email
        self.__phone = phone

    def getId(self):
        return self.__id

    def setId(self, id):
        self.__id = id

    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name

    def getEmail(self):
        return self.__email

    def setEmail(self, email):
        self.__email = email

    def getPhone(self):
        return self.__phone

    def setPhone(self, phone):
        self.__phone = phone
