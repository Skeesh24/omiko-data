from abc import abstractclassmethod, ABC

from app.models.validation import FilterRequestModel


class IRepository(ABC):
    @abstractclassmethod
    def get(self, limit: int, offset: int, document_id: str, where: FilterRequestModel):
        pass

    @abstractclassmethod
    def get_all(self, where: FilterRequestModel):
        pass

    @abstractclassmethod
    def add(self, element):
        pass

    @abstractclassmethod
    def update(self, document_id: str, element):
        pass

    @abstractclassmethod
    def remove(self, document_id: str):
        pass
