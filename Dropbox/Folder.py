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
    def id(self, new_id: str):
        self._id = new_id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name: str):
        self._name = new_name

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, new_location: str):
        self._location = new_location

    @property
    def extension(self):
        return self._extension

    @extension.setter
    def extension(self, new_extension: str):
        self._extension = new_extension

    @property
    def sizeInBytes(self):
        return self._sizeInBytes

    @sizeInBytes.setter
    def sizeInBytes(self, new_size: int):
        self._sizeInBytes = new_size

    @property
    def chunkCount(self):
        return self._chunkCount

    @chunkCount.setter
    def chunkCount(self, new_count: int):
        self._chunkCount = new_count

    @property
    def updatedTime(self):
        return self._updatedTime

    @updatedTime.setter
    def updatedTime(self, new_time: str):
        self._updatedTime = new_time

    @property
    def updatedBy(self):
        return self._updatedBy

    @updatedBy.setter
    def updatedBy(self, new_user: str):
        self._updatedBy = new_user