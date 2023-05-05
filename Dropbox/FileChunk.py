
class FileChunck:
    def __init__(self, id: str, fileId: str, location: str, sizeInBytes: int, nextChunk: int, updatedTime: str, updatedBy: str):
        """
        Initializing File Chunk with provided values.
        """
        self._id = id
        self._fileId = fileId
        self._location = location
        self._sizeInBytes = sizeInBytes
        self._nextChunk = nextChunk
        self._updatedTime = updatedTime
        self._updatedBy = updatedBy

    @property
    def id(self) -> str:
        return self._id
    
    @property
    def fileId(self) -> str:
        return self._fileId
    
    @property
    def location(self) -> str:
        return self._location
    
    @property
    def sizeInBytes(self) -> int:
        return self._sizeInBytes
    
    @property
    def nextChunk(self) -> int:
        return self._nextChunk
    
    @property
    def updatedTime(self) -> str:
        return self._updatedTime
    
    @property
    def updatedBy(self) -> str:
        return self._updatedBy
    
    @id.setter
    def id(self, new_id: str):
        self._id = new_id
    
    @fileId.setter
    def fileId(self, new_fileId: str):
        self._fileId = new_fileId
    
    @location.setter
    def location(self, new_location: str):
        self._location = new_location
    
    @sizeInBytes.setter
    def sizeInBytes(self, new_size: int):
        self._sizeInBytes = new_size
    
    @nextChunk.setter
    def nextChunk(self, nextChunk: int):
        self._nextChunk = nextChunk
    
    @updatedTime.setter
    def updatedTime(self, new_time: str):
        self._updatedTime = new_time
    
    @updatedBy.setter
    def updatedBy(self, new_user: str):
        self._updatedBy = new_user