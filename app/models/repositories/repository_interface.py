from abc import abstractclassmethod, ABC


class IRepository(ABC):
    @abstractclassmethod
    def get_by_id(self, id: int):
        pass

    @abstractclassmethod
    def get_all(self):
        pass

    @abstractclassmethod
    def add(self, element):
        pass

    @abstractclassmethod
    def update(self, id: int, element):
        pass

    @abstractclassmethod
    def remove_by_id(self, id: int):
        pass

    @abstractclassmethod
    def remove(self, element):
        pass
