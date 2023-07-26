from abc import abstractclassmethod, ABC


class IRepository(ABC):
    @abstractclassmethod
    def get(self, document_id: str):
        pass

    @abstractclassmethod
    def get_all(self):
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
