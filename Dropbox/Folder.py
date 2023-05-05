from .PermissionType import PermissionType
class Folder:
    def __init__(self, id: str, ownerId: str, permission: PermissionType, updatedTime: str):
        self._id = id
        self._ownerId = ownerId
        self._permission = permission
        self._updatedTime = updatedTime

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def ownerId(self):
        return self._ownerId

    @ownerId.setter
    def ownerId(self, ownerId):
        self._ownerId = ownerId

    @property
    def permission(self):
        return self._permission

    @permission.setter
    def permission(self, permission):
        self._permission = permission

    @property
    def updatedTime(self):
        return self._updatedTime

    @updatedTime.setter
    def updatedTime(self, updatedTime):
        self._updatedTime = updatedTime
