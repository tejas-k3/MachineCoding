class User:
    def __init__(self, id: str, userName: str, folderId: str, emailAddress: str, registrationDate: str):
        """
        Initializing User with provided values.
        """
        self._id = id
        self._userName = userName
        self._folderId = folderId
        self._emailAddress = emailAddress
        self._registrationDate = registrationDate
    
    @property
    def id(self) -> str:
        return self._id

    @property
    def userName(self) -> str:
        return self._userName

    @property
    def folderId(self) -> str:
        return self._folderId

    @property
    def emailAddress(self) -> str:
        return self._emailAddress

    @property
    def registrationDate(self) -> str:
        return self._registrationDate

    @id.setter
    def id(self, new_id: str):
        self._id = new_id

    @userName.setter
    def userName(self, new_userName: str):
        self._userName = new_userName

    @folderId.setter
    def folderId(self, new_folderId: str):
        self._folderId = new_folderId

    @emailAddress.setter
    def emailAddress(self, new_emailAddress: str):
        self._emailAddress = new_emailAddress

    @registrationDate.setter
    def registrationDate(self, new_registrationDate: str):
        self._registrationDate = new_registrationDate




